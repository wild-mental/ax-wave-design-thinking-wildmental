# 작업 폴더와 워크시트 저장소 준비 가이드

교재: 1.1절 오늘의 지도 (11쪽) · 부록 A-1 작업 폴더와 비공개 저장소 (41~42쪽) · 쓰는 날: Day 1 오전, 그리고 하루를 마치기 전마다 · 쓰는 곳: GitHub 비공개 저장소 `design-thinking-worksheet`와 내 컴퓨터의 작업 폴더 `design-thinking-worksheet/`

> **준비 중인 가이드입니다.** 수업 전에 채워집니다. 그동안은 교재 1.1절 [실습 안내]와 부록 A-1을 보세요.

## 이 가이드에서 볼 것

이틀 동안의 결과물은 두 곳에 둡니다. 수업 중에는 내 컴퓨터의 **작업 폴더**에서 일하고, 하루를 마치기 전에 GitHub의 **비공개 저장소**에 올립니다. 이 가이드는 두 곳을 처음 한 번 만드는 순서와, 작업 폴더의 파일을 저장소에 올리는 순서를 다룹니다. Git 명령은 쓰지 않고 github.com 웹 화면에서만 작업합니다.

## 두 곳 한눈에

| | 작업 폴더 | 워크시트 저장소 |
|---|---|---|
| 어디에 | 내 컴퓨터 (바탕화면이나 문서 폴더) | github.com 내 계정 |
| 이름 | `design-thinking-worksheet/` | `design-thinking-worksheet` (**Private**) |
| 무엇을 | Claude Code가 이 폴더를 열고 파일을 만들고 고칩니다. `worksheet.md`도 여기서 채웁니다 | 하루를 마치기 전에 작업 폴더의 파일을 올려 두는 곳. 강사 `wild-mental`이 봅니다 |

작업 폴더 안의 모양입니다(교재 부록 A-1, 지시문 킷과 같음).

```text
design-thinking-worksheet/
├── worksheet.md                  ← 자료실의 워크시트 원본을 복사한 것
├── research/
│   ├── status-report.md          ← 현황 분석 리서치 (1.3)
│   ├── stakeholders.md           ← 이해관계자 분석 (1.3)
│   ├── market-tam-sam.md         ← TAM·SAM (1.6)
│   ├── causes-hypotheses.md      ← 핵심 원인과 가설 (1.7)
│   ├── segment-map.md            ← 세그먼트 맵 (2.2)
│   └── solution-som.md           ← 솔루션 정의와 SOM (2.3)
├── prototype/
│   └── concept-prototype.html    ← 개념 프로토타입 (2.4)
└── interviews/
    ├── persona-cards.md          ← 인터뷰 대상 페르소나 카드 (2.5)
    ├── interview-plan.md         ← JTBD 인터뷰 계획서 (2.5)
    ├── pair-interview-notes.md   ← 짝 롤플레잉 기록 (2.6, 직접 씀)
    ├── virtual-interviews.md     ← AI 가상 인터뷰 기록 (2.7)
    └── interview-report.md       ← 결과 보고서 · 요약 카드 · 고용·해고 여정 (2.7)
```

폴더와 파일 이름은 모두 영문 소문자로, 위와 똑같이 씁니다. 지시문 킷의 지시문이 이 이름으로 파일을 찾습니다.

## 1. 비공개 저장소 만들기 (처음 한 번)

