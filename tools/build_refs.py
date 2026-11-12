# notes/*.md の要点を【カテゴリ】ごとに並べ替えて、スキルの references/ に書き出す。
# 同じ番号の重複は先に出た方を残し、「知見少なめ」だけの動画（雑談など）は misc に回す。
import re, sys, pathlib

root = pathlib.Path(__file__).parent
out = pathlib.Path(sys.argv[1])
out.mkdir(parents=True, exist_ok=True)

CATS = {
    "ゲーム性": ("gameplay", "ゲーム性（リスクとリターン・駆け引き・難易度・報酬）"),
    "企画・ゲーム設計": ("planning", "企画・ゲーム設計（導入・チュートリアル・ご褒美・時間・独自性）"),
    "企画コンセプト": ("concepts", "企画コンセプト（桜井作品ごとの課題と解決）"),
    "仕様": ("specs", "仕様（ヒットストップ・ジャンプ・カメラ・崖・遷移・ランダム）"),
    "モーション": ("motion", "モーション（構え・攻撃ポーズ・フォロースルー・誇張）"),
    "エフェクト": ("effects", "エフェクト（ヒットマーク・爆発・画面振動・フラッシュ）"),
    "グラフィック": ("graphics", "グラフィック（光・スケール・判定の強調・監修）"),
    "UI": ("ui", "UI（メニュー・文字・HUD・キーコンフィグ・スキップ）"),
    "サウンド": ("sound", "サウンド（効果音の優先度・アタック・BGM・アレンジ）"),
    "プログラム・テクニカル": ("tech", "プログラム・テクニカル（パラメーター・デバッグモード・管理）"),
    "チーム運営": ("team", "チーム運営（決断・情報共有・デバッグ体制・職種）"),
    "仕事の姿勢": ("mindset", "仕事の姿勢（企画書・プレゼン・コンセプトを貫く）"),
    "広報": ("pr", "広報（ゲーム画面を見せる・製品像・体験版・発信）"),
}
MISC = ("misc", "雑談・その他（知見少なめを含む）")

text = "\n".join(p.read_text(encoding="utf-8") for p in sorted((root / "notes").glob("*.md")))
blocks = re.split(r"(?m)^(?=## \d{3} )", text)
seen, groups = set(), {}
for b in blocks:
    m = re.match(r"## (\d{3}) (.*)", b)
    if not m:
        continue
    num, title = m.groups()
    if num in seen:
        continue
    seen.add(num)
    body = b.strip()
    body = re.sub(r"\n# .*$", "", body, flags=re.S)  # 次ファイルの表題が紛れたら落とす
    cm = re.search(r"【(.+?)】", title)
    key = CATS.get(cm.group(1)) if cm else None
    if key is None or "（知見少なめ）" in body.split("\n", 1)[-1][:12]:
        key = MISC
    groups.setdefault(key, []).append((num, body))

for (slug, name), items in groups.items():
    items.sort()
    s = f"# {name}\n\n桜井政博のゲーム作るには、の字幕から作った要点。番号は動画の通し番号（古い順）。\n\n"
    s += "\n\n".join(b for _, b in items) + "\n"
    (out / f"{slug}.md").write_text(s, encoding="utf-8")
    print(slug, len(items))
print("合計", len(seen))
