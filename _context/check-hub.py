#!/usr/bin/env python3
"""자료실 점검: 저장소 맨 위에서 `python3 -I _context/check-hub.py`

1. 인쇄본의 가이드 이름마다 제목(# 줄)이 같은 가이드 파일이 정확히 하나인가
2. README · 사전 안내 · 가이드 · 도움말의 상대 링크가 모두 있는 파일을 가리키는가
3. 금지어가 저장소 어디에도 없는가 (.git 제외)
4. 워크시트 원본과 지시문 킷이 상위 프로젝트 원본과 같은가

상위 프로젝트(../docs/4-2)가 옆에 있으면 원고에서 가이드 이름을 뽑아 대조하고,
없으면 _context/guides.json의 이름으로 대조합니다. 하나라도 어긋나면 끝 상태가 1입니다.
"""
import filecmp, glob, json, os, re, sys

HUB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UP = os.path.join(os.path.dirname(HUB), 'docs', '4-2')
MS = os.path.join(UP, 'manuscript')
LEGEND = '가이드 이름'  # 00-front 표시 범례의 예시
BANNED = ['학' + '습자', '강사 ' + '가이드', 'SaaS' + '형']  # 이 파일 자체에 걸리지 않게 나눠 씀
fail = 0


def say(ok, msg):
    global fail
    print(('OK   ' if ok else 'FAIL ') + msg)
    if not ok:
        fail += 1


# 1. 가이드 이름 ↔ 가이드 파일 제목
registry = json.load(open(os.path.join(HUB, '_context', 'guides.json'), encoding='utf-8'))
if os.path.isdir(MS):
    printed = set()
    for f in glob.glob(os.path.join(MS, '*.md')):
        printed |= set(re.findall(r'→ 온라인 가이드: 「([^」]+)」', open(f, encoding='utf-8').read()))
    printed.discard(LEGEND)
    source = 'manuscript'
    say(printed == {g['title'] for g in registry}, f'guides.json 이름 {len(registry)}개 = 원고 이름 {len(printed)}개')
else:
    printed = {g['title'] for g in registry}
    source = 'guides.json'
h1 = {}
for f in sorted(glob.glob(os.path.join(HUB, 'guides', '*.md'))):
    first = open(f, encoding='utf-8').readline().rstrip('\n')
    if first.startswith('# '):
        h1.setdefault(first[2:], []).append(os.path.relpath(f, HUB))
for name in sorted(printed):
    files = h1.get(name, [])
    say(len(files) == 1, f'[{source}] 「{name}」 → {", ".join(files) or "없음"}')
extra = sorted(set(h1) - printed)
say(not extra, f'인쇄본에 없는 제목의 가이드 파일: {extra or "없음"}')
for g in registry:
    say(h1.get(g['title']) == [f'guides/{g["slug"]}.md'], f'guides.json slug {g["slug"]} ↔ 제목 일치')

# 2. 상대 링크
pages = ['README.md', 'pre-course-notice.md', 'worksheet-template/README.md', 'guides/images/README.md']
pages += [os.path.relpath(f, HUB) for f in sorted(glob.glob(os.path.join(HUB, 'guides', '*.md')) + glob.glob(os.path.join(HUB, 'help', '*.md')))]
n_links = 0
for p in pages:
    text = open(os.path.join(HUB, p), encoding='utf-8').read()
    text = re.sub(r'```.*?```', '', text, flags=re.S)       # 코드 상자
    text = re.sub(r'`[^`\n]*`', '', text)                   # 코드 조각
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)      # 작성자용 주석
    defs = dict(re.findall(r'^\[([^\]]+)\]:\s*(\S+)', text, flags=re.M))
    targets = re.findall(r'\]\(([^)\s]+)\)', text) + list(defs.values())
    refs = set(re.findall(r'\]\[([^\]]+)\]', text))
    if refs:
        missing = sorted(refs - set(defs))
        say(not missing, f'{p}: 참조 링크 {len(refs)}종 정의 확인' + (f' — 정의 없음 {missing}' if missing else ''))
    for t in targets:
        if re.match(r'(https?:|mailto:|#)', t):
            continue
        n_links += 1
        path = os.path.normpath(os.path.join(HUB, os.path.dirname(p), t.split('#')[0]))
        if not os.path.exists(path):
            say(False, f'{p}: 끊긴 링크 {t}')
say(True, f'상대 링크 {n_links}개 확인 (끊긴 링크는 위에 FAIL로 표시)')

# 3. 금지어
hits = []
for root, dirs, files in os.walk(HUB):
    dirs[:] = [d for d in dirs if d != '.git']
    for fn in files:
        fp = os.path.join(root, fn)
        try:
            for i, line in enumerate(open(fp, encoding='utf-8'), 1):
                if any(b in line for b in BANNED):
                    hits.append(f'{os.path.relpath(fp, HUB)}:{i}')
        except UnicodeDecodeError:
            pass
say(not hits, f'금지어 {len(BANNED)}개: {", ".join(hits) or "0건"}')

# 4. 사본 = 원본
if os.path.isdir(UP):
    for hub_path, up_path in [('worksheet-template/worksheet.md', 'worksheet/worksheet.md'),
                              ('kits/claude-code-research-prompts.md', 'kits/claude-code-research-prompts.md')]:
        say(filecmp.cmp(os.path.join(HUB, hub_path), os.path.join(UP, up_path), shallow=False),
            f'{hub_path} = 상위 프로젝트 docs/4-2/{up_path}')

print('\n결과:', '통과' if not fail else f'{fail}건 어긋남')
sys.exit(1 if fail else 0)
