# 이미지 프롬프트

> **2026-11-26: 실제 도면이 나와 아래 프롬프트는 모두 이전 배치 기준이 됐다.** 실제 도면(`기획_통합.md`의 "평면 4안")에 맞춰 다시 써야 한다. 가이드 그림 방식(도면에서 구도 그림을 만들어 레퍼런스로 첨부, 한 장씩 대조)은 그대로 쓴다.

배치는 **3안으로 확정됐다(2026-11-26)**. 도면은 [`public/plan/floor-plan-draft.png`](public/plan/floor-plan-draft.png), 구역별 내용은 [`기획_통합.md`](기획_통합.md)의 "평면 3안"과 앱 화면에 있다.

- 컨셉: **바디·스킨케어 VIP 라운지.** 백화점 VIP 라운지처럼 대접받는 느낌이 목표다.
- **방식: 글로만 배치를 지시하지 않는다.** `public/plan/guides/guide.html?view=<시점>`으로 도면에서 구도 가이드 그림을 만들어 첫 번째 레퍼런스로 첨부하고, "카메라·벽·가구 위치는 그림 그대로 두고 색 상자만 실제 마감과 가구로 바꾸라"고 지시한다. 한 장 뽑을 때마다 도면과 대조한 뒤 다음 장으로 넘어간다. 2026-11-26에 글로만 지시한 9컷 중 4컷이 도면과 달랐고, 가이드를 첨부한 인허가 벽은 한 번에 맞았다.
- 관리실로 가는 개구부는 모두 아치형이다. 가이드 그림에는 아직 네모로 그려져 있으니 프롬프트에 "arched opening"을 적는다.
- 순서: **브랜드 월 컷을 가장 먼저** 뽑아 분위기를 정한다. A안(에스테틱)으로 배치가 맞는 컷을 확정한 뒤, 그 컷을 레퍼런스로 넣어 B안(메디컬)을 뽑는다.
- 고른 이미지는 적힌 경로에 저장한다. 앱이 폴더를 읽어 바로 보여 준다.
- 상호는 **TOMATOK VIP LOUNGE**다(2026-11-26). 브랜드 월 사인은 2줄(윗줄 TOMATOK, 아랫줄 VIP LOUNGE)로 한다. 3줄은 과하다. 철자가 틀리거나 다른 글자가 생긴 컷은 버린다.

## 3안 · 1. 브랜드 월 (입구에서 정면)

카메라 1. 출입문 바로 안쪽에서 정면을 본다. 문에서 벽까지 5.8m, 벽 폭 4m, 문 중심과 벽 중심이 한 줄이다.

### 확인할 것

- 브랜드 월이 화면 한가운데 정면에 있는지, 문과 벽 사이 바닥에 가구가 없는지
- 벽 앞에 의자나 벤치가 붙어 있지 않은지(낮은 콘솔 하나만 허용)
- 벽 오른쪽에 복도로 들어가는 개구부가 있고, 관리실 문이나 베드가 보이지 않는지
- **개구부 안으로 복도가 깊이 뻗어 보이지 않는지.** 복도는 브랜드 월과 나란히 가로로 지나가고 깊이가 1.8m뿐이라, 개구부 안에는 1.8m 뒤의 벽만 정면으로 보여야 한다
- 왼쪽 벽이 1.5m쯤 뒤로 물러나 있고 그 벽에 인증서 액자가 걸려 있는지
- 천장이 낮은 편(약 2.5m)으로 보이는지. 2층 높이 로비처럼 뽑힌 컷은 버린다
- 사인이 TOMATOK / VIP LOUNGE 2줄이고 철자가 맞는지, 다른 곳에 글자가 없는지

### A안 에스테틱

- 저장: `public/views/aesthetic/entry.webp`
- 레퍼런스: `16-27-12 001.jpeg`, `16-27-33 002.png`, `16-27-33 001.jpeg` (`reference/` 폴더, 파일명 앞부분은 `KakaoTalk_Photo_2026-11-25-`)

```text
Interior of a private VIP lounge for body and skin-care treatments, designed to feel like a department-store VIP lounge where every guest is hosted. View from just inside the glass entrance doors, looking straight ahead, perfectly symmetrical one-point perspective.

Directly ahead, 5.8 m from the camera and exactly centred in the frame, stands the brand wall: a single feature wall 4 m wide and full ceiling height, the brightest and most refined surface in the room. In its centre at eye level is elegant back-lit brass lettering in a refined serif typeface, in exactly two centred lines: line 1, large, reads TOMATOK; line 2, smaller with wide letter spacing, reads VIP LOUNGE. The spelling must be exactly as written, with generous empty wall around the lettering. Below the lettering, a low slim console table carrying a single generous arrangement of white flowers. Nothing else stands in front of this wall: no chairs, no benches, no desk. The floor between the entrance and the brand wall is completely clear.

To the right of the brand wall, the same wall continues and has one plain open doorway, 1.8 m wide. Behind the brand wall a corridor runs sideways, left to right, parallel to the brand wall, and is only 1.8 m deep. So through the doorway we see only a plain softly lit wall about 1.8 m behind the opening, facing the camera; the corridor continues out of sight to the left and right. No hallway receding into depth, no treatment beds and no doors. Further right, at the edge of the frame, the start of a lounge with a sofa.

To the left of the brand wall, the wall steps back about 1.5 m. On that recessed wall hang a neat row of framed certificates lit by small picture lights, and beyond them a long built-in upholstered wall bench with two small round side tables. At the far left edge of the frame, lounge armchairs with arms grouped around a low round table, spaced generously apart.

The ceiling is low, about 2.5 m, flat, with a continuous warm cove light along the top of the walls. No chandeliers, no double-height space.

Style: boutique aesthetic spa lounge, warm and hospitable. Cream plaster walls with classic wall mouldings, the brand wall set in a shallow arched niche finished in honed travertine, brass details, dark walnut herringbone wood floor, warm 2700-3000K indirect lighting, wall sconces, boucle and linen upholstery in ivory and warm beige, black accent side tables, white flowers.

Photorealistic architectural interior photograph, eye level 1.5 m, 24 mm lens, landscape 3:2, sharp detail, natural materials, no people, no other text anywhere except the brand wall lettering, no other logos, no watermark.
```

