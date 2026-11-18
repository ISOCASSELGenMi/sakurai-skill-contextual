# 制作指示・物語整合・待ち時間・説明

<a id="animation-spec-or-freedom"></a>
## animation-spec-or-freedom：動きを細かく指定するか、担当者の工夫に任せるか

- 問題：動きを細かく指定するか、担当者の工夫に任せるか。
- 適用状況：モーションの発注、既存リグの限界、指の表現や専用動作の費用対効果。
- 出典要約：動作リストや重要ポーズ・時間を共有し、模型とモデルの違いには担当者の工夫を残す。指や多関節の表現は負荷と効果を比較する。
  - 出典：[motion.md](../references/motion.md) の 014「モーション指定の仕方」、[motion.md](../references/motion.md) の 208「指の表現」、[motion.md](../references/motion.md) の 234「スケルトンの限界」。
- 判断案（編集上の解釈）：必要な見え方とゲーム上の時点を指定し、実現方法の裁量を残す。専用リグを増やす前に、画面上で効果が分かるかを試す。
- 適用外・導けないこと：参考ポーズを全関節の完全再現の義務にしない。既存リグで無理だから表現不能とも、誇張のためなら無制限に拡張すべきとも言えない。
- 関連・対立：[pose-or-anatomy](motion-decisions.md#pose-or-anatomy)、[visual-direction-or-rework](art-decisions.md#visual-direction-or-rework)、[scope-or-quality](production.md#scope-or-quality)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。

<a id="scenario-or-play-consistency"></a>
## scenario-or-play-consistency：物語の展開を守るか、プレイ結果との整合を取るか

- 問題：物語の展開を守るか、プレイ結果との整合を取るか。
- 適用状況：勝利後の強制敗北、仲間の離脱、主人公視点、ゲームの仕掛けとシナリオの接続。
- 出典要約：勝ったのに話の都合で負ける不満、離脱時の育成や装備の扱い、ゲームと物語を一体で用意することを扱う。セオリーを破る表現の可能性もある。
  - 出典：[planning.md](../references/planning.md) の 113「ゲームのシナリオは特異」、[planning.md](../references/planning.md) の 231「ゲーム内ムービー」。
- 判断案（編集上の解釈）：プレイヤーが何を達成したと感じるかを先に確認し、演出意図、事前の期待、結果の引継ぎを比較する。
- 適用外・導けないこと：全ての悲劇や強制展開を禁止しない。意外性を理由に、プレイの労力が無意味になる負担を無検証で受け入れさせない。
- 関連・対立：[story-or-control](onboarding-difficulty.md#story-or-control)、[progression-rewards](player-experience.md#progression-rewards)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。

<a id="loading-or-feedback"></a>
## loading-or-feedback：待ちを演出で埋めるか、状態を簡潔に知らせるか

- 問題：待ちを演出で埋めるか、状態を簡潔に知らせるか。
- 適用状況：読み込みの必要時間、短縮後にも残る演出、画面遷移時の戸惑い。
- 出典要約：必要な読み込みと演出が合う例を示す一方、素直な読み込み表示、最適化で変わる所要時間、素早さと認識の両立を求める。
  - 出典：[ui.md](../references/ui.md) の 078「ローディング画面」、[specs.md](../references/specs.md) の 073「遅さは罪」、[specs.md](../references/specs.md) の 244「画面遷移は素早く」。
- 判断案（編集上の解釈）：本当に必要な待ちと演出都合の待ちを測り、状態の理解を保ちながら操作復帰を早める。
- 適用外・導けないこと：ロードが短くなっても演出尺を守るために待たせるとは限らない。演出ゼロを万能とせず、必要な状態の通知は残す。
- 関連・対立：[impact-and-tempo](player-experience.md#impact-and-tempo)、[retry-or-consequence](onboarding-difficulty.md#retry-or-consequence)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。

<a id="label-or-symbol"></a>
## label-or-symbol：文字で説明するか、絵と配置で伝えるか

- 問題：文字で説明するか、絵と配置で伝えるか。
- 適用状況：分かりにくい項目名、同語反復のヘルプ、色分け、言語が分からない人の入口。
- 出典要約：専門用語を噛み砕くヘルプ、モードごとの色、キャラ絵、重要度に応じた大きさ、言語に依存しすぎない導線を扱う。
  - 出典：[ui.md](../references/ui.md) の 227「メニューにヘルプを」、[ui.md](../references/ui.md) の 132「色による区分」、[ui.md](../references/ui.md) の 238「言語がなくてもわかるように」、[ui.md](../references/ui.md) の 145「大事なものをより大きく」。
- 判断案（編集上の解釈）：初見の人が次に何が起こるか説明できるかを確認し、名前、補足文、絵、配置を組み合わせる。
- 適用外・導けないこと：アイコンなら常に理解されると断定しない。色だけで必要な違いを伝えず、重要度が同じ選択肢に勝手な優劣を付けない。
- 関連・対立：[style-or-clarity](ui-visual.md#style-or-clarity)、[localization-or-layout](ui-visual.md#localization-or-layout)、[detail-or-readability](ui-visual.md#detail-or-readability)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。
