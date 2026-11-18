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
    index = (skill / 'decisions/INDEX.md').read_text(encoding='utf-8')
    headings = {}
    source_files = {}
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
            source_files[num] = path.name
    ids = []
    card_sources = {}
    card_files = {}
    for path in (skill / 'decisions').glob('*.md'):
        if path.name in ('FORMAT.md', 'INDEX.md', 'COVERAGE.md'):
            continue
        for card in re.split(r'(?=^## )', path.read_text(encoding='utf-8'), flags=re.M)[1:]:
            match = re.match(r'## ([a-z-]+)：', card)
            if not match:
                errors.append(f'カード ID の形式: {path.name}')
                continue
            cid = match[1]
            ids.append(cid)
            card_files[cid] = path.name
            card_sources[cid] = set(re.findall(r'(\d{3})「', card))
            for field in ('問題', '適用状況', '出典要約', '判断案（編集上の解釈）', '適用外・導けないこと', '関連・対立', '根拠の状態'):
                if '- ' + field + '：' not in card:
                    errors.append(f'{cid}: {field} がありません')
            if f'[{cid}]({path.name}#{cid})' not in index:
                errors.append(f'索引に入口がありません: {cid}')
            for num, title in re.findall(r'(\d{3})「([^」]+)」', card):
                if not (headings.get(num, '').startswith(title + '【') or headings.get(num) == title):
                    errors.append(f'出典の不一致: {num} {title}')
    if len(ids) != len(set(ids)):
        errors.append('カード ID が重複しています')
    if '(decisions/INDEX.md)' not in main:
        errors.append('主ファイルから索引へ到達できません')
    for filename in set(card_files.values()):
        if f'(decisions/{filename})' not in main:
            errors.append(f'主ファイルから分野へ到達できません: {filename}')
    coverage = json.loads((skill / 'decisions/coverage.json').read_text(encoding='utf-8'))
    numbers = [row['number'] for row in coverage]
    if len(numbers) != len(set(numbers)) or set(numbers) != set(headings):
        errors.append('出典の全件分類に重複または漏れがあります')
    direct = 0
    for row in coverage:
        num = row['number']
        if row['title'] != headings.get(num) or row['source'] != source_files.get(num):
            errors.append(f'分類表の出典が一致しません: {num}')
        actual = {cid for cid, sources in card_sources.items() if num in sources}
        if set(row['cards']) != actual:
            errors.append(f'分類表とカードの出典が一致しません: {num}')
        if actual:
            direct += 1
            if row['status'] != 'カード出典':
                errors.append(f'分類状態が一致しません: {num}')
        elif row['status'] != '背景資料' or not row['reason'].strip():
            errors.append(f'背景資料の保存理由がありません: {num}')
    rendered_numbers = re.findall(r'^\| (\d{3}) \|', (skill / 'decisions/COVERAGE.md').read_text(encoding='utf-8'), re.M)
    if rendered_numbers != numbers:
        errors.append('分類 JSON と Markdown の番号が一致しません')
    links = 0
    for path in skill.rglob('*.md'):
        text = path.read_text(encoding='utf-8')
        if '\ufffd' in text:
            errors.append(f'文字コード: {path}')
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            if target.startswith(('https://', 'http://', '#')):
                continue
            links += 1
            target_path = path.parent / target.split('#')[0]
            if not target_path.is_file():
                errors.append(f'リンク切れ: {path.name}: {target}')
            elif '#' in target:
                fragment = target.split('#', 1)[1]
                if f'<a id="{fragment}"></a>' not in target_path.read_text(encoding='utf-8'):
                    errors.append(f'アンカーがありません: {path.name}: {target}')
    plugin = json.loads((root / '.claude-plugin/plugin.json').read_text(encoding='utf-8'))
    market = json.loads((root / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
    if market['plugins'][0]['name'] != plugin['name'] or market['plugins'][0]['source'] != './':
        errors.append('マーケットプレイスとプラグインの参照が一致しません')
    cases = re.findall(r'^\| ([A-Z]\d+) \|', (skill / 'evaluation/cases.md').read_text(encoding='utf-8'), re.M)
    pairs = re.findall(r'^\| (P\d{3}) \|', (skill / 'evaluation/expanded-cases.md').read_text(encoding='utf-8'), re.M)
    all_cases = cases + pairs
    if len(all_cases) != len(set(all_cases)):
        errors.append('評価ケース ID が重複しています')
    test_coverage = json.loads((skill / 'evaluation/card-coverage.json').read_text(encoding='utf-8'))
    if set(test_coverage) != set(ids):
        errors.append('カードと評価対象が一致しません')
    for cid, case_ids in test_coverage.items():
        if not case_ids or not set(case_ids).issubset(all_cases):
            errors.append(f'評価ケースがありません: {cid}')
    result = {'参照ファイル': len(refs), '出典見出し': len(headings), 'カード出典': direct, '背景資料': len(headings)-direct, '決定カード': len(ids), '評価ケース': len(all_cases), '独立入力数': len(cases)+2*len(pairs), '相対リンク': links, 'バージョン': plugin['version'], 'エラー': errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return not errors


if __name__ == '__main__':
    raise SystemExit(0 if validate(Path(__file__).resolve().parents[1]) else 1)