### B안 메디컬

A안 컷을 확정한 뒤에 뽑는다. 확정한 A안 이미지를 **첫 번째 레퍼런스로** 넣고, "배치와 가구 위치, 카메라는 그대로 두고 마감·색·가구 디자인만 바꾼다"고 지시한다.

- 저장: `public/views/medical/entry.webp`
- 레퍼런스: 확정한 A안 `entry` 컷, `16-26-44.png`, `16-27-04.png`

```text
Keep exactly the same room, camera position, wall positions, doorway, furniture positions and composition as the first reference image. Change only the finishes, colours, lighting colour and furniture design.

The centred brand wall becomes a flat seamless panel in matte white solid surface with a thin vertical line of light on each side and the same two-line lettering, TOMATOK above VIP LOUNGE, in back-lit brushed steel in a clean sans-serif typeface. The low console below carries a small white flower arrangement.

Style: clean professional skin-care centre with a calm, trustworthy mood. Flat white and light grey walls without mouldings and without arches, large matte light-grey floor tiles, slim 4000K linear cove lighting, straight-lined low seating in light grey fabric, white solid-surface side tables, pale wood and blue-grey accents, minimal decoration.

Photorealistic architectural interior photograph, eye level 1.5 m, 24 mm lens, landscape 3:2, sharp detail, no people, no readable text, no logos, no watermark.
```

## 3안 · A안 에스테틱 9컷 (2026-11-26 생성)

힉스필드 GPT Image 2(3:2, 품질 높음, 2K)로 한 장씩 뽑아 `public/views/aesthetic/<시점>.png`에 넣었다. 레퍼런스 이미지는 첨부하지 않았다. 다시 뽑을 때는 아래 프롬프트를 그대로 쓴다.

### 1. 브랜드 월 (입구에서 정면)

- 저장: `public/views/aesthetic/entry.png`

```text
Interior of a private VIP lounge for body and skin-care treatments, designed to feel like a department-store VIP lounge where every guest is hosted. View from just inside the glass entrance doors, looking straight ahead, perfectly symmetrical one-point perspective. The wall we face is one very long flat wall running left to right across the whole picture, parallel to the picture plane; every part of it faces the camera and none of it turns toward us or recedes into depth. Directly ahead, 5.8 m from the camera and exactly centred in the frame, is the brand wall: a section 4 m wide that stands 1.5 m forward of the rest of the long wall, full ceiling height, the brightest and most refined surface in the room. In its centre at eye level is elegant back-lit brass lettering in a refined serif typeface, in exactly two centred lines: line 1, large, reads TOMATOK; line 2, smaller with wide letter spacing, reads VIP LOUNGE. The spelling must be exactly as written. Below the lettering, a low slim console table carrying a single generous arrangement of white flowers. Nothing else stands in front of this wall and the floor between the entrance and the brand wall is completely clear. To the right of the lettering, in the same forward wall plane, one plain open doorway 1.8 m wide. Behind this wall a corridor runs sideways, left to right, parallel to the wall and only 1.8 m deep, so through the doorway we see only a plain softly lit wall about 1.8 m behind, facing the camera; no hallway receding into depth, no doors, no beds. To the left of the brand wall, the long wall continues to the left edge of the picture, set back 1.5 m but still flat and facing the camera, seen frontally, not as a side wall. On that left wall, facing us: first a neat row of framed certificates lit by small picture lights, then a long built-in upholstered wall bench with small round side tables in front of it, continuing out of frame to the left. In the left foreground, lounge armchairs with arms around a low round table; in the right foreground, the corner of a lounge sofa. The ceiling is low, about 2.5 m, flat, with a continuous warm cove light along the top of the walls. No chandeliers. Style: boutique aesthetic spa lounge, warm and hospitable. Cream plaster walls with classic wall mouldings, the brand wall set in a shallow arched niche finished in honed travertine, brass details, dark walnut herringbone wood floor, warm 2700-3000K indirect lighting, wall sconces, boucle and linen upholstery in ivory and warm beige, black accent side tables, white flowers. Photorealistic architectural interior photograph, eye level 1.5 m, 24 mm lens, landscape 3:2, sharp detail, natural materials, no people, no other text anywhere except the brand wall lettering, no other logos, no watermark.
```

### 2. TV 라운지

- 저장: `public/views/aesthetic/lounge-tv.png`

