"""매장 평면도 3안을 SVG로 만든다. 단위는 미터.

건축물현황도 배치도(1:250)에서 읽은 실제 건물 형태에 처음 기획(위쪽 3실, 오른쪽 아래 1실, 출입구 아래 가운데)을 얹었다.
2층 501.41㎡(건축물대장). 쓸 층은 2층이다(2026-11-26).
- 아래 외곽은 건축면적 531.66㎡에 맞춰 읽은 것이라 2층 면적보다 6%쯤 크다. 2층이 어디서 줄어드는지는 2층 평면도로 확인해야 한다.
- 왼쪽(기존) 블록 24.0 x 13.7, 오른쪽(증축) 블록 15.3 x 13.5. 오른쪽 블록이 1.5m 아래로 어긋나 있다.
- 치수는 배치도 그림에서 주차 칸과 건축면적으로 축척을 맞춰 읽은 값이라 ±0.5m 정도 오차가 있다.
- 배치도에서 1층 주출입구는 왼쪽 끝(계룡로), 부출입구는 오른쪽 끝(8m 도로)이다. 2층의 계단·승강기 위치는 모른다.

1안(18 x 12), 2안(28 x 18.7)은 _old/ 폴더에 있다. 좌표 원점은 왼쪽 블록의 왼쪽 위 모서리다.
앱(src/lib/views.ts)이 이 파일이 만든 SVG를 줄 단위로 읽으므로 요소를 한 줄에 하나씩 쓴다.
"""
LW, LH = 24.0, 13.7           # 왼쪽 블록
RX, RY, RW, RH = 24.0, 1.5, 15.3, 13.5   # 오른쪽 블록
W = RX + RW                   # 39.3
RB = RY + RH                  # 15.0
RD = 4.6                      # 2인실 깊이
C1 = 6.4                      # 왼쪽 블록: 복도와 홀 사이 벽
R1 = RY + RD                  # 6.1 오른쪽 블록: 위쪽 방 앞 벽
C2 = R1 + 1.8                 # 7.9 오른쪽 블록: 복도와 홀 사이 벽
o = []
a = o.append
VB = (-3.6, -2.7, 47.2, 21.6)
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VB[0]} {VB[1]} {VB[2]} {VB[3]}" width="1888" height="864" font-family="\'Apple SD Gothic Neo\',\'Noto Sans KR\',\'Malgun Gothic\',sans-serif">')
a(f'<rect x="-3.6" y="-2.7" width="{VB[2]}" height="{VB[3]}" fill="#ffffff"/>')
a('<text x="0" y="-1.75" font-size="0.66" font-weight="700" fill="#2b2622">바디·스킨케어 매장 평면도 (3안)</text>')
a('<text x="9.4" y="-1.75" font-size="0.4" fill="#7a7068">2층 501.41㎡(건축물대장, 약 152평). 건물 형태는 건축물현황도 배치도에서 읽은 가정값이고 약 39.3m × 13.7m다. 2층 계단·승강기·기둥·창 위치는 실측 후 반영한다.</text>')

CUR = 'fill="none" stroke="#b08d57" stroke-width="0.07" stroke-dasharray="0.18 0.12"'
CUR2 = 'fill="none" stroke="#c9b08a" stroke-width="0.05" stroke-dasharray="0.08 0.14"'
FUR = 'fill="#fff" stroke="#8a7d70" stroke-width="0.045"'
SOFT = 'fill="#e9e1d6" stroke="#8a7d70" stroke-width="0.035"'
DSP = 'fill="#f3d9a8" stroke="#a9812f" stroke-width="0.045"'
OFF = 'fill="#fff" stroke="#8a7d5a" stroke-width="0.045"'

