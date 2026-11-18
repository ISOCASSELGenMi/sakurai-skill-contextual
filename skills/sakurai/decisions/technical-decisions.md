# 調整と開発用ツール

<a id="tuning-or-hardcode"></a>
## tuning-or-hardcode：数値を外出しするか、実装に固定するか

- 問題：数値を外出しするか、実装に固定するか。
- 適用状況：プランナーが反復調整する値、実装の制御ロジック、仕様書で数値を指示する場面。
- 出典要約：調整値を外へ出し、素早い反映を可能にする。仕様書の名前と値の表現、速度の単位、技ごとの細かな制御値の例がある。
  - 出典：[tech.md](../references/tech.md) の 046「調整をしやすくする仕組み」、[misc.md](../references/misc.md) の 068「パラメーターを【】でくくる」、[specs.md](../references/specs.md) の 084「速度の単位」、[tech.md](../references/tech.md) の 143「『スマブラ』のふっとばし」。
- 判断案（編集上の解釈）：誰が何を何度変えるかを決め、名前、単位、意味、反映方法を揃える。依存値や低頻度の値は見通しを保つ。
- 適用外・導けないこと：全てのロジックを表にする根拠ではない。【日本語名】と○は出典の作業方式で、他言語チームへの必須規則ではない。
- 関連・対立：[asymmetry-or-balance](systems.md#asymmetry-or-balance)、[frame-rate-or-simulation](controls.md#frame-rate-or-simulation)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。

<a id="debug-tools-or-content"></a>
## debug-tools-or-content：遊びの要素を作るか、確認を速める道具を作るか

- 問題：遊びの要素を作るか、確認を速める道具を作るか。
- 適用状況：再現に時間がかかる、モデルに隠れた動作が見えない、状態を作るため数値を書き換えている場面。
- 出典要約：体力・画面停止・カメラ・キャラ切替・透過等の開発機能を整え、日々の確認を容易にする。スロー観察も動きの分析に役立つ。
  - 出典：[tech.md](../references/tech.md) の 193「デバッグモード」、[tech.md](../references/tech.md) の 215「透過機能」、[effects.md](../references/effects.md) の 079「エフェクトをスローで見てみよう」。
- 判断案（編集上の解釈）：確認したい状態と再現の手間を特定し、使用頻度が高い操作から整備する。製品で残す機能は別に判断する。
- 適用外・導けないこと：作ったデバッグ機能を全て公開するとは限らない。道具作り自体を目的に、確認すべき体験を後回しにしない。
- 関連・対立：[hitbox-or-image](motion-decisions.md#hitbox-or-image)、[exhaustive-or-targeted](production.md#exhaustive-or-targeted)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。

<a id="lock-or-merge"></a>
## lock-or-merge：共同編集を止めるか、差分を統合するか

- 問題：共同編集を止めるか、差分を統合するか。
- 適用状況：複数人が同じ素材や仕様を変更し、上書き・先祖返り・担当不明が発生する制作。
- 出典要約：整理できる名前、チケットの受渡し、ロックとマージの制約、バックアップ、テストする版の統一を扱う。
  - 出典：[tech.md](../references/tech.md) の 022「ファイル名は合理的に」、[tech.md](../references/tech.md) の 094「チケットでタスク管理」、[tech.md](../references/tech.md) の 170「多くの人がファイルをいじる方法」、[team.md](../references/team.md) の 206「デバッグの体制」。
- 判断案（編集上の解釈）：テキストと統合しにくい素材を分け、担当、対象版、変更履歴、復旧方法を決める。
- 適用外・導けないこと：全ファイルのロックを一律に勧めない。紹介されたツール運用を現行製品の仕様と取り違えず、使う道具の仕様を確認する。
- 関連・対立：[communication-or-focus](team-decisions.md#communication-or-focus)、[exhaustive-or-targeted](production.md#exhaustive-or-targeted)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。
