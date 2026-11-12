# 字幕(srv1)を、時刻なし・改行なしの本文だけにする。トークン節約のため1動画=1段落。
import html, re, sys, pathlib

root = pathlib.Path(__file__).parent
titles = {}
for line in (root / "list.tsv").read_text(encoding="utf-8").splitlines():
    vid, title, dur = line.split("\t")
    titles[vid] = (title, dur)

out_dir = root / "text"
out_dir.mkdir(exist_ok=True)
order = [l.split("\t")[0] for l in (root / "list.tsv").read_text(encoding="utf-8").splitlines()]
order.reverse()  # 古い順

n = 0
for i, vid in enumerate(order):
    if "まとめ" in titles[vid][0]:
        continue
    n += 1  # 字幕の有無に関わらず番号を固定する（後から足しても番号がずれない）
    f = None
    for lang in ("ja-orig", "ja"):
        p = root / "raw" / f"{vid}.{lang}.srv1"
        if p.exists():
            f = p
            break
    if not f:
        print("字幕なし", vid, titles[vid][0], file=sys.stderr)
        continue
    xml = f.read_text(encoding="utf-8")
    parts = [html.unescape(html.unescape(t)) for t in re.findall(r"<text[^>]*>(.*?)</text>", xml, re.S)]
    body = "".join(p.replace("\n", "").strip() for p in parts)
    body = re.sub(r"\[[^\]]*\]", "", body)  # [音楽] [拍手] など
    body = re.sub(r"\s+", " ", body)
    (out_dir / f"{n:03d}_{vid}.txt").write_text(f"# {titles[vid][0]}\n{body}\n", encoding="utf-8")
print(n, "本")
