# エフェクト・画面反応・負荷

<a id="effect-impact-or-visibility"></a>
## effect-impact-or-visibility：迫力を増やすか、行動対象を見えるようにするか

- 問題：迫力を増やすか、行動対象を見えるようにするか。
- 適用状況：ヒットマーク、爆発、剣の軌跡が弱い、またはキャラを隠す場面。
- 出典要約：明暗の対比、キャラを遮らない形、爆発の段階、マークの位置・残る長さ、武器に合う風切りと大きさ感を扱う。
  - 出典：[effects.md](../references/effects.md) の 016「モヤっとさせるな」、[effects.md](../references/effects.md) の 035「キャラクターを際立たせる」、[effects.md](../references/effects.md) の 056「閃光､爆発､残煙」、[effects.md](../references/effects.md) の 079「エフェクトをスローで見てみよう」、[effects.md](../references/effects.md) の 130「ヒットマーク」、[effects.md](../references/effects.md) の 177「風切り」、[effects.md](../references/effects.md) の 199「効果は正しい大きさ感で」。
- 判断案（編集上の解釈）：何が起きたか伝える時点を決め、明暗両方の背景と実速度で認識を確認する。拡大や長時間化以外の形・位置・色も比較する。
- 適用外・導けないこと：加算や長い残煙を常に禁止しない。鑑賞用のスローだけで、実プレイ中の視認性を判断しない。
- 関連・対立：[detail-or-readability](ui-visual.md#detail-or-readability)、[impact-and-tempo](player-experience.md#impact-and-tempo)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。

<a id="shake-or-comfort"></a>
## shake-or-comfort：振動やフラッシュを足すか、負担を減らすか

- 問題：振動やフラッシュを足すか、負担を減らすか。
- 適用状況：大きな衝撃、画角や距離の変化、画面酔い、HUD まで揺れる実装。
- 出典要約：振動方式ごとの欠点、距離での補正、フラッシュのコントラスト、酔い対策、ブラーの強度設定を扱う。
  - 出典：[effects.md](../references/effects.md) の 103「画面振動」、[effects.md](../references/effects.md) の 221「フラッシング」、[planning.md](../references/planning.md) の 128「3Dゲームで酔う場合」、[ui.md](../references/ui.md) の 055「いまどきの親切設計」、[graphics.md](../references/graphics.md) の 190「モーションブラー」。
- 判断案（編集上の解釈）：ショックの認識と視界の安定を別に確認する。振動対象、強度、収束、設定、代替の音やポーズを比較する。
- 適用外・導けないこと：全員が快適な固定値や安全な点滅条件を、この要約から確定しない。手応えのために必ず画面全体を揺らすとは限らない。
- 関連・対立：[camera-or-navigation](controls.md#camera-or-navigation)、[effect-impact-or-visibility](effects-decisions.md#effect-impact-or-visibility)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。

<a id="particles-or-authored-shape"></a>
## particles-or-authored-shape：粒子を増やすか、形と配置を作り込むか

- 問題：粒子を増やすか、形と配置を作り込むか。
- 適用状況：重なった半透明描画、可動カメラで板が見える表現、見える効果に比べ負荷が高い場面。
- 出典要約：ビルボードの向きの制約、寿命・同時数・重なりの抑制、手置きの例、見える所へのリソース集中を扱う。
  - 出典：[effects.md](../references/effects.md) の 151「ビルボード」、[effects.md](../references/effects.md) の 242「パーティクルの限界」、[graphics.md](../references/graphics.md) の 044「大事と小事を見分ける」。
- 判断案（編集上の解釈）：負荷の高い場面を測り、粒子数、寿命、画像内の情報量、配置を比較する。可動カメラの範囲も確認する。
- 適用外・導けないこと：全てを板にする、全てを手置きする、と固定しない。特定ハードの容量感を現在の性能上限にしない。
- 関連・対立：[frame-rate-or-simulation](controls.md#frame-rate-or-simulation)、[scope-or-quality](production.md#scope-or-quality)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。
