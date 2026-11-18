#!/usr/bin/env python3
"""参照の保存、カードの出典、索引とリンク、配布メタデータを確認する。"""
from pathlib import Path
import hashlib
import json
import re


def validate(root):
    skill = root / 'skills' / 'sakurai'
    errors = []
    main = (skill / 'SKILL.md').read_text(encoding='utf-8')
    headings = {}
    hashes = json.loads((root / 'tools' / 'upstream-references.sha256.json').read_text(encoding='utf-8'))
    refs = list((skill / 'references').glob('*.md'))
    if {p.name for p in refs} != set(hashes):
        errors.append('参照ファイルの構成が元版と異なります')
    for path in refs:
        # Git の autocrlf による改行差を除き、内容の変更を検出する。
        canonical = path.read_bytes().replace(b'\r\n', b'\n')
        if hashlib.sha256(canonical).hexdigest() != hashes.get(path.name):
            errors.append(f'元の参照資料が変わっています: {path.name}')
        for num, title in re.findall(r'^## (\d{3}) (.+)$', path.read_text(encoding='utf-8'), re.M):
            if num in headings:
                errors.append(f'参照番号の重複: {num}')
            headings[num] = title
    ids = []
    for path in (skill / 'decisions').glob('*.md'):
        if path.name == 'FORMAT.md':
            continue
        for card in re.split(r'(?=^## )', path.read_text(encoding='utf-8'), flags=re.M)[1:]:
            match = re.match(r'## ([a-z-]+)：', card)
            if not match:
                errors.append(f'カード ID の形式: {path.name}')
                continue
            cid = match[1]
            ids.append(cid)
            for field in ('問題', '適用状況', '出典要約', '判断案（編集上の解釈）', '適用外・導けないこと', '関連・対立', '根拠の状態'):
                if '- ' + field + '：' not in card:
                    errors.append(f'{cid}: {field} がありません')
            if '`' + cid + '`' not in main:
                errors.append(f'主ファイルに入口がありません: {cid}')
            for num, title in re.findall(r'(\d{3})「([^」]+)」', card):
                if not headings.get(num, '').startswith(title + '【'):
                    errors.append(f'出典の不一致: {num} {title}')
    if len(ids) != len(set(ids)):
        errors.append('カード ID が重複しています')
    links = 0
    for path in skill.rglob('*.md'):
        text = path.read_text(encoding='utf-8')
        if '\ufffd' in text:
            errors.append(f'文字コード: {path}')
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            if target.startswith(('https://', 'http://', '#')):
                continue
            links += 1
            if not (path.parent / target.split('#')[0]).is_file():
                errors.append(f'リンク切れ: {path.name}: {target}')
    plugin = json.loads((root / '.claude-plugin/plugin.json').read_text(encoding='utf-8'))
    market = json.loads((root / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
    if market['plugins'][0]['name'] != plugin['name'] or market['plugins'][0]['source'] != './':
        errors.append('市集とプラグインの参照が一致しません')
    cases = re.findall(r'^\| ([A-Z]\d+) \|', (skill / 'evaluation/cases.md').read_text(encoding='utf-8'), re.M)
    if len(cases) != len(set(cases)):
        errors.append('評価ケース ID が重複しています')
    result = {'参照ファイル': len(refs), '出典見出し': len(headings), '決定カード': len(ids), '評価ケース': len(cases), '相対リンク': links, 'バージョン': plugin['version'], 'エラー': errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return not errors


if __name__ == '__main__':
    raise SystemExit(0 if validate(Path(__file__).resolve().parents[1]) else 1)
