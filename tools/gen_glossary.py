#!/usr/bin/env python3
"""術語總表產生器

用途：從各譯稿的「章末術語對照表」彙整出兩份總表。
  1) TC_3-21.76/TC_3-21.76_全書術語總表_zh-TW.md ── 單一文件版
  2) 術語總表_zh-TW.md                            ── 跨文件版（TC + ATP）

原則：**章末術語表為主檔、總表為產生結果**。改譯名請先改章末表，再執行本程式。
用法：cd <repo 根目錄> && python3 tools/gen_glossary.py
"""
import glob, re, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

TC_MASTER = 'TC_3-21.76/TC_3-21.76_全書術語總表_zh-TW.md'
ALL_MASTER = '術語總表_zh-TW.md'


def tables_after(s, heading_re):
    m = re.search(heading_re, s, re.M)
    if not m:
        return []
    rows = []
    for tm in re.finditer(r'^\|(.+)\|\n\|[-| :]+\|\n((?:\|.*\n)+)', s[m.end():], re.M):
        head = [c.strip() for c in tm.group(1).split('|')]
        if not any(h.startswith(('原文', '英文')) for h in head):
            continue
        for l in tm.group(2).strip().split('\n'):
            cells = [c.strip() for c in l.strip().strip('|').split('|')]
            if len(cells) >= 2:
                rows.append(cells)
    return rows


def collect(include_atp):
    data = collections.OrderedDict()

    def add(en, zh, note, doc, ch):
        en, zh = en.strip(), zh.strip()
        if not en or not zh:
            return
        e = data.setdefault(en, {'zh': zh, 'note': note, 'src': [], 'alt': []})
        e['src'].append((doc, ch))
        if e['zh'] != zh:
            e['alt'].append((doc, ch, zh))
        if note and not e['note']:
            e['note'] = note

    for f in sorted(glob.glob('TC_3-21.76/*_zh-TW.md')):
        base = os.path.basename(f)
        if '術語總表' in base:          # 不吃自己的產出
            continue
        s = open(f, encoding='utf-8').read()
        m = re.search(r'_(Ch\d\d|AppA|AppB|詞彙表)_', base)
        tag = m.group(1)
        label = {'Ch00': '前言', 'AppA': '附A', 'AppB': '附B', '詞彙表': '詞彙表'}.get(
            tag) or 'Ch' + str(int(tag[2:]))
        if tag == '詞彙表':
            i = s.index('| 縮寫 | 英文全稱 | 中文 |')
            j = s.index('> **譯註**：原文詞彙表將 **SE**')
            for l in [x for x in s[i:j].split('\n')
                      if x.startswith('|') and not x.startswith('|---')][1:]:
                c = [x.strip() for x in l.strip().strip('|').split('|')]
                # 章末術語表已收錄的縮寫不重複列入，只補書末獨有者
                pat = re.compile(r'(^|[^A-Za-z0-9])' + re.escape(c[0]) + r'($|[^A-Za-z0-9])')
                if any(pat.search(k) for k in data):
                    continue
                add(f'{c[0]} ({c[1]})', c[2], '僅見於書末詞彙表', 'TC', '詞彙表')
            continue
        for r in tables_after(s, r'^## 附錄　本(章|篇)(新增)?術語對照表'):
            add(r[0], r[1], r[2] if len(r) > 2 else '', 'TC', label)

    if include_atp:
        for f in sorted(glob.glob('ATP_4-02.11/*_zh-TW.md')):
            s = open(f, encoding='utf-8').read()
            label = 'Ch' + str(int(re.search(r'_Ch(\d\d)_', os.path.basename(f)).group(1)))
            for r in tables_after(s, r'^## 附錄　本章(新增)?術語對照表'):
                add(r[0], r[1], r[2] if len(r) > 2 else '', 'ATP', label)
    return data


ORDER = {'前言': 0, '附A': 16, '附B': 17, '詞彙表': 18}


def chkey(c):
    if c in ORDER:
        return ORDER[c]
    m = re.match(r'Ch(\d+)', c)
    return int(m.group(1)) if m else 99


def sortkey(k):
    s = re.sub(r'^[^0-9A-Za-z]+', '', k)
    return (0 if s[:1].isalpha() else 1, s.lower())


def sections_of(data):
    sec = collections.OrderedDict()
    for k, v in sorted(data.items(), key=lambda kv: sortkey(kv[0])):
        head = k[:1].upper() if k[:1].isalpha() else '數字與符號'
        sec.setdefault(head, []).append((k, v))
    return sec


def srcs(v, cross):
    docs = collections.OrderedDict()
    for doc, ch in v['src']:
        docs.setdefault(doc, []).append(ch)
    out = []
    for doc in ['TC', 'ATP']:
        if doc in docs:
            chs = '、'.join(sorted(set(docs[doc]), key=chkey))
            out.append((doc + ' ' + chs) if cross else chs)
    return '｜'.join(out)