```text
TV lounge area inside a private body and skin-care VIP lounge, viewed from behind a three-seat sofa toward the TV wall 3.5 m ahead. In the foreground the back of the sofa; in front of it a low rectangular coffee table. On the left, a second three-seat sofa placed at a right angle, facing right, so the two sofas form an L. On the right, two matching armchairs with arms facing left. On the long panelled wall straight ahead, one large 85-inch wall-mounted TV showing a soft close-up of a skincare bottle with a blurred subtitle bar. In the same wall, to the left of the TV, one plain open doorway 1.8 m wide; through it only a softly lit wall about 1.8 m behind is visible. Another identical open doorway further to the right of the TV. At the far right edge of the frame, the end of a long stone reception counter with a back-lit glass display wall of skincare products behind it. The seating is generously spaced. Style: TOMATOK VIP LOUNGE, a boutique body and skin-care VIP lounge with the feel of a department-store VIP lounge where every guest is hosted. Cream plaster walls with classic wall mouldings, honed travertine accents, brass details, dark walnut herringbone wood floor, warm 2700-3000K indirect cove lighting, wall sconces, boucle and linen upholstery in ivory and warm beige, black accent side tables, white flowers. Low flat ceiling about 2.5 m with a continuous warm cove light along the top of the walls, no chandeliers. Photorealistic architectural interior photograph, eye level 1.5 m, 24 mm lens, landscape 3:2, sharp detail, natural materials, no people, no readable text, no logos, no watermark.
```

### 3. 커피바와 라운지 좌석

- 저장: `public/views/aesthetic/coffee.png`

```text
Self-service coffee bar and lounge seating inside a private body and skin-care VIP lounge. View across the lounge seating toward the far wall. Against the far wall stands one self-serve coffee bar counter, 4 m long, with a stone top and wood front: two espresso machines, a hot-water dispenser, neat rows of white porcelain cups and saucers, a tea selection in a wooden box, small pastries under two glass domes, an under-counter fridge, and at one end a brass tray stand for used cups. No staff behind it. Above the bar, wide windows covered with sheer ivory curtains. In the foreground and middle of the room, two separate groups of four lounge armchairs with arms, each group around a low round table, the groups set well apart. Along the window wall to the right of the bar, two pairs of armchairs each with a small round side table between them. At the far right edge, a row of armchairs against a side wall. At the far left edge, glass entrance doors. Style: TOMATOK VIP LOUNGE, a boutique body and skin-care VIP lounge with the feel of a department-store VIP lounge where every guest is hosted. Cream plaster walls with classic wall mouldings, honed travertine accents, brass details, dark walnut herringbone wood floor, warm 2700-3000K indirect cove lighting, wall sconces, boucle and linen upholstery in ivory and warm beige, black accent side tables, white flowers. Low flat ceiling about 2.5 m with a continuous warm cove light along the top of the walls, no chandeliers. Photorealistic architectural interior photograph, eye level 1.5 m, 24 mm lens, landscape 3:2, sharp detail, natural materials, no people, no readable text, no logos, no watermark.
```

### 4. 데스크·화장품

- 저장: `public/views/aesthetic/display.png`

```text
Reception desk and cosmetics showcase inside a private body and skin-care VIP lounge, with the glamour of a department-store beauty counter. One long straight counter, 4.6 m long, with a stone top, stands parallel to the wall behind it with a 0.9 m staff aisle between. The left half of the counter is the reception desk: a payment terminal, a small monitor and a tablet stand. The right half is the cosmetics showcase: an internally lit glass front, a tray of tester bottles, a round vanity mirror, product cards, and two upholstered counter stools on the customer side. Behind the counter the whole wall is one back-lit glass display wall, 4.4 m wide and full height, with a curated range of skincare bottles and boxes on individually lit shelves and closed stock cabinets below. A row of small brass pendant lights hangs above the showcase half. To the left of the display wall, in the same wall, one closed wooden door. Viewed from the lounge at a slight angle; at the left edge part of a lounge armchair. Style: TOMATOK VIP LOUNGE, a boutique body and skin-care VIP lounge with the feel of a department-store VIP lounge where every guest is hosted. Cream plaster walls with classic wall mouldings, honed travertine accents, brass details, dark walnut herringbone wood floor, warm 2700-3000K indirect cove lighting, wall sconces, boucle and linen upholstery in ivory and warm beige, black accent side tables, white flowers. Low flat ceiling about 2.5 m with a continuous warm cove light along the top of the walls, no chandeliers. Photorealistic architectural interior photograph, eye level 1.5 m, 24 mm lens, landscape 3:2, sharp detail, natural materials, no people, no readable text, no logos, no watermark.
```

### 5. 2인실

- 저장: `public/views/aesthetic/room.png`

```text
Private two-bed body and skin-care treatment room, 8 m wide and 4.6 m deep, viewed from just inside the room near the front wall, standing at the edge of the dressing zone and looking diagonally toward the back wall. Exactly two massage beds side by side with their heads toward the back wall, about 2 m apart, separated by a floor-to-ceiling linen curtain on a ceiling track, drawn half open. Generous working space, more than 1 m, on the outer side of each bed. On the back wall exactly at the curtain line, a compact hand-wash vanity with a basin and a mirror above. Beside each bed a small treatment trolley, and a therapist stool at the head of each bed. Along the front wall on the right, a low cabinet with a towel warmer and a covered linen bin. At the left edge of the frame, part of the dressing zone: a partition wall, one curtained changing booth and a full-length mirror. Rolled white towels on each bed. No windows; dimmable warm lighting. Style: TOMATOK VIP LOUNGE, a boutique body and skin-care VIP lounge with the feel of a department-store VIP lounge where every guest is hosted. Cream plaster walls with classic wall mouldings, honed travertine accents, brass details, dark walnut herringbone wood floor, warm 2700-3000K indirect cove lighting, wall sconces, boucle and linen upholstery in ivory and warm beige, black accent side tables, white flowers. Low flat ceiling about 2.5 m with a continuous warm cove light along the top of the walls, no chandeliers. Photorealistic architectural interior photograph, eye level 1.5 m, 24 mm lens, landscape 3:2, sharp detail, natural materials, no people, no readable text, no logos, no watermark.
```

