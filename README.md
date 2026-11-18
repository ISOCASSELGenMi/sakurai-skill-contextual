# sakurai-skill-contextual

桜井政博のゲーム制作動画を基にした、状況別の判断を支援する非公式・日本語の Agent Skill と Claude プラグインです。[kociden/sakurai-skill](https://github.com/kociden/sakurai-skill) の fork として、元の要約と開発履歴を引き継いでいます。桜井政博氏・有限会社ソラ・Anthropic の公式製品ではありません。

## この版の内容

[スキル本体](skills/sakurai/SKILL.md) は、問題の特定、資料の選択、適用判断、異なる助言の比較、実行できる提案を案内します。原則に違反したことだけで欠陥と決めません。

[20 枚の決定カード](skills/sakurai/decisions/) は以下を扱います。

- 原型 と PV、映像 の 冒頭、探索 と 正式提案、コンセプト と 仕様変更。
- 対戦 の ランダム性 と 逆転補正、成長報酬、手応え と テンポ。
- 初回導入 と 練習場、物語 と 操作、難易度 と 救済、失敗 と リトライ。
- UI の 世界観 と 分かりやすさ、多言語 と レイアウト、背景 と 視認性。
- 即決 と 調査、制作範囲 と 品質、総当たり と 重点検証。
- 体験版 と 本編、構想 の 集中 と 公開発信、駆け引き 以外 の 楽しさ。

カードには状況、判断案、適用外、出典、根拠の状態を記載。「出典要約」「編集上の解釈」「今回の提案」を分けます。カードのない話題もカテゴリ別資料から扱います。

## 根拠と限界

既存の 14 ファイル・257 件の要約は上流のままです。自動字幕を AI が要約した資料であり、原発言の逐語録ではありません。原動画との照合は未実施。番号はリポジトリ内の通し番号で、公式集数とは限りません。

[31 ケースの評価セット](skills/sakurai/evaluation/cases.md) を同梱しています。ケースの同梱や形式検証は、モデルの命中率向上を実測したことを意味しません。

## Claude Code のインストールと更新

この repo はプラグインと自分で管理する marketplace の両方を含みます。公式ディレクトリへ掲載・承認されたという意味ではありません。

```bash
claude plugin marketplace add ISOCASSELGenMi/sakurai-skill-contextual
claude plugin install sakurai-contextual@genmi-game-design --scope user
```

呼び出し例：

```text
/sakurai-contextual:sakurai 新規 IP の PV 冒頭をレビューして
```

更新も同じ fork から行います。この版は `0.2.0` です。

```bash
claude plugin marketplace update genmi-game-design
claude plugin update sakurai-contextual@genmi-game-design --scope user
```

`claude plugin marketplace list` で取得元が `ISOCASSELGenMi/sakurai-skill-contextual` であることを確認できます。上流は出典であり、この版の更新元ではありません。単独で `~/.claude/skills/sakurai` を配置した版がある場合は二重登録に注意してください。

## Claude のチャット・Cowork

「自訂 / Customize」→「外掛程式 / Plugins」→「新增 / Add」→「新增市集 / Add marketplace」でこの fork の URL を登録し、`sakurai-contextual` をインストールします。

個別スキルとして使う場合は `skills/sakurai/` をルートフォルダ `sakurai/` として ZIP にし、「Skills」→「新增 Skill」からアップロードします。市集版と個別版は同じ環境では片方を選んでください。個別アップロード版は ZIP を再アップロードして更新します。

## Codex

`skills/sakurai/` を Codex の skills ディレクトリ（標準は `~/.codex/skills/`）へ配置し、`$sakurai` を指定できます。既存の改版を更新する場合は、保存内容を確認して同じフォルダへ反映します。このファイル配置によるインストールは Git の remote を持たず、上流へ自動追従する設定ではありません。

## 構成と検証

```text
.claude-plugin/          plugin.json、marketplace.json、icon.png
skills/sakurai/
  SKILL.md              状況確認と資料選択の入口
  decisions/            20 枚の決定カードと追加形式
  evaluation/cases.md   条件を変えた 31 ケース
  references/           上流の動画別要約 14 ファイル
```

```bash
claude plugin validate . --strict
claude plugin validate .claude-plugin/plugin.json --strict
python tools/validate_contextual.py
```

新しいカードは [形式](skills/sakurai/decisions/FORMAT.md) に従い、出典を読み、明記された条件と解釈を分けます。主ファイルに入口を加え、条件を変えた評価ケースを追加します。

## 上流資料と権利

字幕の採録・要約は上流由来です。[原チャンネル](https://www.youtube.com/@sora_sakurai_jp) と [上流 README](https://github.com/kociden/sakurai-skill) を参照してください。ハジキの作例、画像、既存の字幕処理ツールは上流資料として保持しており、この改版の効果測定ではありません。

[LICENSE](LICENSE) に上流の明示的なライセンスを確認できていないことを記載しています。この fork は元の文章・画像等に新たな利用許諾を付与しません。公式ディレクトリへの登録には、形式以外に権利関係・審査等の確認が別途必要です。
