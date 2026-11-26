# CURSOR_TASKS

할 일은 여기에 적는다. "체크해봐"라고 하면 **요청**에서 체크된 항목만 작업한다.

작업이 끝나면 그 줄은 요청에서 빠지고 **완료**로 옮겨진다.

## 요청

매장 뷰어 전환은 2026-11-26에 끝났다(아래 완료 참고). 새로 시킬 일을 여기에 적는다.

이전 목록.

- [ ] 도면에서 가구를 드래그로 옮긴다
- [ ] 프로젝트를 저장한다

## 완료

- 2026-11-26 매장 뷰어 전환 (Claude Code 작업). 화면은 `src/components/viewer.tsx`와 `src/components/plan-map.tsx`, 데이터는 `src/lib/shop.ts`, 이미지 폴더 읽기는 `src/lib/views.ts`다.
  - 도면의 구역이나 카메라를 누르면 그 자리의 이미지, 배치 이유, 물품과 이유, 동선, 확인할 것이 열린다
  - 컨셉 탭, 두 컨셉 나란히 비교, 고객·직원 동선 표시, URL 공유
  - 예전 주거 공간 화면(`studio.tsx`, `floor-plan.tsx`)은 지웠다. 생성 API와 `catalog.ts`·`types.ts`·`concept.ts`·`prompts.ts`는 화면에서 쓰지 않지만 남겨 두었다