### 6. 발마사지

- 저장: `public/views/aesthetic/foot.png`

```text
Open self-service foot-massage seating inside a private body and skin-care VIP lounge, viewed diagonally from the lounge. Exactly five matching upholstered armchairs with arms in one single straight row, backs against a panelled wall, facing the open lounge, with no partition and no enclosure. On the floor in front of each armchair sits a separate compact electric foot-and-calf massager: a low box-shaped unit about knee height with two open slots for the feet and calves. These are ordinary lounge armchairs with separate floor-standing foot massager units, not full-body massage chairs. A small round side table between armchairs and a woven basket for belongings beside each. Nobody is seated. On the adjacent long wall to the right, a built-in upholstered wall bench and, further along, one plain open doorway. In the right foreground, part of a group of lounge armchairs around a low round table. Style: TOMATOK VIP LOUNGE, a boutique body and skin-care VIP lounge with the feel of a department-store VIP lounge where every guest is hosted. Cream plaster walls with classic wall mouldings, honed travertine accents, brass details, dark walnut herringbone wood floor, warm 2700-3000K indirect cove lighting, wall sconces, boucle and linen upholstery in ivory and warm beige, black accent side tables, white flowers. Low flat ceiling about 2.5 m with a continuous warm cove light along the top of the walls, no chandeliers. Photorealistic architectural interior photograph, eye level 1.5 m, 24 mm lens, landscape 3:2, sharp detail, natural materials, no people, no readable text, no logos, no watermark.
```

### 7. 관리실 앞 복도

- 저장: `public/views/aesthetic/corridor.png`

```text
Quiet private corridor in front of the treatment rooms of a body and skin-care VIP lounge, 1.8 m wide and very long, viewed along its length from one end. On the left wall, three identical closed wooden treatment-room doors spaced far apart, about 8 m between one door and the next, each with a small blank brass plaque and a wall sconce beside it. On the right wall, near the camera, two discreet flush staff doors; further along, one plain open doorway 1.8 m wide leading out to the lounge, with warm light spilling through it. A slim brass handrail runs along the right wall. The corridor is calmer and slightly dimmer than a lobby, lit only by a continuous warm cove light and the sconces. The floor is completely clear. Style: TOMATOK VIP LOUNGE, a boutique body and skin-care VIP lounge with the feel of a department-store VIP lounge where every guest is hosted. Cream plaster walls with classic wall mouldings, honed travertine accents, brass details, dark walnut herringbone wood floor, warm 2700-3000K indirect cove lighting, wall sconces, boucle and linen upholstery in ivory and warm beige, black accent side tables, white flowers. Low flat ceiling about 2.5 m with a continuous warm cove light along the top of the walls, no chandeliers. Photorealistic architectural interior photograph, eye level 1.5 m, 24 mm lens, landscape 3:2, sharp detail, natural materials, no people, no readable text, no logos, no watermark.
```

### 8. 파우더룸

- 저장: `public/views/aesthetic/powder.png`

```text
Powder room inside a private body and skin-care VIP lounge, 4 m wide and 4.6 m deep, viewed from the doorway. Along the back wall runs one long stone vanity counter with exactly four seats side by side, each seat with its own softly back-lit mirror on the wall. Four upholstered vanity chairs with backs and arms. On the counter in front of each seat: a hair dryer in a holder and a small amenity tray with cotton pads, cotton swabs and lotion bottles. One small flower arrangement at the end of the counter. On the left side wall a full-length mirror and a brass grab rail; on the right side wall a small hand basin. Soft, flattering front lighting from the mirrors, brighter than a treatment room. No windows. Style: TOMATOK VIP LOUNGE, a boutique body and skin-care VIP lounge with the feel of a department-store VIP lounge where every guest is hosted. Cream plaster walls with classic wall mouldings, honed travertine accents, brass details, dark walnut herringbone wood floor, warm 2700-3000K indirect cove lighting, wall sconces, boucle and linen upholstery in ivory and warm beige, black accent side tables, white flowers. Low flat ceiling about 2.5 m with a continuous warm cove light along the top of the walls, no chandeliers. Photorealistic architectural interior photograph, eye level 1.5 m, 24 mm lens, landscape 3:2, sharp detail, natural materials, no people, no readable text, no logos, no watermark.
```

### 9. 인허가 진열 벽

- 저장: `public/views/aesthetic/license.png`

```text
Recessed section of the long lounge wall inside a private body and skin-care VIP lounge, viewed straight on from the lounge. In the centre of the wall, above a slim brass display ledge, hangs a neat single row of five framed certificates and licences in matching thin brass frames, each lit by its own small picture light; the certificate text is blurred and unreadable. To the left of the certificates, along the same wall, a long built-in upholstered wall bench with two small round side tables in front of it. At the right edge of the frame, the wall steps forward about 1.5 m to form the side of a travertine feature wall. The floor in front is clear. Style: TOMATOK VIP LOUNGE, a boutique body and skin-care VIP lounge with the feel of a department-store VIP lounge where every guest is hosted. Cream plaster walls with classic wall mouldings, honed travertine accents, brass details, dark walnut herringbone wood floor, warm 2700-3000K indirect cove lighting, wall sconces, boucle and linen upholstery in ivory and warm beige, black accent side tables, white flowers. Low flat ceiling about 2.5 m with a continuous warm cove light along the top of the walls, no chandeliers. Photorealistic architectural interior photograph, eye level 1.5 m, 24 mm lens, landscape 3:2, sharp detail, natural materials, no people, no readable text, no logos, no watermark.
```

