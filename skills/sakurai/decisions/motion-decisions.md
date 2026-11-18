# 動作とポーズ

<a id="instant-response-or-windup"></a>
## instant-response-or-windup：即時に反応させるか、予備動作を残すか

- 問題：即時に反応させるか、予備動作を残すか。
- 適用状況：攻撃が重い、入力を受け付けたか分からない、相手に回避の猶予がない場面。
- 出典要約：入力直後の大きな反応、溜めの役割、攻撃後の隙とキャンセル時点を分けて設計する。
  - 出典：[motion.md](../references/motion.md) の 036「攻撃モーションの内訳」、[motion.md](../references/motion.md) の 049「かまえは瞬時に極端に」、[motion.md](../references/motion.md) の 077「フォロースルーで印象が決まる」。
- 判断案（編集上の解釈）：入力受付の見た目と、攻撃判定の発生を別々に測る。溜めは応答を返したうえで残す候補とする。
- 適用外・導けないこと：即反応を全攻撃の即時発生と同一視しない。硬直やオンライン遅延を理由に入力の無反応を放置しない。
- 関連・対立：[impact-and-tempo](player-experience.md#impact-and-tempo)、[asymmetry-or-balance](systems.md#asymmetry-or-balance)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。

<a id="pose-or-anatomy"></a>
## pose-or-anatomy：正しい姿勢を守るか、画面で伝わるポーズを選ぶか

- 問題：正しい姿勢を守るか、画面で伝わるポーズを選ぶか。
- 適用状況：小さなキャラの攻撃・被弾・表情、左右で見え方が変わる動作。
- 出典要約：遠目のシルエット、ヒット時のポーズ、被弾の差、表情の誇張、顔を見せる反転を扱う。リアル系や左右非対称キャラには条件がある。
  - 出典：[motion.md](../references/motion.md) の 028「やり過ぎてちょうどよい」、[motion.md](../references/motion.md) の 062「攻撃ポーズ」、[motion.md](../references/motion.md) の 091「情報が減るからおおげさにふるまう」、[motion.md](../references/motion.md) の 106「ポージングのススメ」、[motion.md](../references/motion.md) の 140「ダメージモーション」、[motion.md](../references/motion.md) の 164「フェイシャル」、[motion.md](../references/motion.md) の 179「フリップモーション」、[graphics.md](../references/graphics.md) の 241「キャラを立てるデザイン」。
- 判断案（編集上の解釈）：実際のカメラ距離と左右両向きで、何をしたか・受けたかが分かるかを見る。誇張を比較し、原作らしさと整合する範囲を選ぶ。
- 適用外・導けないこと：対称、自然な姿勢、繊細な表情を全て禁止しない。反転で武器や文字の意味が壊れる場合は別の見せ方を選ぶ。
- 関連・対立：[coherent-art-style](art-decisions.md#coherent-art-style)、[hitbox-or-image](motion-decisions.md#hitbox-or-image)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。

<a id="blend-or-snap"></a>
## blend-or-snap：滑らかにつなぐか、瞬間の切れ味を残すか

- 問題：滑らかにつなぐか、瞬間の切れ味を残すか。
- 適用状況：補間で動きがぬるい場合と、動作切替が不自然に跳ぶ場合。
- 出典要約：自動補間でメリハリが薄れる点と、短いブレンドによる接続、潰し・伸ばし、二軸回転や重心のずれによる表現を扱う。
  - 出典：[motion.md](../references/motion.md) の 148「モーション補間のワナ」、[motion.md](../references/motion.md) の 192「モーションブレンド」、[motion.md](../references/motion.md) の 120「扁平スケーリング」、[motion.md](../references/motion.md) の 249「二軸で回転」、[specs.md](../references/specs.md) の 253「重心をズラすとどうなる？」。
- 判断案（編集上の解釈）：キーポーズと表示時間を決め、必要な接続だけを短く試す。回転・拡縮の味付けは判定や入力への影響と分ける。
- 適用外・導けないこと：全補間を消す、全遷移を滑らかにする、いずれも一律に適用しない。見た目の変形で判定も変えるとは限らない。
- 関連・対立：[instant-response-or-windup](motion-decisions.md#instant-response-or-windup)、[hitbox-or-image](motion-decisions.md#hitbox-or-image)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。

<a id="hitbox-or-image"></a>
## hitbox-or-image：見た目に判定を合わせるか、当てやすさを補うか

- 問題：見た目に判定を合わせるか、当てやすさを補うか。
- 適用状況：攻撃が当たって見えない、見た目は当たっているのに外れる、ポーズや軌道を修正する場面。
- 出典要約：判定を少し広く取ることと軌道の不一致を区別し、ヒットの時点・停止中の見た目・判定を動かさない振動を扱う。
  - 出典：[motion.md](../references/motion.md) の 223「攻撃判定を常に意識」、[specs.md](../references/specs.md) の 047「8つのヒットストップ仕様」、[graphics.md](../references/graphics.md) の 163「監修あれこれ」。
- 判断案（編集上の解釈）：実際の判定表示と通常画面を同じ時点で比べ、範囲、位置、発生、終了、見た目だけの変位を切り分ける。
- 適用外・導けないこと：広い判定を理由に説明不能な命中を正当化しない。実装する際は対象作品の公平性と見た目の期待を確認する。
- 関連・対立：[debug-tools-or-content](technical-decisions.md#debug-tools-or-content)、[pose-or-anatomy](motion-decisions.md#pose-or-anatomy)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。
