#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
钠电文献日报 —— 抓取 arXiv 与 Crossref 上与钠离子电池相关的新文献。

只用标准库，不需要 pip install。
每天由 GitHub Actions 自动跑一次，结果自动提交回仓库。

本地试跑：
    python fetch_papers.py
"""

import json
import os
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CFG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
UA = {"User-Agent": "sodium-paper-daily/1.0 (mailto:%s)" % CFG.get("mailto", "")}

# 有些校园网/公司网会做 SSL 中间人（自签证书），导致 CERTIFICATE_VERIFY_FAILED。
# 默认严格校验；本地实在连不上时，设环境变量 ALLOW_INSECURE_SSL=1 跳过校验。
# GitHub Actions 上不需要这个变量，那边的证书链是完整的。
SSL_CTX = ssl._create_unverified_context() if os.environ.get("ALLOW_INSECURE_SSL") == "1" else None

ATOM = {"a": "http://www.w3.org/2005/Atom"}

# 相关性过滤：标题/摘要里必须同时出现"钠"和"电池"两类词，否则丢掉
# 相关性过滤。经验：只用"sodium + battery"两个词会混进一堆噪声
# （钠铁酸盐净水、嗜盐菌耐盐、葡萄糖传感、镁硫电池加碘化钠……），
# 所以必须命中"钠离子电池"这个强特征，才认为相关。
STRONG_RE = re.compile(
    r"sodium[-\s]?ion|na[-\s]?ion|\bsibs?\b|sodium[-\s]batter|"
    r"sodium[-\s]metal|sodium[-\s]storage|sodium[-\s]insertion|"
    r"nasicon|prussian[-\s]blue|nafepo4|na3v2|nfpp|nfpo|nafeo2|na\+",
    re.I)
CONTEXT_RE = re.compile(r"batter|cathode|anode|electrode|electrolyte|intercalation", re.I)


def strip_tags(text):
    return re.sub(r"<[^>]+>", " ", text or "")


def norm_title(text):
    """标题归一化，用来跨来源去重（Angew 的 anie/ange 是同一篇，两个 DOI）。"""
    t = strip_tags(text).lower()
    return re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "", t)


def relevant(rec):
    blob = strip_tags(rec.get("title", "")) + " " + strip_tags(rec.get("abstract", ""))
    return bool(STRONG_RE.search(blob)) and bool(CONTEXT_RE.search(blob))


def log(msg):
    print(msg, flush=True)


def http_get(url, timeout=30, retries=2):
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout, context=SSL_CTX) as r:
                return r.read()
        except Exception as e:  # 单次失败不影响整体
            last = e
            time.sleep(2 + i * 3)
    raise last


def clean(text):
    if not text:
        return ""
    return re.sub(r"\s+", " ", text).strip()


# ---------------------------------------------------------------- arXiv
def fetch_arxiv(since_date):
    out = []
    for q in CFG["arxiv_queries"]:
        url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({
            "search_query": q,
            "start": 0,
            "max_results": CFG["max_per_query_arxiv"],
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        })
        try:
            root = ET.fromstring(http_get(url))
        except Exception as e:
            log("  [arxiv] 查询失败：%s → %s" % (q, e))
            continue

        for e in root.findall("a:entry", ATOM):
            raw_id = clean(e.findtext("a:id", default="", namespaces=ATOM))
            m = re.search(r"abs/([^v]+)", raw_id)
            aid = m.group(1) if m else raw_id
            published = clean(e.findtext("a:published", default="", namespaces=ATOM))
            day = published[:10]
            if not day or day < since_date:
                continue
            authors = [clean(a.findtext("a:name", default="", namespaces=ATOM))
                       for a in e.findall("a:author", ATOM)]
            rec = {
                "key": "arxiv:" + aid,
                "source": "arXiv",
                "title": clean(strip_tags(e.findtext("a:title", default="", namespaces=ATOM))),
                "abstract": clean(e.findtext("a:summary", default="", namespaces=ATOM)),
                "date": day,
                "url": "https://arxiv.org/abs/" + aid,
                "venue": "arXiv preprint",
                "authors": authors[:3],
                "query": q,
            }
            if rec["title"] and relevant(rec):
                out.append(rec)
        time.sleep(2)  # arXiv 要求别打太快
    return out


# ---------------------------------------------------------------- Crossref
def fetch_crossref(since_date):
    """按"入库时间"抓，不是按出版日期。
    按出版日期排会抓到 2027、2028 年排期的期刊（真实存在），没法用。"""
    out = []
    fields = "DOI,title,container-title,published,created,author,URL,abstract"
    for q in CFG["crossref_queries"]:
        url = "https://api.crossref.org/works?" + urllib.parse.urlencode({
            "query.bibliographic": q,
            "filter": "from-created-date:%s,type:journal-article" % since_date,
            "rows": CFG["max_per_query_crossref"],
            "select": fields,
            "sort": "created",
            "order": "desc",
        })
        try:
            data = json.loads(http_get(url).decode("utf-8"))
        except Exception as e:
            log("  [crossref] 查询失败：%s → %s" % (q, e))
            continue

        for it in data.get("message", {}).get("items", []):
            title = clean(strip_tags((it.get("title") or [""])[0]))
            if not title:
                continue
            created = (it.get("created") or {}).get("date-time", "")[:10]
            if not created or created < since_date:
                continue
            parts = (it.get("published") or {}).get("date-parts") or [[None]]
            issue = ""
            if parts and len(parts[0]) >= 3:
                issue = "%04d-%02d-%02d" % tuple(parts[0][:3])
            abstract = strip_tags(it.get("abstract", ""))
            abstract = re.sub(r"^\s*abstract[:\s]*", "", abstract, flags=re.I)
            names = []
            for a in (it.get("author") or [])[:3]:
                n = (a.get("given", "") + " " + a.get("family", "")).strip()
                if n:
                    names.append(n)
            rec = {
                "key": "doi:" + it.get("DOI", "").lower(),
                "source": "Crossref",
                "title": title,
                "abstract": clean(abstract),
                "date": created,
                "issue_date": issue,
                "url": it.get("URL") or ("https://doi.org/" + it.get("DOI", "")),
                "venue": clean((it.get("container-title") or [""])[0]),
                "authors": names,
                "query": q,
            }
            if relevant(rec):
                out.append(rec)
        time.sleep(1)
    return out


# ---------------------------------------------------------------- 输出
def md_title(t):
    return t.replace("[", "\\[").replace("]", "\\]")


def short(text, n=240):
    text = text or ""
    return text if len(text) <= n else text[:n].rstrip() + "…"


def render_items(recs):
    lines = []
    for r in recs:
        authors = ""
        if r.get("authors"):
            authors = "、".join(r["authors"])
            if len(r["authors"]) >= 3:
                authors += " 等"
        meta = " · ".join(x for x in [r.get("date", ""), r.get("venue", ""), authors] if x)
        if r.get("issue_date"):
            meta += "（期刊期次 %s）" % r["issue_date"]
        lines.append("- **[%s](%s)**  " % (md_title(r["title"]), r["url"]))
        lines.append("  <sub>%s</sub>  " % meta)
        if r.get("abstract"):
            lines.append("  > %s" % short(r["abstract"]))
        lines.append("")
    return lines


def build_digest(recs, day):
    lines = ["# 钠电文献日报 · %s" % day, ""]
    if not recs:
        lines.append("今天没有抓到新文献。可能是周末、arXiv 未更新，或关键词太窄。")
        return "\n".join(lines) + "\n"
    arx = [r for r in recs if r["source"] == "arXiv"]
    cr = [r for r in recs if r["source"] == "Crossref"]
    lines.append("共 %d 篇：arXiv %d 篇，Crossref %d 篇。" % (len(recs), len(arx), len(cr)))
    lines.append("")
    if arx:
        lines += ["## arXiv 预印本", ""] + render_items(arx)
    if cr:
        lines += ["## Crossref 期刊", ""] + render_items(cr)
    return "\n".join(lines)


def build_readme(recs, total, updated_at):
    head = [
        "# 钠电文献日报",
        "",
        "每天自动抓取 **arXiv 预印本** 与 **Crossref 期刊** 上钠离子电池相关的新文献。",
        "",
        "**最近更新**：%s　·　**今日新增**：%d 篇　·　**累计收录**：%d 篇" % (updated_at, len(recs), total),
        "",
        "---",
        "",
        "## 今日新增",
        "",
    ]
    if not recs:
        body = ["今天没有新文献。若连续几天为空，请检查 `config.json` 里的关键词。", ""]
    else:
        limit = CFG.get("max_listed_in_readme", 40)
        shown = recs[:limit]
        body = render_items(shown)
        if len(recs) > limit:
            body.append("> 还有 %d 篇，见 `digest/%s.md`。" % (len(recs) - limit, updated_at[:10]))
            body.append("")

    tail = [
        "---",
        "",
        "<details>",
        "<summary>使用说明（点开）</summary>",
        "",
        "**改关键词**：编辑 `config.json` 里的 `arxiv_queries` 和 `crossref_queries`，提交后第二天生效。",
        "",
        "**马上跑一次**：仓库页 → Actions → 左侧「钠电文献日报」→ 右侧 Run workflow。",
        "",
        "**改时间**：`.github/workflows/daily.yml` 里的 `cron: \"0 23 * * *\"` 是 UTC，23:00 UTC = 北京时间次日 07:00。想改北京时间 08:00 就写 `0 0 * * *`。",
        "",
        "**往期存档**：`digest/` 目录，一天一个 md 文件。",
        "",
        "**去重**：`data/papers.json` 记录所有见过的文献，同一篇不会重复出现。想重新来过就清空这个文件。",
        "",
        "**为什么某天没有新文献**：arXiv 周末不更新，Crossref 期刊也有淡季。连续三天为空才需要检查配置。",
        "",
        "</details>",
        "",
    ]
    return "\n".join(head + body + tail)


def main():
    today = datetime.now(timezone.utc).date()
    since = (today - timedelta(days=int(CFG.get("days_back", 3)))).isoformat()
    since_date = since

    log("开始抓取，起始日期 %s" % since_date)
    recs = []
    log("→ arXiv")
    recs += fetch_arxiv(since_date)
    log("  arXiv 命中 %d 条" % len([r for r in recs if r["source"] == "arXiv"]))
    log("→ Crossref")
    before = len(recs)
    recs += fetch_crossref(since_date)
    log("  Crossref 命中 %d 条" % (len(recs) - before))

    # 合并去重：①同一篇被多条 query 命中；②同一篇有多个 DOI（Angew 的 anie/ange）
    uniq = {}
    for r in recs:
        uniq.setdefault(r["key"], r)
    recs = list(uniq.values())

    data_dir = ROOT / "data"
    data_dir.mkdir(exist_ok=True)
    db_path = data_dir / "papers.json"
    db = json.loads(db_path.read_text(encoding="utf-8")) if db_path.exists() else {"papers": {}}
    db.setdefault("papers", {})

    title_index = {norm_title(p.get("title", "")) for p in db["papers"].values()}

    today_str = today.isoformat()
    fresh = 0
    for r in recs:
        nt = norm_title(r["title"])
        if r["key"] in db["papers"] or nt in title_index:
            continue
        r2 = dict(r)
        r2["first_seen"] = today_str
        db["papers"][r["key"]] = r2
        title_index.add(nt)
        fresh += 1
    log("新增 %d 篇，累计 %d 篇" % (fresh, len(db["papers"])))
    db_path.write_text(json.dumps(db, ensure_ascii=False, indent=1), encoding="utf-8")

    # 今日新增 = first_seen 是今天的（保证重跑结果一致）
    todays = [p for p in db["papers"].values() if p.get("first_seen") == today_str]
    todays.sort(key=lambda x: (x.get("date", ""), x.get("source", "")), reverse=True)

    digest_dir = ROOT / "digest"
    digest_dir.mkdir(exist_ok=True)
    (digest_dir / ("%s.md" % today_str)).write_text(
        build_digest(todays, today_str), encoding="utf-8")

    updated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    (ROOT / "README.md").write_text(
        build_readme(todays, len(db["papers"]), updated_at), encoding="utf-8")
    log("完成：README.md 与 digest/%s.md 已更新" % today_str)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log("运行失败：%s" % e)
        sys.exit(1)