a('<defs>')
# 2인실. 안쪽 벽이 y=0, 문 있는 벽이 y=4.6. 왼쪽 1.8m가 탈의 구역이고 문이 그 안으로 열린다.
# 4호실은 폭 7.0m(놓인 자리 깊이가 7.1m), 1~3호실은 왼쪽 블록 24m를 셋으로 나눠 폭 8.0m다.
def room(rid, w, beds):
    b1, b2 = beds
    mid = (b1 + 0.8 + b2) / 2          # 두 베드 사이 한가운데: 커튼과 세면대
    a(f'<g id="{rid}">')
    a(f'<rect x="0" y="0" width="{w}" height="4.6" fill="#efe3d3"/>')
    a('<rect x="0.06" y="0.06" width="1.74" height="4.48" fill="#f7ecd9"/>')
    a('<line x1="1.8" y1="0" x2="1.8" y2="3.2" stroke="#2b2622" stroke-width="0.09"/>')
    a('<g stroke="#8a7d70" stroke-width="0.05"><line x1="0.06" y1="1.6" x2="1.0" y2="1.6"/><line x1="0.06" y1="3.15" x2="1.0" y2="3.15"/></g>')
    a(f'<line x1="1.0" y1="0.1" x2="1.0" y2="1.55" {CUR}/>')
    a(f'<line x1="1.0" y1="1.65" x2="1.0" y2="3.1" {CUR}/>')
    a(f'<line x1="1.8" y1="3.2" x2="1.8" y2="4.54" {CUR}/>')
    # 락커는 상하 2단 한 칸(0.5 x 0.5). 두 칸을 나란히 두면 문이 열리면서 부딪친다.
    a(f'<rect x="0.1" y="3.25" width="0.5" height="0.5" {FUR}/>')
    a('<line x1="0.1" y1="3.5" x2="0.6" y2="3.5" stroke="#8a7d70" stroke-width="0.03"/>')
    a('<rect x="0.07" y="3.88" width="0.06" height="0.6" fill="#9db7c4"/>')
    for sy in (0.55, 2.1):
        a(f'<circle cx="0.45" cy="{sy}" r="0.17" {SOFT}/>')
    for bx in (b1, b2):
        a(f'<rect x="{bx}" y="0.8" width="0.8" height="2" rx="0.1" {FUR}/>')
        a(f'<rect x="{bx+0.1:.2f}" y="0.88" width="0.6" height="0.35" rx="0.08" {SOFT}/>')
        a(f'<circle cx="{bx+0.4:.2f}" cy="0.44" r="0.16" {SOFT}/>')
    a(f'<rect x="{mid-0.4:.2f}" y="0.12" width="0.8" height="0.48" rx="0.06" fill="#d6e4ea" stroke="#5f7f8c" stroke-width="0.045"/>')
    a(f'<circle cx="{mid:.2f}" cy="0.36" r="0.15" fill="#fff" stroke="#5f7f8c" stroke-width="0.035"/>')
    a(f'<line x1="{mid:.2f}" y1="0.6" x2="{mid:.2f}" y2="3.0" {CUR}/>')
    a(f'<line x1="1.8" y1="3.0" x2="{w-0.06}" y2="3.0" {CUR2}/>')
    a(f'<rect x="{mid-0.75:.2f}" y="1.5" width="0.4" height="0.5" rx="0.05" {SOFT}/>')
    a(f'<rect x="{mid+0.35:.2f}" y="1.5" width="0.4" height="0.5" rx="0.05" {SOFT}/>')
    a(f'<rect x="{w-2.0}" y="4.08" width="1.9" height="0.44" {FUR}/>')
    a(f'<rect x="{w-2.65:.2f}" y="4.08" width="0.5" height="0.44" rx="0.06" fill="#cfcfcf" stroke="#888" stroke-width="0.04"/>')
    a('<path d="M1.35 4.6 L1.35 3.7 A0.9 0.9 0 0 0 0.45 4.6" fill="none" stroke="#2b2622" stroke-width="0.045"/>')
    a('</g>')
room('room', 7.0, (2.7, 5.3))      # 탈의 1.8 + 0.9 + 베드 + 1.8 + 베드 + 0.9
room('room8', 8.0, (3.0, 5.9))     # 탈의 1.8 + 1.2 + 베드 + 2.1 + 베드 + 1.3
a('<g id="cam"><path d="M0 0 L-0.6 -1.15 L0.6 -1.15 Z" fill="#e2622b" opacity="0.28"/><circle r="0.36" fill="#e2622b"/></g>')
a('</defs>')

