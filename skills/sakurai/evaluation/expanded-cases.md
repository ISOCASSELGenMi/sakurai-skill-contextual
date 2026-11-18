# 条件を対照する追加ケース

各行の A と B は別々の会話で実行する。判定基準は評価側だけで保持する。カードと元の要約を読み、条件によって判断を変えられるかを確かめる。表の用意は実行済みを意味しない。

| ID | カード | 入力 A | 入力 B | 判定基準 |
|---|---|---|---|---|---|
| P001 | [risk-reward-proximity](../decisions/systems.md#risk-reward-proximity) | 接近しても遠距離射撃より弱い武器を直したい。 | 癒やし系の散歩に被弾リスクを必ず入れるべき？ | A は危険と利得の関係を検討し、B はジャンルの狙いを先に確認する。 |
| P002 | [reward-feedback](../decisions/systems.md#reward-feedback) | 通貨は大量に出るが買いたい物がない。 | 報酬は機能するがクリアに気づけない。 | 用途の不足と達成認識の不足を切り分ける。 |
| P003 | [goal-and-pacing](../decisions/systems.md#goal-and-pacing) | 育つほど敵も同率で強くなり成長が分からない。 | 高難度の山場の後に安全な区間が欲しい。 | 成長の相対差と、山場後の緩急という別の問題を扱う。 |
| P004 | [asymmetry-or-balance](../decisions/systems.md#asymmetry-or-balance) | 全キャラの数値を同じにすると退屈になった。 | 一つの技に全状況で対処手段がない。 | A は差の回復を検討し、B は個性を残す言葉だけで放置しない。 |
| P005 | [ai-fairness](../decisions/systems.md#ai-fairness) | 初心者用 CPU が全攻撃を瞬時に防ぐ。 | 上級者の攻め練習用に防御特化の相手が欲しい。 | 通常の対戦相手と、目的を限定した練習相手を区別する。 |
| P006 | [customization-preview](../decisions/systems.md#customization-preview) | 大量の装備があるが違いを試す場所がない。 | 性能を変えず服だけ着せ替える作品を作りたい。 | A は比較と試用、B は外見の価値を中心に判断する。 |
| P007 | [guided-or-free-route](../decisions/systems.md#guided-or-free-route) | 初見の謎で何を目指すか分からない。 | 周回するボスなのに毎回同じ手順を強制される。 | 目的理解の補助と、反復中の攻略幅を区別する。 |
| P008 | [original-or-familiar](../decisions/systems.md#original-or-familiar) | プログラム学習で好きなゲームの操作を模作したい。 | 販売企画の説明が「有名作と同じ」だけになっている。 | 練習としての模作と、製品の差別化の責任を区別する。 |
| P009 | [sequel-or-new](../decisions/systems.md#sequel-or-new) | 前作の道具もチームも残っている続編を考えている。 | タイトルだけ続編でチームも技術も全て変わる。 | 引き継げる資産の実態を見て工数と魅力を比較する。 |
| P010 | [ranking-or-belonging](../decisions/systems.md#ranking-or-belonging) | 少人数地域で厳密な実力マッチングが成立しない。 | 観戦モードでどちらも応援する理由がない。 | 対戦成立の制約と観戦動機の不足を混同しない。 |
| P011 | [exploit-or-bug](../decisions/systems.md#exploit-or-bug) | ソロで安全に経験値を稼ぐ裏道が見つかった。 | 対戦で他人の操作を永久に止める手順が見つかった。 | 個人の攻略と他者の参加を壊す挙動を分ける。 |
| P012 | [jump-or-commitment](../decisions/controls.md#jump-or-commitment) | 初心者が攻撃の小さな踏み込みで崖から落ちる。 | 踏切位置を読むのが核のアクションを作る。 | 誤操作の補正と、意図した踏切の制約を区別する。 |
| P013 | [camera-or-navigation](../decisions/controls.md#camera-or-navigation) | ジャンプでカメラも同じだけ上がり、高さが分からない。 | 二人とも同格の協力ゲームで別方向へ移動したい。 | 高さの認識と複数主体の視界調停を分ける。 |
| P014 | [standard-or-custom-input](../decisions/controls.md#standard-or-custom-input) | はじきでダッシュが暴発し、歩けない人がいる。 | コマンド熟練にも意味を残したい。 | 入力の確実性と任意の習熟差を別々に調整する。 |
| P015 | [frame-rate-or-simulation](../decisions/controls.md#frame-rate-or-simulation) | 最適化後に敵の移動まで速くなった。 | 同じビルドでも展示用テレビだけ操作が遅い。 | シミュレーションの時間依存と表示機器の遅延を区別する。 |
| P016 | [instant-response-or-windup](../decisions/motion-decisions.md#instant-response-or-windup) | 押した後しばらく待機姿勢のままになる。 | 大技を見て回避する駆け引きは残したい。 | 反応開始と攻撃発生の時間を切り分ける。 |
| P017 | [pose-or-anatomy](../decisions/motion-decisions.md#pose-or-anatomy) | 遠くのキャラの被弾が待機と区別できない。 | 左右非対称の剣士を反転すると持ち手が変わる。 | 認識のための誇張と、反転が壊す固有情報を区別する。 |
| P018 | [blend-or-snap](../decisions/motion-decisions.md#blend-or-snap) | 同じキーポーズでも自動補間すると勢いがない。 | 攻撃から歩行への切替で身体が飛ぶ。 | ポーズ間の時間配分と接続の不連続を分ける。 |
| P019 | [hitbox-or-image](../decisions/motion-decisions.md#hitbox-or-image) | 剣の先が敵に触れるのに外れる。 | エフェクト終了後も見えない攻撃判定が残る。 | 空間的な範囲と時間的な終了の問題を区別する。 |
| P020 | [effect-impact-or-visibility](../decisions/effects-decisions.md#effect-impact-or-visibility) | 明るい場所ではヒットマークが消える。 | マークを強くしたら次の攻撃が見えなくなった。 | コントラスト不足と遮蔽・残存時間を分ける。 |
| P021 | [shake-or-comfort](../decisions/effects-decisions.md#shake-or-comfort) | 引きの画面では衝撃が伝わらない。 | 近距離で画面が激しく揺れ、遊びにくいと言われる。 | 距離による認識不足と負担増を同じ振幅で処理しない。 |
| P022 | [particles-or-authored-shape](../decisions/effects-decisions.md#particles-or-authored-shape) | 半透明の煙が重なると処理が落ちる。 | カメラを回すと炎が細い板に見える。 | 描画負荷と表現方式の視点制約を区別する。 |
| P023 | [coherent-art-style](../decisions/art-decisions.md#coherent-art-style) | 別作者のキャラを置くと照明も質感もばらばら。 | 表現を揃えたら原作らしい特徴が消えた。 | 画面の一貫性と固有の識別要素を別に評価する。 |
| P024 | [material-or-final-image](../decisions/art-decisions.md#material-or-final-image) | 巨大な城が小さなおもちゃに見える。 | ミニチュアの机上世界にしたい。 | 同じ視覚効果でも、意図する大きさが逆なら判断を変える。 |
| P025 | [visual-direction-or-rework](../decisions/art-decisions.md#visual-direction-or-rework) | 明るくと何度伝えても解釈がずれる。 | 見えない裏面の修正で発売が遅れそう。 | 伝達不足と優先順位の問題を区別する。 |
| P026 | [sound-priority-or-density](../decisions/sound-decisions.md#sound-priority-or-density) | 必殺技の声に埋もれて被弾音が聞こえない。 | 探索中に全て止まり無音になる。 | 情報競合を減らす判断と環境の存在感を足す判断を分ける。 |
| P027 | [sound-realism-or-impact](../decisions/sound-decisions.md#sound-realism-or-impact) | 連打時に長い残響が重なって打撃が消える。 | 広い洞窟を音の余韻で感じさせたい。 | 頻発する打撃の分離と、環境を伝える残響を区別する。 |
| P028 | [music-tempo-or-identity](../decisions/sound-decisions.md#music-tempo-or-identity) | 緊張した戦闘なのに BGM がゆったりしすぎる。 | 懐かしい原曲の主旋律まで変わってしまった。 | 場面への適合と原曲の識別を別の判断として扱う。 |
| P029 | [sound-reference-or-fixation](../decisions/sound-decisions.md#sound-reference-or-fixation) | この曲みたいにと頼んだら望まない楽器まで似た。 | 想定とは違う音だがゲームの反応が良くなった。 | 必要な要素の特定と、想定外でも目的に合う成果の評価を分ける。 |
| P030 | [tuning-or-hardcode](../decisions/technical-decisions.md#tuning-or-hardcode) | 攻撃力を変えるたびにコード修正と再起動が要る。 | 内部のアルゴリズムまで全て表に出すべき？ | 反復する調整値と制御手順を区別する。 |
| P031 | [debug-tools-or-content](../decisions/technical-decisions.md#debug-tools-or-content) | 特定の被弾を見るため毎回 20 分遊び直す。 | 便利な開発用無敵スイッチをそのまま製品へ残すべき？ | 開発中の確認効率と製品側の用途を分ける。 |
| P032 | [lock-or-merge](../decisions/technical-decisions.md#lock-or-merge) | 同じバイナリ素材を二人が変更し片方が消えた。 | 別行の文章修正でも全員をロック待ちにしている。 | 統合の難しい素材と、差分統合できる文書を区別する。 |
| P033 | [authority-or-vote](../decisions/team-decisions.md#authority-or-vote) | 好みの投票で毎回コンセプトが変わる。 | 画面の読みづらさを調べるため意見を集めたい。 | 最終方針の決定と情報収集を区別する。 |
| P034 | [communication-or-focus](../decisions/team-decisions.md#communication-or-focus) | 上流の判断が返らず全員の作業が止まる。 | 緊急でない通知で一日中集中できない。 | 依存作業を止める遅れと、まとめられる割込みを分ける。 |
| P035 | [playtest-evidence](../decisions/team-decisions.md#playtest-evidence) | 開発者は簡単だと言うが初見は操作で詰まる。 | 熟練者の対戦でだけ支配的な戦法が見つかった。 | 初見の学習問題と熟練者のバランス問題を区別する。 |
| P036 | [market-data-or-concept](../decisions/planning-practice.md#market-data-or-concept) | 誰も試していない操作の企画を既存市場データだけで決めたい。 | 既存ファン向けの続編について販売規模を説明したい。 | 新しい魅力の探索と事業説明の情報を区別する。 |
| P037 | [presentation-or-catalog](../decisions/planning-practice.md#presentation-or-catalog) | 初見向け発表で素材一覧だけを見せている。 | 詳細を確認する社内資料まで全て二行に削るべき？ | 魅力の入口と詳細な検討資料の役割を区別する。 |
| P038 | [start-or-prepare](../decisions/planning-practice.md#start-or-prepare) | 一人で操作を学びたいが計画だけ増えている。 | 試せていない方式で大量の素材制作を発注したい。 | 小さな学習の着手と、検証前の大量投資を区別する。 |
| P039 | [effort-or-sustainability](../decisions/planning-practice.md#effort-or-sustainability) | 定期投稿の凝りすぎで本制作が止まる。 | 短時間の修正でプレイヤーの見落としを大きく減らせる。 | 継続負担の削減と、効果が見える改善への投資を区別する。 |
| P040 | [standard-or-exception](../decisions/planning-practice.md#standard-or-exception) | 慣習で飛ばせないロゴを入れているが、本当に必須か不明。 | 現行の配布条件に明示された表示を省いてよい？ | 未確認の慣習を調べることと、確認済みの要件を破ることを分ける。 |
| P041 | [animation-spec-or-freedom](../decisions/edge-decisions.md#animation-spec-or-freedom) | 発注が「かっこよく」だけで判定時刻も決まっていない。 | 顔も指も見えない遠景キャラに専用の指リグが必要？ | 不足している制約の共有と、効果に見合わない詳細化を区別する。 |
| P042 | [scenario-or-play-consistency](../decisions/edge-decisions.md#scenario-or-play-consistency) | 完全勝利した直後のムービーで一方的に負け扱いになる。 | 意図的に喪失を描く場面で仲間を離脱させたい。 | 結果の矛盾による不満と意図的な喪失表現を分け、双方で引継ぎを確認する。 |
| P043 | [loading-or-feedback](../decisions/edge-decisions.md#loading-or-feedback) | ロードは終わっているがアニメの終了まで操作できない。 | 画面が一瞬で変わり、どこへ来たか分からない。 | 不要な待ちの除去と変化の認識を助ける表現を分ける。 |
| P044 | [label-or-symbol](../decisions/edge-decisions.md#label-or-symbol) | オプションの説明が「オプション画面へ進む」だけ。 | 全て同じ重要度の選択肢を一つだけ大きくすべき？ | 意味の説明不足と、根拠のない重要度付けを区別する。 |
| P045 | [concept-or-change](../decisions/planning-change.md#concept-or-change) | 体験の核は有効だが入力実装が不便だと分かった。 | 体験の核そのものが対象者に届かない可能性が出た。 | 手段の修正と核の再検証を区別し、185 と 029 を機械的な禁止にしない。 |
| P046 | [show-gameplay](../decisions/development-pr.md#show-gameplay) | 新規 IP の初公開 PV は長いロゴから始まる。 | 著名シリーズのティザーとして短い謎を見せたい。 | 新規作品と認知済み作品の条件を比較し、開発工程の先後へ読み替えない。 |
