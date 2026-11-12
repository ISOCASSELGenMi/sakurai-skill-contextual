# sakurai-skill

YouTube「[桜井政博のゲーム作るには](https://www.youtube.com/@sora_sakurai_jp)」の**全本編257本の字幕**から作った、ゲーム制作の原則をまとめた Agent Skill（Claude Code などで使える `SKILL.md`）です。

ゲームの企画・ゲーム性・難易度・ご褒美・導入・操作感（ヒットストップ、ジャンプ、カメラ）・モーション・エフェクト・グラフィック・UI・サウンド・パラメーター調整・デバッグ・チーム運営・企画書・広報を考えるとき、レビューするとき、「手応えがない」「もっさり」と言われて直すときに使います。

> 非公式のファンメイドです。桜井政博氏・有限会社ソラとは関係ありません。中身は動画の内容を AI が要約したもので、桜井氏の発言そのものではありません。正確な内容は元の動画で確かめてください。

## 入れ方

```bash
git clone https://github.com/kociden/sakurai-skill.git
cp -r sakurai-skill/skills/sakurai ~/.claude/skills/
```

Claude Code では「桜井さんならどうする？」「このゲームの手応えをレビューして」などと頼むと読み込まれます。

## 中身

```
skills/sakurai/
  SKILL.md            原則の要約（14章）と、レビュー・企画・手応えの直しの手順
  references/         動画ごとの要点をカテゴリ別に並べたもの（必要なときだけ読む）
    gameplay.md  planning.md  concepts.md  specs.md  motion.md  effects.md  graphics.md
    ui.md  sound.md  tech.md  team.md  mindset.md  pr.md  misc.md
tools/
  to_text.py          字幕（srv1）を時刻なしの本文にする
  build_refs.py       要点メモをカテゴリ別の references/ に並べ替える
```

- `SKILL.md` は約2.7万字。読み込みを軽くするため、具体的な数値・手順・作品例は `references/` に分け、必要なカテゴリだけを読む作りです。
- 各要点には動画の通し番号（古い順の 001〜259）とタイトルを付けているので、元の動画をたどれます。

## 作り方

1. `yt-dlp` でチャンネルの全動画（300本）を一覧にし、中身が重複するまとめ動画41本を除いた259本の日本語自動字幕を取得（257本で取得できました。2本は字幕なし）。
2. 時刻・タグを捨てて1動画1段落の本文にする（約30万字）。
3. 25本前後ずつ Claude（Sonnet）に読ませ、1動画につき2〜5行の要点に要約（約16万字）。自動字幕の誤変換は文脈から直させています。
4. Claude（Opus）が全要点を読んで `SKILL.md` に統合し、要点は `references/` にカテゴリ別に並べ替え。

字幕の本文そのものは著作物なので、このリポジトリには入れていません。手元で作り直すときの手順は `tools/` を参照してください。

```bash
yt-dlp --extractor-args "youtube:lang=ja" --flat-playlist --print "%(id)s	%(title)s	%(duration)s" \
  "https://www.youtube.com/channel/UC5CTV3JSdrlo5Pa42QkK8SA/videos" > list.tsv
grep -v まとめ list.tsv | cut -f1 | sed 's#^#https://www.youtube.com/watch?v=#' > urls.txt
yt-dlp --extractor-args "youtube:lang=ja" --skip-download --write-auto-subs --sub-langs "ja-orig,ja" \
  --sub-format srv1 --sleep-subtitles 2 -o "raw/%(id)s.%(ext)s" -a urls.txt
python tools/to_text.py              # text/ に本文ができる（list.tsv と raw/ を同じ場所に置く）
# text/ を AI で要約して notes/*.md（"## 番号 タイトル" + 箇条書き）を作り、
python tools/build_refs.py skills/sakurai/references
```

## 既存の Sakurai-Skills との違い

同じチャンネルを元にしたスキルに [kokuren333/Sakurai-Skills](https://github.com/kokuren333/Sakurai-Skills) があります（このリポジトリより先に公開されています）。目的は近いですが、作り方と向きが違います。

| | kokuren333/Sakurai-Skills | このリポジトリ |
|---|---|---|
| 元にした物 | まとめ動画（雑談を除く）を Gemini が要約した中間メモ。README によると動画との照合はしていない | 全本編257本の自動字幕を直接取得して要約 |
| 範囲 | 原則177件＋横断原則17件 | 動画257本すべて（雑談回も `misc.md` に収録） |
| 言語 | 英語が中心（日本語 README あり） | 日本語 |
| 形 | 24個のタスク別スキル、ルーター、チェックリスト、原則グラフ、lint ルール、テストまで揃った体系的な作り | スキル1つ（SKILL.md＋参照14ファイル）の軽い作り |
| 出典のたどり方 | SOURCE / GENERALIZED / AGENT の3層で、元メモの記述と解釈を分けて記録 | 要点ごとに動画番号とタイトル |
| 向いている使い方 | 大きなプロジェクトで、工程ごとのレビューや点検を体系的に回す | 普段の会話で手軽に読み込み、具体的な数値・手順・作品例まで引く |

どちらも AI による要約で、人の目で全部を照合したものではありません。このリポジトリは元が自動字幕なので、聞き取りの誤りが要約に残っている可能性があります。

## 注意

- 原則は桜井氏の大作・アクション寄りの経験に基づくので、ジャンルや規模に合わない所はそのまま当てはめず、狙い（遊ぶ人を楽しませること）から読み替える前提で書いています。
- 誤りや抜けを見つけたら issue で教えてください。