1. github.com에 로그인하고 오른쪽 위 **+ → New repository**를 누릅니다.
2. Repository name에 `design-thinking-worksheet`를 쓰고, 공개 범위는 반드시 **Private**(비공개)를 고른 뒤 **Create repository**를 누릅니다.
3. 새 탭에서 [자료실의 `worksheet.md` 원본](https://github.com/wild-mental/ax-wave-design-thinking-wildmental/blob/main/worksheet-template/worksheet.md)을 엽니다. 파일 내용 위쪽 막대의 **Copy raw file**(복사 아이콘)을 눌러 내용 전체를 복사합니다.

> [캡처 예정] 공통: worksheet.md 원본 화면의 Raw · Copy raw file · Download raw file 아이콘 위치

4. 내 저장소 탭으로 돌아와 **Add file → Create new file**을 누릅니다(빈 저장소라면 안내 문구의 **creating a new file** 링크). 파일 이름을 `worksheet.md`로 쓰고, 편집 칸에 붙여 넣은 뒤 **Commit changes**를 누릅니다.

## 2. 강사 초대

내 저장소의 **Settings → Collaborators → Add people**에서 `wild-mental`을 찾아 초대합니다. 목록에 `wild-mental`이 수락 대기(Pending invite)로 보이면 여러분이 할 일은 끝났습니다.

> [작성 예정] 초대 버튼 문구와 Settings 탭이 안 보일 때(창이 좁을 때) 찾는 법 — 실제 화면 확인 뒤 적음

## 3. 작업 폴더 만들기

1. 바탕화면이나 문서 폴더에 `design-thinking-worksheet` 폴더를 만듭니다.
2. 내 저장소의 `worksheet.md` 화면에서 **Download raw file**(내려받기 아이콘)을 눌러 이 폴더에 저장합니다. 파일 이름이 `worksheet.md` 그대로인지 확인합니다.

> [작성 예정] Mac·Windows에서 새 폴더 만들기, 파일 확장자 보이게 하기, 내려받은 파일을 작업 폴더로 옮기기 (단축키는 「[Windows 사용자 메모](../help/windows-notes.md)」와 맞춤)

## 4. Claude Code에서 작업 폴더 열고 하위 폴더 만들기

1. Claude Code 데스크톱 앱의 **Code** 탭을 엽니다. 입력창 아래의 환경 선택에서 내 컴퓨터(Local)를, 폴더 선택에서 `design-thinking-worksheet` 폴더를 고릅니다. 하위 폴더가 아니라 맨 위 폴더를 고릅니다.

> [캡처 예정] 공통: Code 탭 입력창 아래 줄(환경 · 폴더 · 모드 · 모델)

2. 지시문 킷의 「[작업 폴더 준비 지시문](../kits/claude-code-research-prompts.md)」을 붙여 넣어 보냅니다.
3. 작업 폴더 안에 `research/` · `prototype/` · `interviews/` 세 폴더가 생겼는지 봅니다.

> [작성 예정] 지시문을 보낸 뒤 "이렇게 나오면 정상"의 기준(세 폴더 생성 · `worksheet.md` 제목 목록 · 다섯 줄 요약)과, 폴더 접근 허락을 묻는 창이 뜰 때 할 일

## 5. 하루를 마치기 전에: 저장소에 올리기

1. 내 저장소 첫 화면에서 **Add file → Upload files**를 누릅니다.
2. 작업 폴더 **안의** `worksheet.md`와 `research` · `prototype` · `interviews` 폴더를 끌어다 놓습니다. 작업 폴더 자체를 끌어다 놓지 않습니다. 같은 이름의 파일은 새 내용으로 바뀝니다.
3. **Commit changes**를 누릅니다.
4. 저장소 이름 옆에 **Private** 표시가 있는지, Settings → Collaborators에 `wild-mental`이 있는지 확인합니다.

`worksheet.md` 맨 위 「기본 정보」 아래의 파일 체크리스트로 Day 1 · Day 2에 올릴 파일을 확인할 수 있습니다.

> [작성 예정] 폴더째 끌어다 놓기가 되는 브라우저와 안 될 때 파일을 골라 올리는 법, 빈 폴더는 올라가지 않는다는 점, 올린 뒤 폴더 안까지 들어가 확인하는 법

## 자주 하는 실수와 고친 예

> [작성 예정] 3~5개: 저장소를 Public으로 만듦 · 저장소나 파일 이름 철자가 다름 · 다른 폴더를 열고 시작함 · GitHub 웹 화면에서 `worksheet.md`를 고친 뒤 작업 폴더의 옛 파일을 올려 덮어씀 · 작업 폴더 자체를 끌어다 놓아 한 단계 깊은 폴더가 생김

## 제대로 됐는지 확인

- [ ] 저장소 이름이 `design-thinking-worksheet`이고 이름 옆에 **Private** 표시가 있다
- [ ] 저장소에 `worksheet.md`가 있고, 열면 「서비스 아이디어 기획을 위한 데이터 기반 디자인 씽킹 · 워크시트」 제목과 차례가 보인다
- [ ] Settings → Collaborators에 `wild-mental`이 수락 대기 또는 수락된 상태로 있다
- [ ] 내 컴퓨터의 `design-thinking-worksheet/` 안에 `worksheet.md`와 `research/` · `prototype/` · `interviews/`가 있다
- [ ] Claude Code의 폴더 선택에 `design-thinking-worksheet`가 보인다

## 막혔을 때

> [작성 예정] Copy raw file 아이콘이 안 보일 때 · Settings 탭이 없을 때 · `wild-mental`이 검색되지 않거나 초대가 사라졌을 때 · Download raw file이 브라우저에서 글로 열릴 때 · Upload files에 폴더가 안 끌려갈 때 · Claude Code가 다른 폴더를 보고 있을 때

수업 전에 혼자 하다 막힌 단계는 표시해 두고 첫날 수업 시작 전에, 수업 중에는 손을 들어 현장에서 함께 해결합니다.

> [작성 예정] 화면 확인 날짜: YYYY-MM-DD

<!-- 아래는 작성자용 자리표시입니다. 가이드를 다 쓰면 「준비 중」 안내와 [작성 예정] 표시, 이 줄부터 「작성 계획」 끝까지를 지우고 본문으로 바꿉니다. 제목 줄은 그대로 둡니다. -->

## 작성 계획

| 항목 | 내용 |
|---|---|
| 교재 위치 | 1.1절 오늘의 지도 (실습 안내 11쪽) · 부록 A-1 (41~42쪽) |
| 교재 원문 | 상위 프로젝트 `docs/4-2/manuscript/part-1.md` 1.1절 [실습 안내] · `appendix-a-tools.md` A-1 |
| 유형 | T 도구 조작 |
| 우선순위 · 마감 | P0 · 11/23(월) 사전 안내와 함께 |
| 목표 수준 (표준) | 저장소 만들기부터 올리기까지 단계별 글, 캡처 2곳(아이콘만 있는 버튼과 입력창 아래 줄), 막힘 3~5개, 맨 아래 화면 확인 날짜 |

### 이 가이드가 채울 것 (교재에 없는 것)

- 실제 화면의 버튼 이름과 위치(교재 A-1은 흐름만 있음)
- 하루 끝 올리기에서 생기는 실수(덮어쓰기, 폴더 한 단계 깊어짐, 빈 폴더)
- 작업 폴더의 `worksheet.md`만 고치고 GitHub 웹 화면에서는 고치지 않는다는 원칙과 그 이유

### 지킬 규칙

- `_context/RULES.md` 전부. 특히 학생에게 하는 말만 · 인쇄본과 같은 이름 · 교재 내용 반복 금지.
- 제목(맨 위 `#` 줄)은 인쇄본과 글자 하나까지 같아야 합니다. 바꾸지 않습니다.

### 완료 기준

- [ ] 「준비 중」 안내와 모든 [작성 예정] 표시, 이 작성 계획을 지웠다
- [ ] [캡처 예정] 2곳을 `images/workspace-repo-setup-guide-1.png`, `-2.png`로 바꿨다
- [ ] 맨 아래에 "화면 확인 날짜: YYYY-MM-DD"를 적었다
- [ ] `_context/RULES.md`의 점검 명령을 돌려 걸린 곳이 없다
- [ ] 「막혔을 때 모음」의 GitHub 항목을 같은 커밋에서 맞췄고, README 「가이드 고침 이력」에 한 줄 더했다
