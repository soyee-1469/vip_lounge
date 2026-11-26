"""매장 평면도 2안을 SVG로 만든다. 단위는 미터, 전체 28 x 18.7 (가로:세로 3:2, 3층 523.2㎡ 기준).

1안(18 x 12)은 _old/ 폴더에 있다. 좌표 원점은 왼쪽 위, 위가 매장 안쪽, 아래가 출입구다.
앱(src/lib/views.ts)이 이 파일이 만든 SVG를 줄 단위로 읽으므로 요소를 한 줄에 하나씩 쓴다.
"""
W, H = 28, 18.7
RD = 4.6            # 2인실 깊이
CY = 6.4            # 룸 앞 복도와 홀을 나누는 벽
BY = 14.1           # 아래쪽 블록 윗벽
o = []
a = o.append
VB = (-1.6, -2.4, 32.4, 25.4)
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VB[0]} {VB[1]} {VB[2]} {VB[3]}" width="1620" height="1270" font-family="\'Apple SD Gothic Neo\',\'Noto Sans KR\',\'Malgun Gothic\',sans-serif">')
a(f'<rect x="-1.6" y="-2.4" width="{VB[2]}" height="{VB[3]}" fill="#ffffff"/>')
a('<text x="0" y="-1.5" font-size="0.62" font-weight="700" fill="#2b2622">바디·스킨케어 매장 평면도 (2안)</text>')
a('<text x="8.6" y="-1.5" font-size="0.38" fill="#7a7068">3층 523.2㎡(약 158평) 기준. 28m × 18.7m는 가로:세로 3:2로 잡은 가정값이고 위가 매장 안쪽이다. 기둥·승강기·계단·창 위치는 실측 후 반영한다.</text>')

CUR = 'fill="none" stroke="#b08d57" stroke-width="0.07" stroke-dasharray="0.18 0.12"'
CUR2 = 'fill="none" stroke="#c9b08a" stroke-width="0.05" stroke-dasharray="0.08 0.14"'
FUR = 'fill="#fff" stroke="#8a7d70" stroke-width="0.045"'
SOFT = 'fill="#e9e1d6" stroke="#8a7d70" stroke-width="0.035"'
DSP = 'fill="#f3d9a8" stroke="#a9812f" stroke-width="0.045"'

a('<defs>')
# 2인실 (7 x 4.6). 안쪽 벽이 y=0, 문 있는 벽이 y=4.6. 왼쪽 1.8m가 탈의 구역이고 문이 그 안으로 열린다.
a('<g id="room">')
a('<rect x="0.06" y="0.06" width="1.74" height="4.48" fill="#f7ecd9"/>')
a('<line x1="1.8" y1="0" x2="1.8" y2="3.2" stroke="#2b2622" stroke-width="0.09"/>')
a('<g stroke="#8a7d70" stroke-width="0.05"><line x1="0.06" y1="1.6" x2="1.0" y2="1.6"/><line x1="0.06" y1="3.15" x2="1.0" y2="3.15"/></g>')
a(f'<line x1="1.0" y1="0.1" x2="1.0" y2="1.55" {CUR}/>')
a(f'<line x1="1.0" y1="1.65" x2="1.0" y2="3.1" {CUR}/>')
a(f'<line x1="1.8" y1="3.2" x2="1.8" y2="4.54" {CUR}/>')
# 락커는 상하 2단 한 칸(0.5 x 0.5). 두 칸을 나란히 두면 문이 열리면서 부딪친다.
a(f'<rect x="0.1" y="3.25" width="0.5" height="0.5" {FUR}/>')
a('<line x1="0.1" y1="3.5" x2="0.6" y2="3.5" stroke="#8a7d70" stroke-width="0.03"/>')
# 전신 거울 (벽 부착)
a('<rect x="0.07" y="3.88" width="0.06" height="0.6" fill="#9db7c4"/>')
for sy in (0.55, 2.1):
    a(f'<circle cx="0.45" cy="{sy}" r="0.17" {SOFT}/>')