# 바닥
a(f'<rect x="0" y="0" width="{LW}" height="{LH}" fill="#f6f1ea"/>')
a(f'<rect x="{RX}" y="{RY}" width="{RW}" height="{RH}" fill="#f6f1ea"/>')
a(f'<rect x="0" y="{RD}" width="21" height="{C1-RD}" fill="#efe9df"/>')            # 복도(왼쪽)
a(f'<rect x="21" y="{RD}" width="3" height="{C2-RD}" fill="#efe9df"/>')            # 복도 꺾이는 곳
a(f'<rect x="{RX}" y="{R1}" width="{RW}" height="{C2-R1}" fill="#efe9df"/>')       # 복도(오른쪽)
a(f'<rect x="24" y="{RY}" width="4" height="{RD}" fill="#f1e1e3"/>')               # 파우더룸
a(f'<rect x="28" y="{RY}" width="7.5" height="{RD}" fill="#e8e6d8"/>')             # 사무실(회의·상담 테이블 포함)
a(f'<rect x="35.5" y="{RY}" width="3.8" height="{RD}" fill="#e4e4e4"/>')           # 비품·린넨 수거
a(f'<rect x="0" y="{C1}" width="4" height="{LH-C1}" fill="#e4e4e4"/>')             # 린넨·재고
a(f'<rect x="4" y="{C1}" width="3.5" height="{LH-C1}" fill="#dfe8ee"/>')           # 직원휴게실
a('<rect x="32.2" y="10.0" width="2.5" height="5.0" fill="#fbf1dc"/>')             # 데스크·화장품
a('<rect x="7.5" y="6.7" width="1.9" height="6.2" fill="#e6ecdf"/>')               # 발마사지

# 2인실: 위쪽 3개, 오른쪽 아래 1개(90도 돌려 놓았다. 문은 서쪽 벽 위쪽)
for x in (0, 8, 16):
    a(f'<use href="#room8" transform="translate({x},0)"/>')
a(f'<use href="#room" transform="translate({W},{C2}) rotate(90)"/>')

# 파우더룸, 사무실, 비품·수거
a('<rect x="24.3" y="1.65" width="3.4" height="0.5" fill="#fff" stroke="#a06f78" stroke-width="0.045"/>')
for cx in (24.8, 25.6, 26.4, 27.2):
    a(f'<circle cx="{cx}" cy="2.5" r="0.2" fill="#fff" stroke="#a06f78" stroke-width="0.035"/>')
a(f'<g {FUR}>')
a('<rect x="28.15" y="1.65" width="2.7" height="0.45"/>')
a('<circle cx="29.5" cy="3.7" r="0.5" fill="#e9e1d6"/><circle cx="28.72" cy="3.7" r="0.26"/><circle cx="30.28" cy="3.7" r="0.26"/><circle cx="29.5" cy="2.92" r="0.26"/>')
a('</g>')
a(f'<g {OFF}>')
for dx in (31.2, 32.65, 34.0):
    a(f'<rect x="{dx}" y="1.65" width="1.35" height="0.7"/><circle cx="{dx+0.67}" cy="2.75" r="0.22" fill="#e9e1d6"/>')
a('<rect x="34.95" y="3.4" width="0.45" height="2.5"/>')
a('</g>')
a('<g fill="#fff" stroke="#888" stroke-width="0.045"><rect x="35.7" y="1.65" width="2.6" height="0.5"/><rect x="38.7" y="1.65" width="0.5" height="3.2"/><rect x="35.65" y="4.9" width="0.6" height="0.6" rx="0.08" fill="#cfcfcf"/><rect x="35.65" y="4.2" width="0.6" height="0.6" rx="0.08" fill="#cfcfcf"/></g>')