## 3안 · 아직 뽑지 않은 것

- **B안 메디컬**: A안 컷이 확정되면 각 컷을 첫 번째 레퍼런스로 넣고 마감·색·가구 디자인만 바꿔 뽑는다.
- **항공뷰**: 가장 마지막에 뽑는다. 부분 컷이 다 확정된 뒤, 도면과 확정 컷을 레퍼런스로 넣어야 배치가 틀어지지 않는다.

---

# 이전 프롬프트 (1안 18 × 12m 기준, 쓰지 않는다)

아래는 1안 배치로 쓴 프롬프트다. 배치가 달라 그대로 쓰면 안 되고, 문장 구조와 스타일 문단을 참고하는 용도로만 남긴다.

힉스필드의 GPT Image 2(3:2, 품질 높음, 2K)로 생성했다. 다시 뽑을 때는 프롬프트를 붙여 넣고, 적힌 레퍼런스를 함께 첨부한다. 레퍼런스 파일은 `reference/` 폴더에 있고, 아래에는 파일명 뒷부분만 적었다(앞부분은 모두 `KakaoTalk_Photo_2026-11-25-`).

고른 이미지는 적힌 경로에 저장한다. 물품과 배치는 [`기획_통합.md`](기획_통합.md)의 운영 체크와 [도면](public/plan/floor-plan-draft.png)을 따른다.

## 확인할 것

- 2인실은 베드가 정확히 2개, 발마사지는 암체어 5개와 바닥 마사지기 5대이고 전신 안마의자가 아닌지
- 입구 컷에서 룸 문 3개가 벽 전체에 넓게 떨어져 있는지(문 사이 약 6m)
- 화장품이 유리문 진열장 안에 있고 열린 선반에 쌓여 있지 않은지
- 커튼이 두 베드 사이에 있고 세면대가 안쪽 벽 가운데에 있는지
- 간판이나 액자에 엉뚱한 글자나 다른 업체 로고가 생기지 않았는지
- 메디컬 안에 의원, 클리닉 같은 글자가 들어가지 않았는지
- **들어갈 수 없는 공간이 없는지.** 벽으로 막힌 방마다 홀로 난 문이 보이고, 좌석과 진열대 앞에 사람이 걸어 들어갈 통로가 있는지
- 발마사지 의자가 방 안에 갇히지 않고 홀에 열려 있는지, 의자가 벽이 아니라 홀을 향하는지

## 항공뷰 (전체 배치)

2026-11-25에 뽑은 항공뷰 두 장은 버린다. 메디컬은 발마사지 5석이 문 없는 방에 갇혔고 화장품 진열도 막힌 방 안에 들어갔다. 에스테틱은 발마사지 의자가 홀을 등지고 외벽을 보고 있다. 당시 프롬프트를 남기지 않아 배치가 지정되지 않은 탓이다.

- 저장: `public/views/aesthetic/aerial.webp`, `public/views/medical/aerial.webp`
- 레퍼런스: `public/plan/floor-plan-draft.png`를 **첫 번째로** 첨부한다. 그 뒤에 컨셉별 입구 컷 레퍼런스를 붙인다.
- 아래 배치 프롬프트 뒤에 해당 컨셉의 `Style:` 문단(각 컨셉 1번 프롬프트의 것)을 그대로 붙인다.

```text
Top-down isometric cutaway view of a single-storey body and skin-care spa with the roof and ceiling removed, seen from high above the front (entrance) side. The attached floor plan is the exact layout: reproduce its walls, doors and furniture positions precisely and do not add, move or remove any wall. Ignore the orange numbered markers and all text labels on the plan.

Overall shape: one rectangle 18 m wide and 12 m deep. Glass double entrance doors in the centre of the front wall.

Back band, 3.5 m deep: exactly three identical two-bed treatment rooms side by side, each 6 m wide. Each room has one hinged door in its front wall opening onto the central hall. Inside each: a 1.5 m wide dressing zone on the left with two curtained changing booths and two lockers, then two massage beds with heads to the back wall, a ceiling-track curtain between them, and a small hand-wash vanity on the back wall at the curtain line.

Middle band, 5 m deep: one open central hall running the full 18 m width, with no partitions and no internal walls. Upholstered benches against the back wall between the three room doors. On the far left wall, two lounge chairs with a small table. Centre-left, a round consultation table with three chairs. In the centre, a round feature table with flowers. On the right, a lounge: sofa and coffee table facing a TV mounted on the right-hand outer wall, and a self-serve coffee bar counter in the back right corner.

Front band, 3.5 m deep, three parts:
- Front left, 6 m wide: a block of small back-of-house rooms: stock and linen store, powder room with three vanity seats, staff room. Each of these rooms has a visible door.
- Front centre, 6 m wide: the entrance lobby, completely open to the hall with no wall between them. A reception desk stands on the right side of the lobby against the wall of the fourth treatment room. A display of framed certificates hangs on the left lobby wall.
- Front right, 6 m wide: the fourth two-bed treatment room, same contents as the others, with its one door in the wall facing the hall.

Foot-massage seats: exactly five armchairs in one straight row standing IN THE OPEN HALL, with their backs against the hall-side wall of the front-left room block and the seats facing into the hall. One compact foot massager unit on the floor in front of each chair, on the hall side. This seating is NOT a room: no walls, no partitions, no screens and no enclosure around it; it is open to the hall on its front and both ends, and people walk straight to the chairs from the hall floor.

Cosmetics display: one backlit glass display wall built against the hall-facing wall of the fourth treatment room, with one showcase counter standing in the open hall in front of it. It is NOT a separate room and has no walls around it.

Circulation rule: every enclosed room must have a clearly visible door onto the hall. There are no sealed spaces and no dead ends. Clear walking paths at least 1.5 m wide lead from the entrance to the reception desk, to each of the four treatment-room doors, to the foot-massage chairs, to the lounge and to the powder-room door. Nothing blocks the entrance lobby.

Photorealistic architectural dollhouse rendering, high three-quarter angle from the front, whole floor plate visible, landscape 3:2, sharp detail, no people, no readable text, no logos, no watermark.
```

