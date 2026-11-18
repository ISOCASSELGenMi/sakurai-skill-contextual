# 音の役割・音楽・発注

<a id="sound-priority-or-density"></a>
## sound-priority-or-density：全ての音を鳴らすか、重要な音を通すか

- 問題：全ての音を鳴らすか、重要な音を通すか。
- 適用状況：戦闘 SE、ボイス、環境音、音楽が競合する場面と、静かな探索。
- 出典要約：勝敗や行動への影響で SE の重要度を決め、声の長さ・頻度・重なりと環境音の存在感を調整する。少ない音源での配分例もある。
  - 出典：[sound.md](../references/sound.md) の 032「重要度で効果音バランスを取る」、[sound.md](../references/sound.md) の 069「環境音楽としてのゲーム音楽」、[sound.md](../references/sound.md) の 107「音声収録」、[sound.md](../references/sound.md) の 202「環境音のバランス」、[sound.md](../references/sound.md) の 237「ファミコンの音源」、[sound.md](../references/sound.md) の 255「名作に音が悪いものなし」。
- 判断案（編集上の解釈）：その場で聞くべき情報を定め、同時再生の状況で聞き分けられるかを確認する。静かな場面では環境を感じる音の役割も見る。
- 適用外・導けないこと：スマブラの音量順位を全ジャンルの固定順序にしない。環境音の優先度が低いことを常に無音にする指示としない。
- 関連・対立：[sound-realism-or-impact](sound-decisions.md#sound-realism-or-impact)、[music-tempo-or-identity](sound-decisions.md#music-tempo-or-identity)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。

<a id="sound-realism-or-impact"></a>
## sound-realism-or-impact：実音に寄せるか、誇張して手応えを出すか

- 問題：実音に寄せるか、誇張して手応えを出すか。
- 適用状況：打撃・材質・操作の音。映像の写実度と、連続して鳴る頻度を確認する。
- 出典要約：映像とジャンルに合う誇張、材質の情報、多人数のヒット音での強い出だしと短い残響、複数再生環境での確認を扱う。
  - 出典：[sound.md](../references/sound.md) の 089「音はフィクション、ノンフィクション」、[sound.md](../references/sound.md) の 165「アタック強め、残響ほどほど」、[sound.md](../references/sound.md) の 054「いろんな環境で聞き比べ」。
- 判断案（編集上の解釈）：何を伝える音かを定め、単音だけでなく連続時・小型スピーカー等で比較する。
- 適用外・導けないこと：全効果音の残響を短くしない。写実的な映像だから実録音だけが正しいとも言えない。
- 関連・対立：[impact-and-tempo](player-experience.md#impact-and-tempo)、[sound-priority-or-density](sound-decisions.md#sound-priority-or-density)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。

<a id="music-tempo-or-identity"></a>
## music-tempo-or-identity：場面に合わせて変えるか、原曲の同一性を守るか

- 問題：場面に合わせて変えるか、原曲の同一性を守るか。
- 適用状況：新曲のテンポ、主題の反復、既存曲のアレンジ、言語別の曲構成。
- 出典要約：操作と場面に合うテンポ、覚えられる主題、アレンジの構成条件、原曲として記憶された主旋律の尊重を扱う。
  - 出典：[sound.md](../references/sound.md) の 025「ゲームに合ったテンポ感」、[sound.md](../references/sound.md) の 069「環境音楽としてのゲーム音楽」、[sound.md](../references/sound.md) の 126「アレンジの手法」、[sound.md](../references/sound.md) の 144「原曲がすべて正しい」。
- 判断案（編集上の解釈）：新作の曲と原曲のアレンジを区別し、変更できる構成と残すフレーズを発注時に明確にする。
- 適用外・導けないこと：対戦曲の BPM 範囲を全作品へ固定しない。「原曲が正しい」を新曲の作曲や全ての二次的解釈の禁止に拡大しない。
- 関連・対立：[sound-reference-or-fixation](sound-decisions.md#sound-reference-or-fixation)、[coherent-art-style](art-decisions.md#coherent-art-style)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。

<a id="sound-reference-or-fixation"></a>
## sound-reference-or-fixation：参考音を示すか、目的だけを伝えるか

- 問題：参考音を示すか、目的だけを伝えるか。
- 適用状況：音を発注・修正するとき、擬音や参考曲だけでは意図が共有できない場合。
- 出典要約：具体表現、共通の比喩、参考動画を手がかりにし、欲しい要素を明示する。監修は頭の中の音との一致より目的への適合で判断する。
  - 出典：[sound.md](../references/sound.md) の 183「効果音の指示」、[sound.md](../references/sound.md) の 220「他の曲を例に挙げる場合」、[sound.md](../references/sound.md) の 054「いろんな環境で聞き比べ」。
- 判断案（編集上の解釈）：参考から欲しいのが質感、雰囲気、立上り、構成のどれかを示し、実ゲームと対象の再生環境で確認する。
- 適用外・導けないこと：参考作品の模写や音源の流用を自動的に許可したことにしない。擬音だけで唯一の完成音が定まると考えない。
- 関連・対立：[visual-direction-or-rework](art-decisions.md#visual-direction-or-rework)、[music-tempo-or-identity](sound-decisions.md#music-tempo-or-identity)。
- 根拠の状態：AI 要約のみ・原動画未照合。条件の整理と比較手順は編集上の解釈。