# 린넨·재고, 직원휴게실 (왼쪽 아래)
a('<g fill="#fff" stroke="#888" stroke-width="0.045"><rect x="0.1" y="7.6" width="0.5" height="5.3"/><rect x="0.8" y="13.1" width="3.0" height="0.5"/><rect x="3.38" y="7.7" width="0.5" height="2.0"/></g>')
a('<g fill="#cfcfcf" stroke="#888" stroke-width="0.04"><rect x="2.7" y="6.55" width="0.55" height="0.55" rx="0.08"/><rect x="3.33" y="6.55" width="0.55" height="0.55" rx="0.08"/></g>')
a('<g fill="#fff" stroke="#5f7f8c" stroke-width="0.045"><rect x="5.1" y="9.7" width="1.3" height="0.9" rx="0.1"/><rect x="4.2" y="13.05" width="2.4" height="0.5" rx="0.12"/><rect x="6.9" y="7.7" width="0.5" height="2.0"/><rect x="4.12" y="7.7" width="0.55" height="2.2"/></g>')

# 발마사지: 암체어 5 + 바닥 발마사지기. 직원휴게실 벽을 등지고 홀을 본다.
for i in range(5):
    y = 6.95 + 1.2 * i
    a(f'<rect x="7.62" y="{y:.2f}" width="0.85" height="0.85" rx="0.2" fill="#fff" stroke="#6f8560" stroke-width="0.045"/>')
    a(f'<rect x="8.68" y="{y+0.15:.2f}" width="0.45" height="0.55" rx="0.08" fill="#cfdcc4" stroke="#6f8560" stroke-width="0.035"/>')
    if i < 4:
        a(f'<circle cx="8.05" cy="{y+1.02:.2f}" r="0.15" {SOFT}/>')

# 홀: 담소 좌석, 벤치, 인허가 진열대, 출입문 옆 거울
a(f'<g {FUR}>')
for cx, cy in ((11.8, 9.4), (16.3, 10.1)):   # 4인 좌석 2조
    a(f'<rect x="{cx-0.4:.2f}" y="{cy-1.3:.2f}" width="0.8" height="0.75" rx="0.2"/><rect x="{cx-0.4:.2f}" y="{cy+0.55:.2f}" width="0.8" height="0.75" rx="0.2"/>')
    a(f'<rect x="{cx-1.3:.2f}" y="{cy-0.4:.2f}" width="0.75" height="0.8" rx="0.2"/><rect x="{cx+0.55:.2f}" y="{cy-0.4:.2f}" width="0.75" height="0.8" rx="0.2"/>')
    a(f'<circle cx="{cx}" cy="{cy}" r="0.45" fill="#e9e1d6"/>')
for tx in (9.9, 12.6):                       # 창가 라운지 체어 2개 + 사이드 테이블, 2조
    a(f'<rect x="{tx}" y="12.7" width="0.8" height="0.8" rx="0.25"/><rect x="{tx+1.5:.2f}" y="12.7" width="0.8" height="0.8" rx="0.25"/><circle cx="{tx+1.15:.2f}" cy="13.1" r="0.22" fill="#e9e1d6"/>')
# 출입문에서 화장품 쇼케이스까지는 소파 뒤와 창가 좌석 사이(폭 1.8m)로 지나간다
a('<rect x="9.6" y="6.5" width="2.2" height="0.6" rx="0.14"/><rect x="14.1" y="6.5" width="4.0" height="0.6" rx="0.14"/>')   # 복도 벽을 따라 놓은 벽면 소파
a('<circle cx="15.4" cy="7.5" r="0.27" fill="#e9e1d6"/><circle cx="16.8" cy="7.5" r="0.27" fill="#e9e1d6"/>')
a('</g>')
a(f'<rect x="18.3" y="6.47" width="2.4" height="0.32" {DSP}/>')
a('<rect x="21.0" y="7.97" width="4.0" height="0.16" fill="#8d4b32"/>')            # 브랜드 월: 출입문 정면, 폭 4m
a('<line x1="23.0" y1="8.3" x2="23.0" y2="12.6" stroke="#8d4b32" stroke-width="0.04" stroke-dasharray="0.12 0.16"/>')
a('<rect x="21.0" y="13.56" width="0.9" height="0.07" fill="#9db7c4"/>')