## A안 에스테틱

### 1. 입구에서 홀

- 저장: `public/views/aesthetic/entry.webp`
- 레퍼런스: `16-27-12 001.jpeg`, `16-27-33 002.png`, `16-27-33 001.jpeg`

```text
Wide-angle view from just inside the entrance double doors of a body and skin-care spa, looking straight into a very wide, shallow central hall: 18 m wide from left wall to right wall and only 5 m deep to the far wall. The far wall straight ahead is one long continuous wall 18 m wide with exactly three treatment-room doors spaced far apart, about 6 m between one door and the next, because each door leads to a separate 6 m wide two-bed room; long stretches of plain wall with an upholstered bench separate the doors. The doors are not clustered together. On the right in the foreground, a reception desk running along the right-hand wall with a payment terminal and a monitor. Ahead on the left, a wall display of framed licences and certificates lit by picture lights. In the centre of the hall, a round feature table with a flower arrangement and a small lit glass display case showing the spa's hero skincare products under glass. Beside it, a small round consultation table with three chairs. Far to the right, a lounge with a sofa facing a wall-mounted TV, and a department-store style cosmetics counter with internally lit glass showcases and a backlit wall display behind it. Far to the left, an open row of five armchairs along the wall, each with a compact foot massager unit on the floor in front of it. Guests keep their shoes on; no shoe cabinet.

Style: boutique aesthetic spa, warm and hospitable. Cream plaster walls with classic wall mouldings and arched niches, black accent furniture, dark walnut herringbone wood floor, warm 2700-3000K cove and indirect lighting, decorative wall sconces, curved boucle seating, white flower arrangements, warm beige linen curtains.

Photorealistic architectural interior photograph, eye level 1.5 m, 24 mm wide lens, landscape 3:2, sharp detail, natural materials, no people, no readable text, no logos, no watermark.
```

### 2. 라운지에서 TV 벽

- 저장: `public/views/aesthetic/lounge-tv.webp`
- 레퍼런스: `16-27-33 003.jpeg`, `16-27-14 009.jpeg`, `16-26-35.png`

```text
Lounge corner of a body and skin-care spa, viewed from behind a three-seat sofa toward the TV wall. In the foreground the back of the sofa, in front of it a low coffee table, with one armchair on each side. On the wall ahead, a large wall-mounted TV showing a soft close-up of a skincare product with a subtitle bar. On the left end of the same wall, a self-serve coffee bar: counter with an espresso machine, water dispenser, stacked cups, tea selection, small sink and under-counter fridge. On the right edge of the frame, the start of the cosmetics retail corner with backlit display shelves.

Style: boutique aesthetic spa, warm and hospitable. Cream plaster walls with classic wall mouldings and arched niches, black accent furniture, dark walnut herringbone wood floor, warm 2700-3000K cove and indirect lighting, decorative wall sconces, curved boucle seating, white flower arrangements, warm beige linen curtains.

Photorealistic architectural interior photograph, eye level 1.5 m, 24 mm wide lens, landscape 3:2, sharp detail, natural materials, no people, no readable text, no logos, no watermark.
```

### 3. 발마사지

- 저장: `public/views/aesthetic/foot.webp`
- 레퍼런스: `16-27-13 006.jpeg`, `16-27-13 007.jpeg`

```text
Open self-service foot-massage corner in the main hall of a body and skin-care spa, viewed diagonally from the hall. Exactly five matching upholstered armchairs in a single straight row, backs against the wall, facing the open hall with no partition. On the floor in front of each armchair sits a separate compact electric foot-and-calf massager machine: a low box-shaped unit about knee height with two open slots for the feet and calves. These are ordinary lounge armchairs with separate floor-standing foot massager units, not full-body massage chairs. A small side table between armchairs and a basket for belongings beside each. Nobody is seated. To the right of the row, a door to the powder room. In the background the open hall continues with a small round consultation table and benches along the far wall.

Style: boutique aesthetic spa, warm and hospitable. Cream plaster walls with classic wall mouldings and arched niches, black accent furniture, dark walnut herringbone wood floor, warm 2700-3000K cove and indirect lighting, decorative wall sconces, curved boucle seating, white flower arrangements, warm beige linen curtains.

Photorealistic architectural interior photograph, eye level 1.5 m, 24 mm wide lens, landscape 3:2, sharp detail, natural materials, no people, no readable text, no logos, no watermark.
```

