# ax-wave-design-thinking-wildmental — 작업 안내

4-2 「서비스 아이디어 기획을 위한 데이터 기반 디자인 씽킹」 교재(인쇄본)와 함께 쓰는 **공개 온라인 자료실** 저장소입니다. 이 파일은 사이트에 나오지 않습니다(`_config.yml` exclude). 이 저장소에서 일을 시작할 때 이 파일과 `_context/RULES.md`를 먼저 읽습니다. 제작 계획과 후속 작업 목록은 상위 프로젝트의 비공개 문서 `../docs/4-2/ONLINE_MATERIALS_PLAN.md` · `../docs/4-2/HUB_TODO.md`에 있습니다(이 저장소에는 두지 않음).

## 배경 (2026-11-20)

- 교재는 이 자료실보다 **먼저 조판**되었습니다(2026-11-20, 47쪽). 교재는 가이드를 이름으로만 가리키고(`→ 온라인 가이드: 「이름」` 19곳, 9개), 1.1절과 부록 A 첫 쪽에 아래를 인쇄했습니다. 그래서 **계정 이름, 저장소 이름, 가이드 제목, 학생 저장소 이름은 바꿀 수 없습니다.**
  - 자료실: `https://wild-mental.github.io/ax-wave-design-thinking-wildmental/` (이 저장소의 GitHub Pages)
  - 자료실 저장소: `https://github.com/wild-mental/ax-wave-design-thinking-wildmental` (워크시트 문서 원본 `worksheet.md`)
  - 강사 GitHub 아이디: `wild-mental` (학생이 비공개 저장소에 초대)
  - 학생 비공개 저장소이자 작업 폴더 이름: `design-thinking-worksheet`
- 강사 결정 (상위 프로젝트 `docs/4-2/TEXTBOOK_SPEC.md` §1-4-12 · §1-4-14):
  - 4-2 전용 새 공개 저장소입니다. 4-1 자료실(`ax-wave-uxui-wildmental`)은 건드리지 않습니다.
  - 학생은 비공개 저장소 `design-thinking-worksheet`를 새로 만들고, `worksheet-template/worksheet.md`를 Copy raw file로 복사해 붙여 넣은 뒤 `wild-mental`을 초대합니다. 내 컴퓨터의 같은 이름 폴더를 Claude Code 작업 폴더로 쓰고, 하루를 마치기 전에 Add file → Upload files로 올립니다. Git 명령은 다루지 않습니다.
  - 개념 프로토타입은 배포하지 않습니다. 화면 녹화는 만들지 않습니다.
  - ChatGPT 공유 링크 같은 외부 대화 링크는 인쇄본에 넣지 않고, 필요하면 자료실에만 둡니다.
- 수업: 2026-11-30(월) ~ 12-01(화), Day 1~2 = 교재 Part 1~2.

## 폴더

| 경로 | 무엇 | 사이트에 공개 |
|---|---|---|
| `README.md` | 자료실 첫 화면 = 교재 매칭표 (교재 절 · 교재 쪽 · 온라인 가이드 · 함께 쓰는 자료), 처음 오셨다면, 도움말, 가이드 고침 이력 | 예 |
| `guides/` | 온라인 가이드 9개 (2026-11-20 모두 작성). 캡처는 `guides/images/` (1곳 작성, Claude Code 입력창 아래 줄 1곳은 강사 촬영 대기) | 예 |
| `pre-course-notice.md` | 사전 안내 (2026-11-20 작성. Claude 계정은 수업 전에 미리 배부됨) | 예 |
| `help/` | 도움말 3개: 막혔을 때 모음 · 다른 AI 코딩 도구 대응 · Windows 메모 (가이드를 모아 가리킴, RULES §4) | 예 |
| `kits/` | 지시문 킷 (상위 프로젝트 `docs/4-2/kits/`의 사본) | 예 |
| `worksheet-template/` | 워크시트 원본(상위 프로젝트 `docs/4-2/worksheet/`의 사본)과 시작 안내. 학생은 github.com 화면에서 열어 복사 | 아니오 (저장소 화면에서 봄) |
| `_context/` | 작성 규칙, 교재↔자료실 매칭표(강사용 상태 추적), 가이드 목록, 점검 · 동기화 스크립트 | 아니오 (저장소에는 공개) |

## 가이드 하나를 쓰는 순서

1. `guides/<파일>.md`의 각 절에 있는 `[작성 예정]` 메모와 맨 아래 「작성 계획」을 읽습니다.
2. 「작성 계획」의 교재 원문(상위 프로젝트 `docs/4-2/manuscript/`)을 읽습니다. 교재에 있는 내용은 되풀이하지 않고 절을 가리킵니다.
3. 칸 이름 · 점검 질문은 `worksheet-template/worksheet.md`, 지시문은 `kits/claude-code-research-prompts.md`를 따릅니다.
4. 원자료를 써야 하는 가이드(「관통 예제 리서치 보고서 전문」 · 「JTBD 심층 인터뷰 가이드」)는 상위 프로젝트 `docs/4-2/ONLINE_MATERIALS_PLAN.md` §3의 원천과 고칠 점을 따릅니다. 원자료 파일 자체나 정정 메모는 이 저장소에 넣지 않습니다.
5. 본문을 쓰고, 「준비 중」 안내 · `[작성 예정]` 표시 · 작성자용 주석과 「작성 계획」을 지웁니다. 제목 줄은 그대로 둡니다.
6. `_context/RULES.md` §8 점검 명령을 돌립니다.
7. `_context/TEXTBOOK_HUB_MAP.md`의 상태를 「작성」으로, README 「가이드 고침 이력」에 한 줄을 더합니다. 상위 프로젝트 `docs/4-2/ONLINE_MATERIALS_PLAN.md` §3의 상태도 같이 고칩니다.

## 절대 하지 않을 것

- 강사용 내용(피드백 기준과 운영, 차시 운영 시간, 설계 의도, 원자료 정정 메모)을 넣지 않습니다. 이 저장소는 공개입니다.
- 실제 개인 데이터(실명 · 연락처 · 실제 인터뷰 기록)를 넣지 않습니다.
- 인쇄된 이름 · 주소 · 저장소 이름 · 가이드 제목을 바꾸지 않습니다.
- `worksheet-template/worksheet.md`와 `kits/claude-code-research-prompts.md`를 이 저장소에서 직접 고치지 않습니다. 상위 프로젝트 원본을 고친 뒤 동기화합니다.
- 강사의 확인 없이 저장소 설정(Pages 포함)을 바꾸지 않습니다.

## 교재가 바뀌었을 때

상위 프로젝트(`../docs/4-2/`)가 원고 · 워크시트 · 킷의 원본입니다. 바뀌면 저장소 맨 위에서 `sh _context/sync-from-textbook.sh`를 실행해 사본을 다시 복사하고 점검합니다. 다시 조판해 쪽이 바뀌면 `README.md` · `_context/TEXTBOOK_HUB_MAP.md` · `_context/guides.json`의 쪽을 함께 고칩니다.

## 공개 상태

- 2026-11-20 공개 저장소 `wild-mental/ax-wave-design-thinking-wildmental`로 올림(main).
- GitHub Pages 설정은 강사가 직접: Settings → Pages → Deploy from a branch → `main` · `/ (root)` → Save. 인쇄된 자료실 주소가 열리는지 확인합니다.