# 라운지(TV는 복도 벽), 커피바(도로 쪽 벽)
a('<rect x="29.45" y="7.97" width="1.9" height="0.14" fill="#2b2622"/>')
# 안내데스크: 출입문에서 정면 오른쪽, 브랜드 월 바로 옆(막은 개구부 자리). 직원은 벽을 등지고 선다
a(f'<rect x="25.2" y="8.8" width="3.2" height="0.6" rx="0.1" {DSP}/><circle cx="26.8" cy="8.35" r="0.2" {SOFT}/>')
# 호출 안내 화면 2대: 복도 개구부 옆 벽 위쪽. "몇 번 손님 몇 번 실로"를 띄운다
a('<rect x="10.7" y="6.47" width="1.0" height="0.1" fill="#3f6b7a"/><rect x="28.3" y="7.97" width="1.0" height="0.1" fill="#3f6b7a"/>')
a(f'<g {FUR}>')
a('<rect x="29.2" y="11.4" width="2.4" height="0.9" rx="0.22"/>')
a('<rect x="28.1" y="9.9" width="0.8" height="0.8" rx="0.25"/><rect x="28.1" y="10.95" width="0.8" height="0.8" rx="0.25"/>')
for tx in (24.5, 27.3, 30.1):                 # 창가 라운지 체어 2개 + 사이드 테이블, 3조
    a(f'<rect x="{tx}" y="14.1" width="0.8" height="0.8" rx="0.25"/><rect x="{tx+1.5:.2f}" y="14.1" width="0.8" height="0.8" rx="0.25"/><circle cx="{tx+1.15:.2f}" cy="14.5" r="0.22" fill="#e9e1d6"/>')
a('<rect x="29.8" y="10.0" width="1.2" height="0.6" rx="0.12" fill="#e9e1d6"/>')
a('</g>')
a('<rect x="16.2" y="13.02" width="4.0" height="0.6" rx="0.06" fill="#d9c2a3" stroke="#8a6a3f" stroke-width="0.045"/>')

# 데스크·쇼케이스 카운터(4호실 서쪽 바깥 벽), 뒤쪽 조명 진열 벽
a(f'<rect x="34.32" y="10.5" width="0.38" height="4.4" {DSP}/>')
a(f'<rect x="32.82" y="10.4" width="0.6" height="4.6" {DSP}/>')
a(f'<circle cx="33.87" cy="11.4" r="0.2" {SOFT}/>')
a(f'<circle cx="32.4" cy="11.4" r="0.2" {SOFT}/><circle cx="32.4" cy="12.4" r="0.2" {SOFT}/>')

# 벽
a('<g fill="none" stroke="#2b2622" stroke-linecap="square" stroke-linejoin="miter">')
a(f'<path d="M0 0 H{LW} V{RY} H{W} V{RB} H{RX} V{LH} H0 Z" stroke-width="0.22"/>')
a('<g stroke-width="0.13">')
for l in ((0,RD,24,RD),(8,0,8,RD),(16,0,16,RD),(24,0,24,R1),
          (0,C1,21,C1),(21,C1,21,C2),(21,C2,W,C2),(4,C1,4,LH),(7.5,C1,7.5,LH),
          (24,R1,W,R1),(28,RY,28,R1),(35.5,RY,35.5,R1),(34.7,C2,34.7,RB)):
    a('<line x1="%s" y1="%s" x2="%s" y2="%s"/>' % l)
a('</g></g>')

# 문과 개구부 (벽을 바닥색으로 덮는다)
a('<g stroke="#f6f1ea" stroke-width="0.2">')
for l in ((0.45,RD,1.35,RD),(8.45,RD,9.35,RD),(16.45,RD,17.35,RD),
          (24.6,R1,25.5,R1),(31.3,R1,32.2,R1),(36.5,R1,37.4,R1),
          (1.5,C1,2.4,C1),(5.3,C1,6.2,C1),(12.0,C1,13.8,C1),
          (32.6,C2,34.4,C2),(34.7,8.35,34.7,9.25)):
    a('<line x1="%s" y1="%s" x2="%s" y2="%s"/>' % l)
