---
name: sakurai
description: 桜井政博のゲーム制作動画を基に、ゲームの企画・仕様・操作感・難易度・導入・演出・制作運営・広報の相談やレビューを、状況と出典を確認して行う。「桜井さんならどうする」「桜井流」という依頼にも使う。
---

# 桜井政博のゲーム制作：状況に応じた判断

非公式のファンメイド。桜井政博氏・有限会社ソラとは関係がない。
基礎資料は [kociden/sakurai-skill](https://github.com/kociden/sakurai-skill) が自動字幕から作成した AI 要約。既存の `references/*.md` はそのまま保存している。要約には聞き取りや解釈の誤りがあり得る。原動画を照合した資料ではない。

## 判断の進め方

1. **決める対象を特定する。** 今回の問題、開発段階、目指す体験、ジャンル・対象プレイヤー、人数・期限など、結論を左右する条件を既存の情報から拾う。結論が変わる情報だけを質問する。小さな相談に一律の質問票を課さない。情報不足でも進められる範囲は仮定を明示して扱う。
2. **該当する資料を読む。** 下表から必要な決定カードを選び、記載された出典の該当見出しを確認する。カードがない話題はカテゴリ別要約を直接読み、元の問題・条件・提案を切り分ける。カードの存在は必須条件ではない。全ファイルの一括読み込みは不要。
3. **適用を判断する。** 今回の条件と資料の条件がどう一致するかを示す。大作・アクション・特定作品の経験を、個人制作や別ジャンルへ広げる場合は、その広げ方を今回の提案として扱う。原則との不一致だけを欠陥とせず、観察された問題と狙う効果から改善を考える。
4. **異なる助言を比較する。** 相反しそうな資料は、問題、目的、工程、制約を比較する。条件の差が資料で確認できれば適用範囲を分ける。差が推測なら解釈と明記する。同じ条件で衝突が残る場合は両方を示し、保留または小さな検証を提案する。記載順・番号の新しさだけで優先せず、資料にない前提を作って整合させない。
5. **実行できる提案を出す。** 「今回の判断と理由 → 具体的な変更・試し方 → 根拠と限界」を依頼の大きさに合わせて簡潔に伝える。比較するなら何を観察して採否を決めるかも添える。

## 根拠の扱い

- **出典要約**：既存のカテゴリ別要約に書かれた内容。引用は「このリポジトリの通し番号 184『ゲーム画面を見せてくれ!』の要約では」のように表す。番号はリポジトリ内の古い順の通し番号で、公式の集数・カテゴリ番号とは限らない。
- **編集上の解釈**：複数の要約の関連づけ、適用範囲の推定、衝突の整理。出典の明言と区別する。
- **今回の提案**：ユーザーの目的・制約から組み立てた判断。桜井氏の発言として扱わない。

原発言の確認を求められたとき、または解釈の違いが結論を左右するときは原動画・字幕を確認する。未確認ならその旨を示し、直接引用、動画 URL、時間位置、公式番号を推測で補わない。確認済みとする場合は実際に確認した URL・該当箇所・範囲を記録する。回答言語はユーザーに合わせる。

## 決定カードへの入口

各カードの「出典要約」と「編集上の解釈」を分けて読む。例外が書かれていないことは、例外が存在しない証拠にはならない。

| 決めたいこと | 読むカード |
|---|---|
| 原型と PV のどちらに時間を使うか／PV の冒頭 | [開発と広報](decisions/development-pr.md)：`prototype-or-pv`、`show-gameplay` |
| 案を広げるか一案に絞るか／没案の記録 | [企画と変更](decisions/planning-change.md)：`explore-or-commit` |
| コンセプトを維持するか仕様を変更するか | [企画と変更](decisions/planning-change.md)：`concept-or-change` |
| 対戦のランダム性・逆転補正 | [体験と調整](decisions/player-experience.md)：`randomness-and-handicap` |
| 成長報酬と対戦の公平性 | [体験と調整](decisions/player-experience.md)：`progression-rewards` |
| 手応えを強めるか待ち時間を減らすか | [体験と調整](decisions/player-experience.md)：`impact-and-tempo` |
| 初回導入と任意の練習場 | [導入と難易度](decisions/onboarding-difficulty.md)：`tutorial-or-practice` |
| 物語と操作開始の配分 | [導入と難易度](decisions/onboarding-difficulty.md)：`story-or-control` |
| 難易度と救済／失敗とリトライ | [導入と難易度](decisions/onboarding-difficulty.md)：`difficulty-or-assistance`、`retry-or-consequence` |
| UI の世界観と分かりやすさ | [UI と視認性](decisions/ui-visual.md)：`style-or-clarity` |
| 翻訳と画面サイズ／背景と対象の区別 | [UI と視認性](decisions/ui-visual.md)：`localization-or-layout`、`detail-or-readability` |
| 即決と調査／要素の削減／検証の配分 | [制作運営](decisions/production.md)：`decide-or-investigate`、`scope-or-quality`、`exhaustive-or-targeted` |
| 体験版と本編／企画の集中と公開発信 | [体験版と発信](decisions/distribution.md)：`demo-or-main`、`private-idea-or-public-update` |
| 駆け引き以外の楽しさ | [ジャンルと目的](decisions/genre-purpose.md)：`risk-or-other-appeal` |

## カードがない話題の参照先

| ファイル | 探す内容 |
|---|---|
| [gameplay](references/gameplay.md) | リスクとリターン、ジャンル別のゲーム性、難易度・報酬・バランス |
| [planning](references/planning.md) | 導入、シナリオ、ご褒美、独自性、続編、CPU、カスタマイズ |
| [concepts](references/concepts.md) | 作品ごとの課題、解決策、開発条件、反省 |
| [specs](references/specs.md) | ヒットストップ、ジャンプ、カメラ、崖、時間・速度、画面遷移 |
| [motion](references/motion.md) | 入力からの反応、ポーズ、補間、誇張 |
| [effects](references/effects.md) | ヒットマーク、爆発、振動、フラッシュ、負荷 |
| [graphics](references/graphics.md) | 視認性、光、タッチ、スケール、最終出力 |
| [ui](references/ui.md) | レイアウト、文字、操作設定、ヘルプ、アクセシビリティ |
| [sound](references/sound.md) | 優先順位、ヒット音、BGM、音の指示 |
| [tech](references/tech.md) | パラメーター、即時反映、デバッグ、バージョン管理 |
| [team](references/team.md) | 意思決定、共有、工数、削減、デバッグ体制 |
| [mindset](references/mindset.md) | 企画書、選択肢、コンセプト、ディレクターの判断 |
| [pr](references/pr.md) | PV、製品像、体験版、発信、実演 |
| [misc](references/misc.md) | 遅延、ゲームの価値、チャンネル制作などの雑談 |

## カードを追加・修正するとき

[カード形式](decisions/FORMAT.md) を使い、出典の本文を読み、条件が明記か解釈かを分ける。関連・対立するカードをつなぎ、索引にも入口を加える。全動画を機械的にカード化するより、実際に誤用された判断を優先する。動作の確認には [検証ケース](evaluation/cases.md) を使う。通常の助言では評価用の判定基準を読む必要はない。