### 4. 2인실 문 안쪽

- 저장: `public/views/aesthetic/room.webp`
- 레퍼런스: `16-27-13 005.jpeg`, `16-27-13 006.jpeg`, `16-27-13 004.jpeg`

```text
Private two-bed body and skin-care treatment room, 6 m wide and 3.5 m deep, viewed from the doorway on the long front wall. On the left side of the room, a 1.5 m wide dressing zone runs from front to back: two separate changing booths, each closed by its own ceiling-track curtain, one at the front and one at the back, and between them two tall personal lockers with key locks. The remaining 4.5 m on the right is the treatment area: exactly two massage beds side by side with heads toward the back wall, separated by a floor-to-ceiling curtain on a ceiling track, drawn half open. On the back wall at the curtain line, a compact therapist hand-wash vanity with a basin and a mirror above. Beside each bed a small treatment trolley and a therapist stool at the head. A small cabinet with a towel warmer in the far right corner. Rolled white towels on each bed. No windows, dimmable warm lighting.

Style: boutique aesthetic spa, warm and hospitable. Cream plaster walls with classic wall mouldings and arched niches, black accent furniture, dark walnut herringbone wood floor, warm 2700-3000K cove and indirect lighting, decorative wall sconces, curved boucle seating, white flower arrangements, warm beige linen curtains.

Photorealistic architectural interior photograph, eye level 1.5 m, 24 mm wide lens, landscape 3:2, sharp detail, natural materials, no people, no readable text, no logos, no watermark.
```

### 5. 화장품 진열

- 저장: `public/views/aesthetic/display.webp`
- 레퍼런스: `16-27-14 009.jpeg`, `16-27-14 008.png`, `16-27-33 003.jpeg`

```text
Luxurious cosmetics boutique corner inside a body and skin-care spa, with the glamour of a flagship department-store beauty counter, viewed from the open hall. The focal point is one grand feature wall about 5 m wide and full ceiling height: three tall illuminated glass-fronted display niches with backlit shelves and a softly glowing blank brand panel in the centre, framed in rich stone and metal trim, with closed stock cabinets below. The spa's own skincare line is shown behind the glass, a curated range of about twenty products in matching elegant bottles and boxes, each shelf individually lit like jewellery. In front of the wall stands one long showcase counter with an internally lit glass front and a stone top, carrying a tray of tester bottles, a round vanity mirror and product information cards, with two upholstered counter stools for trying samples. A row of small pendant lights hangs above the counter. Everything gleams: polished surfaces, layered warm accent lighting, generous flower arrangement at one end. Only this one wall and one counter; no other shelving. At the left edge of the frame, part of a lounge sofa is visible.

Style: boutique aesthetic spa, warm and hospitable. Cream plaster walls with classic wall mouldings and arched niches, black accent furniture, dark walnut herringbone wood floor, warm 2700-3000K cove and indirect lighting, decorative wall sconces, curved boucle seating, white flower arrangements, warm beige linen curtains.

Photorealistic architectural interior photograph, eye level 1.5 m, 24 mm wide lens, landscape 3:2, sharp detail, natural materials, no people, no readable text, no logos, no watermark.
```

## B안 메디컬

### 1. 입구에서 홀

- 저장: `public/views/medical/entry.webp`
- 레퍼런스: `16-26-44.png`, `16-26-55.png`, `16-27-04.png`

```text
Wide-angle view from just inside the entrance double doors of a body and skin-care spa, looking straight into a very wide, shallow central hall: 18 m wide from left wall to right wall and only 5 m deep to the far wall. The far wall straight ahead is one long continuous wall 18 m wide with exactly three treatment-room doors spaced far apart, about 6 m between one door and the next, because each door leads to a separate 6 m wide two-bed room; long stretches of plain wall with an upholstered bench separate the doors. The doors are not clustered together. On the right in the foreground, a reception desk running along the right-hand wall with a payment terminal and a monitor. Ahead on the left, a wall display of framed licences and certificates lit by picture lights. In the centre of the hall, a round feature table with a flower arrangement and a small lit glass display case showing the spa's hero skincare products under glass. Beside it, a small round consultation table with three chairs. Far to the right, a lounge with a sofa facing a wall-mounted TV, and a department-store style cosmetics counter with internally lit glass showcases and a backlit wall display behind it. Far to the left, an open row of five armchairs along the wall, each with a compact foot massager unit on the floor in front of it. Guests keep their shoes on; no shoe cabinet.

Style: clean professional skin-care centre with a clinical, trustworthy mood. Flat white and light grey walls without mouldings, large matte light-grey floor tiles, frosted and clear glass partitions, slim 4000K linear ceiling lights and recessed cove lighting, straight-lined low seating in light grey, white solid-surface counters, pale wood or blue-grey accents, minimal decoration, white curtains.

Photorealistic architectural interior photograph, eye level 1.5 m, 24 mm wide lens, landscape 3:2, sharp detail, natural materials, no people, no readable text, no logos, no watermark.
```

### 2. 라운지에서 TV 벽

- 저장: `public/views/medical/lounge-tv.webp`
- 레퍼런스: `16-26-49.png`, `16-26-59.png`, `16-27-14 009.jpeg`