a('</g>')
a(f'<line x1="22.1" y1="{LH}" x2="23.9" y2="{LH}" stroke="#ffffff" stroke-width="0.3"/>')
a(f'<line x1="{W}" y1="6.45" x2="{W}" y2="7.55" stroke="#ffffff" stroke-width="0.3"/>')
a('<g fill="none" stroke="#2b2622" stroke-width="0.045">')
for d in ('M25.5 6.1 L25.5 5.2 A0.9 0.9 0 0 0 24.6 6.1',
          'M32.2 6.1 L32.2 5.2 A0.9 0.9 0 0 0 31.3 6.1', 'M37.4 6.1 L37.4 5.2 A0.9 0.9 0 0 0 36.5 6.1',
          'M1.5 6.4 L1.5 7.3 A0.9 0.9 0 0 0 2.4 6.4', 'M5.3 6.4 L5.3 7.3 A0.9 0.9 0 0 0 6.2 6.4',
          'M22.1 13.7 L22.1 12.8 A0.9 0.9 0 0 1 23.0 13.7', 'M23.9 13.7 L23.9 12.8 A0.9 0.9 0 0 0 23.0 13.7'):
    a(f'<path d="{d}"/>')
a('</g>')

# 이름
a('<g font-size="0.46" font-weight="700" fill="#2b2622" text-anchor="middle">')
for x, y, t in ((4.1,3.75,'2인실 1'),(12.1,3.75,'2인실 2'),(20.1,3.75,'2인실 3'),
                (26.0,4.3,'파우더룸'),(33.4,4.4,'사무실'),(37.45,3.6,'비품·수거'),
                (2.0,10.6,'린넨·재고'),(5.75,11.6,'직원휴게실'),(12.2,7.6,'셀프 발마사지 5석'),
                (30.4,12.9,'TV 라운지'),(23.0,14.75,'출입구'),
                (10.0,5.65,'관리실 앞 복도'),(31.0,7.15,'복도')):
    a(f'<text x="{x}" y="{y}">{t}</text>')
a(f'<text x="35.62" y="11.9" transform="rotate(90 35.62 11.9)">2인실 4</text>')
a('<text x="33.45" y="9.85" font-size="0.4">화장품</text>')
a('</g>')
a('<g font-size="0.34" fill="#5a4f45" text-anchor="middle">')
for x, y, t in ((30.4,8.55,'TV'),(28.8,8.5,'호출 화면'),(18.2,12.8,'커피바'),(26.8,9.75,'안내데스크'),(27.9,13.85,'창가 좌석'),(29.5,4.85,'회의·상담'),(19.5,7.2,'인허가 진열대'),(23.0,8.75,'브랜드 월 (폭 4m)'),
                (13.0,12.35,'라운지 좌석'),(16.1,6.92,'벽면 소파'),(10.7,6.92,'벽면 소파'),(21.45,13.35,'거울'),
                (5.35,2.3,'커튼'),(0.5,1.3,'탈의'),(0.5,2.85,'탈의'),(26.0,3.3,'화장대 4석'),
                (12.9,6.15,'↕'),(33.5,7.65,'↕')):
    a(f'<text x="{x}" y="{y}">{t}</text>')
a('</g>')

# 바깥 표시
a('<g font-size="0.36" fill="#7a7068">')
a('<text x="21.6" y="14.75" text-anchor="end">2층 계단·승강기 위치는 확인 필요 ▶</text>')
a('<text x="-0.5" y="9.8" text-anchor="end">계룡로(40m) 쪽</text>')
a('<text x="-0.5" y="10.3" text-anchor="end">1층 주출입구</text>')
a(f'<text x="{W+0.5}" y="6.95">◀ 부출입구 쪽</text>')
a(f'<text x="{W+0.5}" y="7.5">직원·납품(가정)</text>')
a('<text x="5" y="14.45" text-anchor="middle">아래쪽: 8m 도로 쪽</text>')
a('<text x="31" y="1.05" text-anchor="middle">위쪽: 인접 대지 쪽</text>')
a('<g transform="translate(41.6,-0.9)"><circle r="0.55" fill="none" stroke="#9a8f85" stroke-width="0.04"/><path d="M-0.3 0.3 L0.42 -0.42 M0.42 -0.42 L0.1 -0.34 M0.42 -0.42 L0.34 -0.1" fill="none" stroke="#5a4f45" stroke-width="0.06"/><text x="0.62" y="-0.5" font-size="0.34">N</text></g>')
a('</g>')

