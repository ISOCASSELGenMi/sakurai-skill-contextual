# 操作・カメラ・時間

<a id="jump-or-commitment"></a>
## jump-or-commitment：空中で調整させるか、踏切の判断を重くするか

- 問題：空中で調整させるか、踏切の判断を重くするか。
- 適用状況：ジャンプ、着地、崖際の動作。初心者向け操作と位置取りのリスクを区別する。
- 出典要約：ジャンプの高さ・落下・空中制御はゲーム目的で変える。崖から落とすかも動作ごとに決め、慣性等で手触りが変わる。
  - 出典：[specs.md](../references/specs.md) の 037「ジャンプのしくみ」、[specs.md](../references/specs.md) の 102「ガケぎわのふるまい」、[specs.md](../references/specs.md) の 019「物理ボタンに重たさを感じさせる」。
- 判断案（編集上の解釈）：踏切、飛行中、着地、攻撃中の崖際を別々に試し、狙った位置へ行けるか、意図した危険かを確認する。
- 適用外・導けないこと：一つの名作の軌道や落下補正を万能としない。全行動で落下禁止にすると壊れる駆け引きもある。
- 関連・対立：[risk-reward-proximity](systems.md#risk-reward-proximity)、[difficulty-or-assistance](onboarding-difficulty.md#difficulty-or-assistance)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。

<a id="camera-or-navigation"></a>
## camera-or-navigation：主人公を中央に置くか、必要な情報を映すか

- 問題：主人公を中央に置くか、必要な情報を映すか。
- 適用状況：ジャンプの高さ、進行方向、協力プレイ、マップ注視、画面内の標的認識。
- 出典要約：注視点の単純追従を避け、進行方向や高さの認識を助ける。地図だけを見続けない誘導や、主役を追う協力プレイの例がある。
  - 出典：[specs.md](../references/specs.md) の 061「注視点をくっつけない」、[specs.md](../references/specs.md) の 118「マップもゲーム画面」、[planning.md](../references/planning.md) の 042「世界の窓はとっても狭い」、[concepts.md](../references/concepts.md) の 020「星のカービィ スーパーデラックス」。
- 判断案（編集上の解釈）：誰の何の判断に必要な視界かを定め、追従、先読み、画面内の目印、マップを比較する。
- 適用外・導けないこと：全ゲームに同じ追従の弱さを指定しない。協力プレイの主従関係をユーザーの方針なしに決めない。
- 関連・対立：[detail-or-readability](ui-visual.md#detail-or-readability)、[shake-or-comfort](effects-decisions.md#shake-or-comfort)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。

<a id="standard-or-custom-input"></a>
## standard-or-custom-input：標準操作を使うか、独自入力を作るか

- 問題：標準操作を使うか、独自入力を作るか。
- 適用状況：ボタン数、はじき入力、コマンド入力、キー設定、入力デバイスの違い。
- 出典要約：馴染みの操作は説明を減らし、独自入力は手触りや駆け引きを作る。暴発、反応、割当変更、アナログとデジタルの違いも扱う。
  - 出典：[planning.md](../references/planning.md) の 051「ワンボタンでできること」、[planning.md](../references/planning.md) の 104「ノーリアクションを排除せよ」、[specs.md](../references/specs.md) の 152「はじき入力」、[gameplay.md](../references/gameplay.md) の 157「昇龍拳コマンド」、[planning.md](../references/planning.md) の 173「知っていることは話が早い」、[ui.md](../references/ui.md) の 195「ボタン設定」、[ui.md](../references/ui.md) の 167「高速に選びたい」。
- 判断案（編集上の解釈）：使える操作と学習負担を確認し、必須の入力と任意の熟練入力を分ける。設定変更後も表示と実動作が合うか試す。
- 適用外・導けないこと：全ボタンや新機器を使い切ることを目標にしない。入力方式が異なる操作を、名前だけ同じにして置換できるとは限らない。
- 関連・対立：[tutorial-or-practice](onboarding-difficulty.md#tutorial-or-practice)、[asymmetry-or-balance](systems.md#asymmetry-or-balance)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。

<a id="frame-rate-or-simulation"></a>
## frame-rate-or-simulation：描画を軽くするか、時間と反応の設計を見直すか

- 問題：描画を軽くするか、時間と反応の設計を見直すか。
- 適用状況：フレーム落ち、移植後の難化、開発機と製品機の差、展示環境の遅延。
- 出典要約：フレーム・距離・時間の基準、体感での指定、処理速度の変化による難易度の変化、表示機器の遅延を扱う。
  - 出典：[planning.md](../references/planning.md) の 005「フレームはコマ数」、[planning.md](../references/planning.md) の 076「フレームを計れるようになれ！」、[specs.md](../references/specs.md) の 084「速度の単位」、[specs.md](../references/specs.md) の 139「想定外の完成形」、[misc.md](../references/misc.md) の 008「遅延を撲滅してほしい」。
- 判断案（編集上の解釈）：入力、処理、描画、表示のどこが遅いかを分け、時間基準と対象実機での挙動を確認する。
- 適用外・導けないこと：過去の機器の設定を現在の全機器へ適用しない。60fps 前提の数値を別レートへ換算せず転用しない。
- 関連・対立：[impact-and-tempo](player-experience.md#impact-and-tempo)、[scope-or-quality](production.md#scope-or-quality)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。