```text
Lounge corner of a body and skin-care spa, viewed from behind a three-seat sofa toward the TV wall. In the foreground the back of the sofa, in front of it a low coffee table, with one armchair on each side. On the wall ahead, a large wall-mounted TV showing a soft close-up of a skincare product with a subtitle bar. On the left end of the same wall, a self-serve coffee bar: counter with an espresso machine, water dispenser, stacked cups, tea selection, small sink and under-counter fridge. On the right edge of the frame, the start of the cosmetics retail corner with backlit display shelves.

Style: clean professional skin-care centre with a clinical, trustworthy mood. Flat white and light grey walls without mouldings, large matte light-grey floor tiles, frosted and clear glass partitions, slim 4000K linear ceiling lights and recessed cove lighting, straight-lined low seating in light grey, white solid-surface counters, pale wood or blue-grey accents, minimal decoration, white curtains.

Photorealistic architectural interior photograph, eye level 1.5 m, 24 mm wide lens, landscape 3:2, sharp detail, natural materials, no people, no readable text, no logos, no watermark.
```

### 3. 발마사지

- 저장: `public/views/medical/foot.webp`
- 레퍼런스: `16-26-29.png`, `16-27-04.png`

```text
Open self-service foot-massage corner in the main hall of a body and skin-care spa, viewed diagonally from the hall. Exactly five matching upholstered armchairs in a single straight row, backs against the wall, facing the open hall with no partition. On the floor in front of each armchair sits a separate compact electric foot-and-calf massager machine: a low box-shaped unit about knee height with two open slots for the feet and calves. These are ordinary lounge armchairs with separate floor-standing foot massager units, not full-body massage chairs. A small side table between armchairs and a basket for belongings beside each. Nobody is seated. To the right of the row, a door to the powder room. In the background the open hall continues with a small round consultation table and benches along the far wall.

Style: clean professional skin-care centre with a clinical, trustworthy mood. Flat white and light grey walls without mouldings, large matte light-grey floor tiles, frosted and clear glass partitions, slim 4000K linear ceiling lights and recessed cove lighting, straight-lined low seating in light grey, white solid-surface counters, pale wood or blue-grey accents, minimal decoration, white curtains.

Photorealistic architectural interior photograph, eye level 1.5 m, 24 mm wide lens, landscape 3:2, sharp detail, natural materials, no people, no readable text, no logos, no watermark.
```

### 4. 2인실 문 안쪽

- 저장: `public/views/medical/room.webp`
- 레퍼런스: `16-26-29.png`, `16-27-14 009.jpeg`, `16-27-13 005.jpeg`

```text
Private two-bed body and skin-care treatment room, 6 m wide and 3.5 m deep, viewed from the doorway on the long front wall. On the left side of the room, a 1.5 m wide dressing zone runs from front to back: two separate changing booths, each closed by its own ceiling-track curtain, one at the front and one at the back, and between them two tall personal lockers with key locks. The remaining 4.5 m on the right is the treatment area: exactly two massage beds side by side with heads toward the back wall, separated by a floor-to-ceiling curtain on a ceiling track, drawn half open. On the back wall at the curtain line, a compact therapist hand-wash vanity with a basin and a mirror above. Beside each bed a small treatment trolley and a therapist stool at the head. A small cabinet with a towel warmer in the far right corner. Rolled white towels on each bed. No windows, dimmable warm lighting.

Style: clean professional skin-care centre with a clinical, trustworthy mood. Flat white and light grey walls without mouldings, large matte light-grey floor tiles, frosted and clear glass partitions, slim 4000K linear ceiling lights and recessed cove lighting, straight-lined low seating in light grey, white solid-surface counters, pale wood or blue-grey accents, minimal decoration, white curtains.

Photorealistic architectural interior photograph, eye level 1.5 m, 24 mm wide lens, landscape 3:2, sharp detail, natural materials, no people, no readable text, no logos, no watermark.
```

### 5. 화장품 진열

- 저장: `public/views/medical/display.webp`
- 레퍼런스: `16-26-44.png`, `16-27-14 009.jpeg`, `16-26-59.png`

```text
Luxurious cosmetics boutique corner inside a body and skin-care spa, with the glamour of a flagship department-store beauty counter, viewed from the open hall. The focal point is one grand feature wall about 5 m wide and full ceiling height: three tall illuminated glass-fronted display niches with backlit shelves and a softly glowing blank brand panel in the centre, framed in rich stone and metal trim, with closed stock cabinets below. The spa's own skincare line is shown behind the glass, a curated range of about twenty products in matching elegant bottles and boxes, each shelf individually lit like jewellery. In front of the wall stands one long showcase counter with an internally lit glass front and a stone top, carrying a tray of tester bottles, a round vanity mirror and product information cards, with two upholstered counter stools for trying samples. A row of small pendant lights hangs above the counter. Everything gleams: polished surfaces, layered warm accent lighting, generous flower arrangement at one end. Only this one wall and one counter; no other shelving. At the left edge of the frame, part of a lounge sofa is visible.

Style: clean professional skin-care centre with a clinical, trustworthy mood. Flat white and light grey walls without mouldings, large matte light-grey floor tiles, frosted and clear glass partitions, slim 4000K linear ceiling lights and recessed cove lighting, straight-lined low seating in light grey, white solid-surface counters, pale wood or blue-grey accents, minimal decoration, white curtains.

Photorealistic architectural interior photograph, eye level 1.5 m, 24 mm wide lens, landscape 3:2, sharp detail, natural materials, no people, no readable text, no logos, no watermark.
```