# 카메라 (1차 5개)
cams = ((23.0,12.9,0),(30.4,13.2,0),(10.3,11.4,308),(10.4,4.0,38),(31.2,12.6,80))
a('<g id="cameras">')
for x, y, h in cams:
    a(f'<use href="#cam" transform="translate({x},{y}) rotate({h})"/>')
a('<g font-size="0.4" font-weight="700" fill="#fff" text-anchor="middle">')
for i, (x, y, h) in enumerate(cams, 1):
    a(f'<text x="{x}" y="{y+0.14:.2f}">{i}</text>')
a('</g></g>')

# 치수선
a('<g stroke="#9a8f85" stroke-width="0.035" fill="#7a7068" font-size="0.36" text-anchor="middle">')
a(f'<line x1="0" y1="-0.45" x2="{W}" y2="-0.45"/>')
for x in (0, 8, 16, 24, 28, 35.5, W):
    a(f'<line x1="{x}" y1="-0.63" x2="{x}" y2="-0.27"/>')
for x, t in ((4,'8m'),(12,'8m'),(20,'8m'),(26,'4m'),(31.75,'7.5m'),(37.4,'3.8m')):
    a(f'<text x="{x}" y="-0.62" stroke="none">{t}</text>')
a(f'<line x1="0" y1="16.1" x2="{W}" y2="16.1"/>')
for x in (0, 24, W):
    a(f'<line x1="{x}" y1="15.92" x2="{x}" y2="16.28"/>')
for x, t in ((12,'24.0m (기존 블록)'),(31.65,'15.3m (증축 블록)')):
    a(f'<text x="{x}" y="16.65" stroke="none">{t}</text>')
a('<line x1="-0.45" y1="0" x2="-0.45" y2="13.7"/>')
for y in (0, RD, C1, LH):
    a(f'<line x1="-0.63" y1="{y}" x2="-0.27" y2="{y}"/>')
for y, t in ((2.4,'4.6m'),(5.6,'1.8m'),(8.3,'7.3m')):
    a(f'<text x="-1.25" y="{y}" stroke="none">{t}</text>')
a(f'<line x1="{W+0.45}" y1="{RY}" x2="{W+0.45}" y2="{RB}"/>')
for y in (RY, R1, C2, RB):
    a(f'<line x1="{W+0.27}" y1="{y}" x2="{W+0.63}" y2="{y}"/>')
for y, t in ((3.9,'4.6m'),(11.6,'7.1m')):
    a(f'<text x="{W+1.25}" y="{y}" stroke="none">{t}</text>')
a('</g>')

# 범례
a('<g id="legend" font-size="0.36" fill="#5a4f45">')
a('<circle cx="0.3" cy="17.6" r="0.26" fill="#e2622b"/>')
a('<text x="0.8" y="17.73">카메라 1 입구에서 홀 · 2 라운지에서 TV 벽 · 3 발마사지 · 4 2인실 · 5 데스크·화장품</text>')
a(f'<line x1="0.05" y1="18.4" x2="0.6" y2="18.4" {CUR}/>')
a('<text x="0.8" y="18.53">천장형 커튼</text>')
a(f'<rect x="3.6" y="18.18" width="0.5" height="0.4" {DSP}/>')
a('<text x="4.3" y="18.53">데스크·조명 진열</text>')
a('<rect x="8.0" y="18.18" width="0.5" height="0.4" fill="#f7ecd9" stroke="#b08d57" stroke-width="0.035"/>')
a('<text x="8.7" y="18.53">탈의·락커 구역 (문이 이 안으로 열린다)</text>')
a('<text x="16.6" y="18.53">↕ 홀과 복도를 잇는 개구부</text>')
a('</g>')
a('</svg>')
open(__file__.replace('make_plan.py', 'floor-plan-draft.svg'), 'w', encoding='utf-8').write('\n'.join(o) + '\n')