AMBIGUOUS = [
    ('TQ', 'TC Ch11', '戰術詢問（tactical questioning）', 'TC 詞彙表只收錄此義'),
    ('TQ', 'TC Ch15、ATP', '止血帶（tourniquet）', '兩份文件的醫療章節同此用法'),
    ('TQ', 'TC 附A', '戰術詢問員（tactical questioner）', '執行戰術詢問的人員'),
    ('cloverleaf', 'TC Ch07', '四葉草環繞法', '偵察技巧（使用者指定譯名）'),
    ('cloverleaf', 'TC Ch13', '苜蓿葉型交流道', '道路工程用語，與上者無關'),
    ('high carry／low carry', 'TC Ch11／Ch12', '高姿／低姿持槍／搬運', '前者為持槍姿勢，後者為小艇搬運'),
    ('slough／dead water', 'TC Ch12', '盲汊／靜水區', '前者為盲端支汊，後者為主河道上的無流段'),
    ('SE', 'TC Ch07、附A／詞彙表', '敏感地點蒐證／地點蒐證', '正文與原文詞彙表全稱不一致'),
    ('CLS／CMC', 'TC、ATP', '戰鬥救護員／醫務兵', 'CLS 階層低於 CMC（combat medic）'),
]

DIFFS = [
    ('CBRN', '化學、生物、**輻射**與核', '化學、生物、放射性與核', '使用者指定，TC 附錄 B 與詞彙表共 4 處已改'),
    ('space blanket', '**保暖毯**', '太空毯', '使用者指定，ATP Ch08 共 2 處已改'),
    ('acclimatization', '高度（環境）適應／熱適應', '—', '語境不同並存：TC Ch09 登山為高度適應、ATP Ch17 熱傷害為熱適應'),
    ('DD Form 1380', 'DD Form 1380（戰傷救護卡）', '戰術戰傷救護卡（TCCC 卡）', '同義，表單全稱寫法不同，不強制統一'),
    ('rescue breathing', '人工呼吸', '人工呼吸（人工換氣）', '同義，括號補充'),
    ('contusion', '挫傷', '挫傷（瘀青）', '同義，括號補充'),
]


def write(path, data, cross):
    L = []
    if cross:
        L += ['# 術語總表（跨文件）', '',
              '> **涵蓋文件**：',
              '> - **TC** — TC 3-21.76《遊騎兵手冊》（Ranger Handbook，2025 年 9 月版）',
              '> - **ATP** — ATP 4-02.11《戰術戰傷救護與急救》（2026 年 3 月版）',
              '>',
              f'> **條目數**：{len(data)} 條，由兩份譯稿的**章末術語對照表自動彙整**（TC 另含書末詞彙表）。',
              '> **排序**：依原文英文字母（縮寫依字首）。**出處**欄標示文件與章節。',
              '> **產生方式**：`python3 tools/gen_glossary.py`。章末術語表為主檔、本表為產生結果——改譯名請先改章末表再重新產生。',
              '> **單一文件檢視**：TC 3-21.76 另有 `TC_3-21.76/TC_3-21.76_全書術語總表_zh-TW.md`。', '',
              '---', '',
              '## 跨文件譯名差異（已處理）', '',
              '彙整時比對兩份文件的全部術語，共 6 組原文出現不同譯文，處理如下：', '',
              '| 原文 | 統一譯文 | 原本的另一譯法 | 處理 |', '|---|---|---|---|']
        L += [f'| {a} | {b} | {c} | {d} |' for a, b, c, d in DIFFS]
        L += ['', '---', '']
    else:
        L += ['# TC 3-21.76《遊騎兵手冊》全書術語總表', '',
              '> **來源**：TC 3-21.76《Ranger Handbook》，2025 年 9 月 19 日版，繁體中文譯稿',
              f'> **條目數**：{len(data)} 條，由前言、第 1～15 章、附錄 A／B 與書末詞彙表的**章末術語對照表自動彙整**。',
              '> **排序**：依原文英文字母（縮寫依字首）。**出處**欄為收錄該詞的章節。',
              '> **產生方式**：`python3 tools/gen_glossary.py`。章末術語表為主檔、本表為產生結果。',
              '> **跨文件對照**（含 ATP 4-02.11）：見 repo 根目錄 `術語總表_zh-TW.md`。', '',
              '---', '']
    L += ['## 一詞多義與易混淆', '', '| 原文 | 出處 | 譯文 | 說明 |', '|---|---|---|---|']
    L += [f'| {a} | {b} | {c} | {d} |' for a, b, c, d in AMBIGUOUS]
    L += ['', '---', '']
    for head, rows in sections_of(data).items():
        L += [f'## {head}', '', '| 原文 | 譯文 | 說明 | 出處 |', '|---|---|---|---|']
        for k, v in rows:
            L.append(f"| {k} | {v['zh']} | {v['note'].replace('|', '／')} | {srcs(v, cross)} |")
        L.append('')
    L += ['---', '']
    alt = sum(1 for v in data.values() if v['alt'])
    L.append(f"*自章末術語對照表彙整，共 {len(data)} 條；其中 {alt} 條在不同章節有不同譯文寫法（見上方說明）。*")
    open(path, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print(f'{path}: {len(data)} 條，差異 {alt} 組')


write(TC_MASTER, collect(include_atp=False), cross=False)
write(ALL_MASTER, collect(include_atp=True), cross=True)