for bx in (2.7, 5.3):
    a(f'<rect x="{bx}" y="0.8" width="0.8" height="2" rx="0.1" {FUR}/>')
    a(f'<rect x="{bx+0.1}" y="0.88" width="0.6" height="0.35" rx="0.08" {SOFT}/>')
    a(f'<circle cx="{bx+0.4}" cy="0.44" r="0.16" {SOFT}/>')
a('<rect x="4.0" y="0.12" width="0.8" height="0.48" rx="0.06" fill="#d6e4ea" stroke="#5f7f8c" stroke-width="0.045"/>')
a('<circle cx="4.4" cy="0.36" r="0.15" fill="#fff" stroke="#5f7f8c" stroke-width="0.035"/>')
a(f'<line x1="4.4" y1="0.6" x2="4.4" y2="3.0" {CUR}/>')
a(f'<line x1="1.8" y1="3.0" x2="6.94" y2="3.0" {CUR2}/>')
a(f'<rect x="3.65" y="1.5" width="0.4" height="0.5" rx="0.05" {SOFT}/>')
a(f'<rect x="4.75" y="1.5" width="0.4" height="0.5" rx="0.05" {SOFT}/>')
a(f'<rect x="5.0" y="4.08" width="1.9" height="0.44" {FUR}/>')
a('<rect x="4.35" y="4.08" width="0.5" height="0.44" rx="0.06" fill="#cfcfcf" stroke="#888" stroke-width="0.04"/>')
a('<path d="M1.35 4.6 L1.35 3.7 A0.9 0.9 0 0 0 0.45 4.6" fill="none" stroke="#2b2622" stroke-width="0.045"/>')
a('</g>')
a('<g id="cam"><path d="M0 0 L-0.6 -1.15 L0.6 -1.15 Z" fill="#e2622b" opacity="0.28"/><circle r="0.36" fill="#e2622b"/></g>')
a('</defs>')

