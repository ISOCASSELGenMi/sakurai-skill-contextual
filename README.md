# sakurai-skill-contextual

[kociden/sakurai-skill](https://github.com/kociden/sakurai-skill) を基にした、状況に応じた判断を重視する日本語の fork です。元の動画別要約を保存し、参照と判断の流れを変更しています。

## この fork の変更点

- [SKILL.md](skills/sakurai/SKILL.md) は、状況の特定、資料の確認、適用判断、衝突の比較、具体的な提案を案内します。
- [決定カード](skills/sakurai/decisions/) は 7 枚。適用条件、判断案、適用外、関連する出典、根拠の状態を分けています。
- 「出典要約」「編集上の解釈」「今回の提案」を区別し、未確認の条件で矛盾を解消したことにしません。
- 既存の参照 14 ファイル・257 件の要約は変更していません。カードがない話題も参照できます。
- [14 ケースの評価セット](skills/sakurai/evaluation/cases.md) を追加しました。形式・リンク・引用番号の整合性は確認済みですが、モデルの反復比較による命中率の改善は未測定です。原動画の照合も未実施です。

スキル名は `sakurai` のままです。既存版がある場合はバックアップし、使う版を選んでください。

## 元資料について

YouTube「[桜井政博のゲーム作るには](https://www.youtube.com/@sora_sakurai_jp)」の**全本編257本の字幕**から作った、ゲーム制作の原則をまとめた Agent Skill（Claude Code などで使える `SKILL.md`）です。

ゲームの企画・ゲーム性・難易度・ご褒美・導入・操作感（ヒットストップ、ジャンプ、カメラ）・モーション・エフェクト・グラフィック・UI・サウンド・パラメーター調整・デバッグ・チーム運営・企画書・広報を考えるとき、レビューするとき、「手応えがない」「もっさり」と言われて直すときに使います。

> 非公式のファンメイドです。桜井政博氏・有限会社ソラとは関係ありません。中身は動画の内容を AI が要約したもので、桜井氏の発言そのものではありません。正確な内容は元の動画で確かめてください。

## まずは動画で

**[X の紹介ポスト](https://x.com/MvKWt5XpPV36233/status/2120977715864252887)** に、使い方の動画（約100秒）を付けています。このスキルで何ができるか（入れ方・頼み方・手ごたえの足し方・別のAIによるレビュー・レベルデザインの見直しなど）が、作例のゲームと一緒に見られるので、先に見ておくと分かりやすいです。

## 入れ方

```bash
git clone https://github.com/ISOCASSELGenMi/sakurai-skill-contextual.git
mkdir -p ~/.claude/skills
cp -r sakurai-skill-contextual/skills/sakurai ~/.claude/skills/
```

Codex では、同じフォルダを Codex の skills ディレクトリ（標準は `~/.codex/skills/`）へ配置し、`$sakurai` で指定できます。Windows では既存の同名フォルダがないことを確認してから、次の PowerShell の例を使えます。

```powershell
git clone https://github.com/ISOCASSELGenMi/sakurai-skill-contextual.git
$skillBase = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $env:USERPROFILE '.codex/skills' }
$skillTarget = Join-Path $skillBase 'sakurai'
if (Test-Path -LiteralPath $skillTarget) { throw '既存の sakurai をバックアップしてから実行してください。' }
New-Item -ItemType Directory -Path $skillBase -Force | Out-Null
Copy-Item -LiteralPath './sakurai-skill-contextual/skills/sakurai' -Destination $skillTarget -Recurse
```

Claude Code では「桜井さんならどうする？」「このゲームの手応えをレビューして」などと頼むと読み込まれます。

## 上流版の作例：ハジキ

<img src="examples/hajiki/hajiki_icon.gif" width="160" align="right">

上流版のスキルを読み込んだ AI エージェントが、企画から磨き込み・タイトル・アイコンまで作った Godot 4.6 の一画面アクションです。敵の弾を引きつけるほど強く打ち返せます。

- [unityroom で遊ぶ](https://unityroom.com/games/hajiki)
- [このゲームでスキルのどこを参照したか（動画番号つき）](examples/hajiki/README.md)

<br clear="right">

## 中身

```
skills/sakurai/
  SKILL.md            状況確認・資料選択・適用判断・衝突比較の手順
  decisions/          状況・判断・適用外・出典を記録する決定カード
  evaluation/         条件を変えた動作確認ケース
  references/         動画ごとの要点をカテゴリ別に並べたもの（必要なときだけ読む）
    gameplay.md  planning.md  concepts.md  specs.md  motion.md  effects.md  graphics.md
    ui.md  sound.md  tech.md  team.md  mindset.md  pr.md  misc.md
tools/
  to_text.py          字幕（srv1）を時刻なしの本文にする
  build_refs.py       要点メモをカテゴリ別の references/ に並べ替える
```

- `SKILL.md` は約3千文字。必要なカードと、その根拠となる `references/` の見出しを読みます。
- 各要点には動画の通し番号（古い順の 001〜259）とタイトルを付けているので、元の動画をたどれます。

## 上流版で紹介されている関連プロジェクト

以下の比較は上流 README の説明を引き継いだもので、比較表の「上流版」は kociden/sakurai-skill を指します。この fork の変更点は冒頭を参照してください。

同じチャンネルを元にしたスキルに [kokuren333/Sakurai-Skills](https://github.com/kokuren333/Sakurai-Skills) があります（上流リポジトリより先に公開されています）。目的は近いですが、作り方と向きが違います。

| | kokuren333/Sakurai-Skills | 上流版 |
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
