# 美術・全体の見え方・監修

<a id="coherent-art-style"></a>
## coherent-art-style：素材を忠実に使うか、画面全体のタッチを揃えるか

- 問題：素材を忠実に使うか、画面全体のタッチを揃えるか。
- 適用状況：複数作者・異なる原作の素材、リアルとコミカルの混在、デフォルメの選択。
- 出典要約：共通のイメージボード、彩度・描き込み・等身等の統一と、原作らしさ・シルエット・漫画的な見え方を重視する。
  - 出典：[graphics.md](../references/graphics.md) の 129「タッチを合わせる」、[graphics.md](../references/graphics.md) の 136「アニメと実写が戦うような」、[graphics.md](../references/graphics.md) の 230「マンガ的表現」、[graphics.md](../references/graphics.md) の 241「キャラを立てるデザイン」、[gameplay.md](../references/gameplay.md) の 186「キャラゲームはらしさが第一」。
- 判断案（編集上の解釈）：保つ固有特徴と揃える表現ルールを決め、同じ照明・画面内で並べて評価する。
- 適用外・導けないこと：全キャラを同じ形にすることや原作の特徴の消去を統一と呼ばない。原作らしさの許容範囲を勝手に確定しない。
- 関連・対立：[pose-or-anatomy](motion-decisions.md#pose-or-anatomy)、[original-or-familiar](systems.md#original-or-familiar)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。

<a id="material-or-final-image"></a>
## material-or-final-image：モデルを直すか、素材・光・最終画面を直すか

- 問題：モデルを直すか、素材・光・最終画面を直すか。
- 適用状況：巨大物が模型に見える、最終出力で陰が潰れる、色が制作環境で変わる場面。
- 出典要約：反射する光、素材のスケール、俯瞰やぼかしの効果、環境ごとの色の差、最終画面全体の調整を扱う。少色表現にも材質の工夫がある。
  - 出典：[graphics.md](../references/graphics.md) の 010「素材を描かず、光を描く」、[graphics.md](../references/graphics.md) の 063「スケール感は正しく合わせる」、[graphics.md](../references/graphics.md) の 172「ミニチュア効果」、[graphics.md](../references/graphics.md) の 182「アナログな色合い統一」、[graphics.md](../references/graphics.md) の 203「無いものをあると感じさせる」、[graphics.md](../references/graphics.md) の 213「最終出力」、[graphics.md](../references/graphics.md) の 114「ドット絵の初歩的な話」。
- 判断案（編集上の解釈）：狙う大きさ感と対象画面を決め、形状以外に模様、彩度、光、視点、後処理を比較する。
- 適用外・導けないこと：高彩度や俯瞰を一律に禁止しない。意図的なミニチュア表現は別の目標として扱う。低解像度の技法を高解像度へ無条件で転用しない。
- 関連・対立：[detail-or-readability](ui-visual.md#detail-or-readability)、[coherent-art-style](art-decisions.md#coherent-art-style)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。

<a id="visual-direction-or-rework"></a>
## visual-direction-or-rework：言葉で監修するか、画像で方向を共有するか

- 問題：言葉で監修するか、画像で方向を共有するか。
- 適用状況：修正を繰り返しても方向が伝わらない、細部の修正が期限を圧迫する場面。
- 出典要約：レタッチや図による具体化、視点・パターン別の確認、実際に見える所への集中、品質を満たした段階で割り切る判断を挙げる。
  - 出典：[graphics.md](../references/graphics.md) の 090「レタッチ監修」、[graphics.md](../references/graphics.md) の 163「監修あれこれ」、[graphics.md](../references/graphics.md) の 222「カベ破壊ひとつに」、[graphics.md](../references/graphics.md) の 251「監修あれこれ：ソラ編」、[graphics.md](../references/graphics.md) の 044「大事と小事を見分ける」。
- 判断案（編集上の解釈）：狙う変化を一つの比較画像で示し、完成作業を担当者へ返す。優先度と採否の基準を決め、画面で改善したか確認する。
- 適用外・導けないこと：監修者の加工画像をそのまま製品品質としない。出典の修正量の比喩を常に倍の変更を要求する規則にしない。
- 関連・対立：[scope-or-quality](production.md#scope-or-quality)、[communication-or-focus](team-decisions.md#communication-or-focus)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。