# 바닥
a(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#f6f1ea"/>')
a(f'<rect x="0" y="{RD}" width="{W}" height="{CY-RD}" fill="#efe9df"/>')                 # 룸 앞 복도
a(f'<rect x="18" y="0" width="3" height="{RD}" fill="#e3e9ee"/>')                          # 화장실
a(f'<rect x="14" y="0" width="4" height="{RD}" fill="#f1e1e3"/>')                          # 파우더룸
for x in (0, 7, 21):
    a(f'<rect x="{x}" y="0" width="7" height="{RD}" fill="#efe3d3"/>')
a(f'<rect x="21" y="{BY}" width="7" height="{RD}" fill="#efe3d3"/>')
a(f'<rect x="0" y="{BY}" width="5.5" height="{RD}" fill="#e4e4e4"/>')                     # 린넨·재고
a(f'<rect x="5.5" y="{BY}" width="4.5" height="{RD}" fill="#dfe8ee"/>')                   # 직원휴게실
a('<rect x="1.9" y="12.4" width="6.1" height="1.7" fill="#e6ecdf"/>')                     # 발마사지
a('<rect x="19.2" y="11.5" width="6.6" height="2.6" fill="#fbf1dc"/>')                    # 데스크·화장품
a('<rect x="19.2" y="14.1" width="1.8" height="3.3" fill="#fbf1dc"/>')

# 2인실
for x in (0, 7, 21):
    a(f'<use href="#room" transform="translate({x},0)"/>')
a(f'<use href="#room" transform="translate({W},{H}) scale(-1,-1)"/>')

# 화장실, 파우더룸
a('<g fill="#fff" stroke="#5f7f8c" stroke-width="0.045">')
a('<rect x="18.5" y="0.25" width="0.5" height="0.7" rx="0.2"/><rect x="20.0" y="0.25" width="0.5" height="0.7" rx="0.2"/>')
a('<rect x="18.12" y="2.5" width="0.5" height="1.5" rx="0.06"/>')
a('</g>')
a('<g stroke="#8a7d70" stroke-width="0.05"><line x1="19.5" y1="0.06" x2="19.5" y2="1.9"/><line x1="18.06" y1="1.9" x2="18.6" y2="1.9"/><line x1="19.4" y1="1.9" x2="20.1" y2="1.9"/><line x1="20.9" y1="1.9" x2="20.94" y2="1.9"/></g>')
a('<rect x="14.3" y="0.15" width="3.4" height="0.5" fill="#fff" stroke="#a06f78" stroke-width="0.045"/>')
for cx in (14.8, 15.6, 16.4, 17.2):
    a(f'<circle cx="{cx}" cy="1.0" r="0.2" fill="#fff" stroke="#a06f78" stroke-width="0.035"/>')

# 홀: 벤치, 담소 좌석, 상담석, 대표 제품
a(f'<g {FUR}>')
a('<rect x="11.2" y="6.52" width="2.0" height="0.5" rx="0.12"/><rect x="14.8" y="6.52" width="2.0" height="0.5" rx="0.12"/>')
a('<rect x="3.2" y="8.0" width="0.8" height="0.75" rx="0.2"/><rect x="3.2" y="9.9" width="0.8" height="0.75" rx="0.2"/>')
a('<rect x="2.25" y="8.9" width="0.75" height="0.8" rx="0.2"/><rect x="4.2" y="8.9" width="0.75" height="0.8" rx="0.2"/>')
a('<circle cx="3.6" cy="9.3" r="0.45" fill="#e9e1d6"/>')
a('<circle cx="8.0" cy="10.6" r="0.5" fill="#e9e1d6"/><circle cx="7.2" cy="10.6" r="0.26"/><circle cx="8.8" cy="10.6" r="0.26"/><circle cx="8.0" cy="9.8" r="0.26"/>')
a('</g>')
a('<circle cx="14" cy="11.4" r="0.62" fill="#3a332d"/><circle cx="14" cy="11.4" r="0.3" fill="#f6f1ea"/>')

# 발마사지: 암체어 5 + 바닥 발마사지기. 창고 벽을 등지고 홀을 본다.
for i in range(5):
    x = 2.1 + 1.2 * i
    a(f'<rect x="{x:.2f}" y="13.2" width="0.85" height="0.85" rx="0.2" fill="#fff" stroke="#6f8560" stroke-width="0.045"/>')
    a(f'<rect x="{x+0.15:.2f}" y="12.58" width="0.55" height="0.45" rx="0.08" fill="#cfdcc4" stroke="#6f8560" stroke-width="0.035"/>')
    if i < 4:
        a(f'<circle cx="{x+1.02:.2f}" cy="13.62" r="0.15" {SOFT}/>')

# 라운지, TV, 커피바
a(f'<g {FUR}>')
a('<rect x="23.4" y="8.7" width="0.9" height="2.4" rx="0.22"/>')
a('<rect x="24.9" y="7.75" width="0.8" height="0.8" rx="0.25"/><rect x="24.9" y="11.2" width="0.8" height="0.8" rx="0.25"/>')
a('<rect x="25.1" y="9.3" width="0.6" height="1.2" rx="0.12" fill="#e9e1d6"/>')
a('</g>')
a('<rect x="27.76" y="8.95" width="0.14" height="1.9" fill="#2b2622"/>')
a('<rect x="24.4" y="6.47" width="3.2" height="0.6" rx="0.06" fill="#d9c2a3" stroke="#8a6a3f" stroke-width="0.045"/>')

# 데스크와 쇼케이스 카운터(ㄱ자 하나), 뒤쪽 조명 진열 벽
a(f'<path d="M19.4 12.2 H25.6 V12.8 H20.0 V17.2 H19.4 Z" {DSP}/>')
a(f'<rect x="21.1" y="13.7" width="5.2" height="0.36" {DSP}/>')
a(f'<circle cx="20.5" cy="15.2" r="0.2" {SOFT}/>')
a(f'<circle cx="22.4" cy="11.85" r="0.2" {SOFT}/><circle cx="23.4" cy="11.85" r="0.2" {SOFT}/>')
# 출입구 옆 전신 거울 (벽 부착)
a('<rect x="10.07" y="17.2" width="0.07" height="0.9" fill="#9db7c4"/>')
# 인허가 진열대
a(f'<rect x="10.08" y="14.5" width="0.36" height="2.4" {DSP}/>')

# 린넨·재고, 직원휴게실
a('<g fill="#fff" stroke="#888" stroke-width="0.045"><rect x="0.1" y="15.2" width="0.5" height="3.4"/><rect x="0.8" y="18.1" width="4.5" height="0.5"/><rect x="3.3" y="14.25" width="2.0" height="0.55"/></g>')
a('<g fill="#cfcfcf" stroke="#888" stroke-width="0.04"><rect x="1.7" y="14.25" width="0.6" height="0.6" rx="0.08"/><rect x="2.4" y="14.25" width="0.6" height="0.6" rx="0.08"/></g>')
a('<g fill="#fff" stroke="#5f7f8c" stroke-width="0.045"><rect x="7.0" y="16.0" width="1.4" height="0.9" rx="0.1"/><rect x="5.7" y="18.05" width="2.4" height="0.5" rx="0.12"/><rect x="9.4" y="15.3" width="0.5" height="2.0"/><rect x="6.0" y="14.25" width="2.2" height="0.55"/></g>')

# 벽
a('<g fill="none" stroke="#2b2622" stroke-linecap="square">')
a(f'<rect x="0" y="0" width="{W}" height="{H}" stroke-width="0.22"/>')
a('<g stroke-width="0.13">')
for l in ((0,RD,W,RD),(7,0,7,RD),(14,0,14,RD),(18,0,18,RD),(21,0,21,RD),(0,CY,W,CY),
          (0,BY,10,BY),(21,BY,W,BY),(5.5,BY,5.5,H),(10,BY,10,H),(21,BY,21,H)):
    a('<line x1="%s" y1="%s" x2="%s" y2="%s"/>' % l)
a('</g></g>')

# 문과 개구부 (벽을 바닥색으로 덮는다)
a('<g stroke="#f6f1ea" stroke-width="0.2">')
for l in ((19.9,RD,20.8,RD),(15.5,RD,16.4,RD),(0.45,RD,1.35,RD),(7.45,RD,8.35,RD),(21.45,RD,22.35,RD),
          (3.0,CY,4.5,CY),(9.0,CY,10.8,CY),(17.2,CY,19.0,CY),
          (0.5,BY,1.4,BY),(8.6,BY,9.5,BY),(26.65,BY,27.55,BY),(5.5,15.0,5.5,15.9)):
    a('<line x1="%s" y1="%s" x2="%s" y2="%s"/>' % l)
a('</g>')
a(f'<line x1="13.1" y1="{H}" x2="14.9" y2="{H}" stroke="#ffffff" stroke-width="0.3"/>')
a('<g fill="none" stroke="#2b2622" stroke-width="0.045">')
for d in ('M20.8 4.6 L20.8 3.7 A0.9 0.9 0 0 0 19.9 4.6', 'M16.4 4.6 L16.4 3.7 A0.9 0.9 0 0 0 15.5 4.6',
          'M0.5 14.1 L0.5 15 A0.9 0.9 0 0 0 1.4 14.1', 'M9.5 14.1 L9.5 15 A0.9 0.9 0 0 1 8.6 14.1',
          'M5.5 15 L4.6 15 A0.9 0.9 0 0 0 5.5 15.9',
          f'M13.1 {H} L13.1 {H-0.9} A0.9 0.9 0 0 1 14 {H}', f'M14.9 {H} L14.9 {H-0.9} A0.9 0.9 0 0 0 14 {H}'):
    a(f'<path d="{d}"/>')
a('</g>')

# 이름
a('<g font-size="0.46" font-weight="700" fill="#2b2622" text-anchor="middle">')
for x, y, t in ((3.6,3.75,'2인실 1'),(10.6,3.75,'2인실 2'),(24.6,3.75,'2인실 3'),(24.4,15.3,'2인실 4'),
                (5.0,12.1,'셀프 발마사지 5석'),(16.0,2.6,'파우더룸'),(19.75,3.0,'화장실'),
                (3.0,16.6,'린넨·재고 창고'),(7.7,17.6,'직원휴게실'),(26.75,8.45,'라운지'),
                (22.9,13.42,'데스크·화장품'),(14,19.75,'출입구'),(11.5,5.65,'관리실 앞 복도')):
    a(f'<text x="{x}" y="{y}">{t}</text>')
a('</g>')
a('<g font-size="0.34" fill="#5a4f45" text-anchor="middle">')
for x, y, t in ((27.2,10.0,'TV'),(26.0,6.9,'커피바'),(24.6,12.62,'쇼케이스 카운터'),(11.5,15.8,'인허가 진열대'),(10.75,17.75,'거울'),
                (18.55,15.0,'접수'),(24.3,11.95,'테스터'),(14,12.6,'대표 제품'),(3.6,11.2,'담소 좌석'),
                (12.2,7.5,'벤치'),(15.8,7.5,'벤치'),(8.0,11.65,'상담석'),(14,6.95,'브랜드 월'),
                (4.85,2.3,'커튼'),(0.5,1.3,'탈의'),(0.5,2.85,'탈의'),(16.0,1.75,'화장대 4석'),
                (3.75,6.15,'↕'),(9.9,6.15,'↕'),(18.1,6.15,'↕')):
    a(f'<text x="{x}" y="{y}">{t}</text>')
a('</g>')

# 카메라 (1차 5개)
cams = ((14,17.9,0),(22.6,9.9,90),(9.8,12.1,255),(9.4,4.0,38),(21.2,10.4,150))
a('<g id="cameras">')
for x, y, h in cams:
    a(f'<use href="#cam" transform="translate({x},{y}) rotate({h})"/>')
a('<g font-size="0.4" font-weight="700" fill="#fff" text-anchor="middle">')
for i, (x, y, h) in enumerate(cams, 1):
    a(f'<text x="{x}" y="{y+0.14:.2f}">{i}</text>')
a('</g></g>')

# 치수선
a('<g stroke="#9a8f85" stroke-width="0.035" fill="#7a7068" font-size="0.36" text-anchor="middle">')
a(f'<line x1="0" y1="-0.4" x2="{W}" y2="-0.4"/>')
for x in (0, 7, 14, 18, 21, 28):
    a(f'<line x1="{x}" y1="-0.58" x2="{x}" y2="-0.22"/>')
for x, t in ((3.5,'7m'),(10.5,'7m'),(16,'4m'),(19.5,'3m'),(24.5,'7m')):
    a(f'<text x="{x}" y="-0.56" stroke="none">{t}</text>')
a(f'<line x1="{W+0.45}" y1="0" x2="{W+0.45}" y2="{H}"/>')
for y in (0, RD, CY, BY, H):
    a(f'<line x1="{W+0.27}" y1="{y}" x2="{W+0.63}" y2="{y}"/>')
for y, t in ((2.4,'4.6m'),(5.6,'1.8m'),(10.35,'7.7m'),(16.5,'4.6m')):
    a(f'<text x="{W+1.25}" y="{y}" stroke="none">{t}</text>')
a('</g>')

# 범례
a('<g id="legend" font-size="0.36" fill="#5a4f45">')
a('<circle cx="0.3" cy="20.9" r="0.26" fill="#e2622b"/>')
a('<text x="0.8" y="21.03">카메라 1 입구에서 홀 · 2 라운지에서 TV 벽 · 3 발마사지 · 4 2인실 · 5 데스크·화장품</text>')
a(f'<line x1="0.05" y1="21.8" x2="0.6" y2="21.8" {CUR}/>')
a('<text x="0.8" y="21.93">천장형 커튼</text>')
a(f'<rect x="3.6" y="21.58" width="0.5" height="0.4" {DSP}/>')
a('<text x="4.3" y="21.93">데스크·조명 진열</text>')
a('<rect x="8.0" y="21.58" width="0.5" height="0.4" fill="#f7ecd9" stroke="#b08d57" stroke-width="0.035"/>')
a('<text x="8.7" y="21.93">탈의·락커 구역 (문이 이 안으로 열린다)</text>')
a('<text x="16.6" y="21.93">↕ 홀과 복도를 잇는 개구부</text>')
a('</g>')
a('</svg>')
open(__file__.replace('make_plan.py', 'floor-plan-draft.svg'), 'w', encoding='utf-8').write('\n'.join(o) + '\n')
