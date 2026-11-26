"""매장 평면도 초안을 SVG로 만든다. 단위는 미터, 전체 18 x 12 (가로:세로 3:2)."""
W, H = 18, 12
o = []
a = o.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1.6 -2.4 21.2 21.2" width="1060" height="1060" font-family="\'Apple SD Gothic Neo\',\'Noto Sans KR\',\'Malgun Gothic\',sans-serif">')
a('<rect x="-1.6" y="-2.4" width="21.2" height="21.2" fill="#ffffff"/>')
a('<text x="0" y="-1.55" font-size="0.5" font-weight="700" fill="#2b2622">바디·스킨케어 매장 평면도 (초안)</text>')
a('<text x="0" y="-0.95" font-size="0.3" fill="#7a7068">전체 가로:세로 3:2. 18m × 12m는 가정값이고 위가 도면 상단이다. 실측 후 다시 그린다.</text>')

CUR = 'fill="none" stroke="#b08d57" stroke-width="0.06" stroke-dasharray="0.16 0.1"'
FUR = 'fill="#fff" stroke="#8a7d70" stroke-width="0.04"'
a('<defs>')
# 2인실 (6 x 3.5, 안쪽 벽이 y=0): 왼쪽 1.5m는 탈의·락커 구역, 나머지 4.5m에 베드 2
a('<g id="room">')
a('<rect x="0.06" y="0.06" width="1.44" height="3.38" fill="#f7ecd9"/>')
a('<g stroke="#8a7d70" stroke-width="0.05"><line x1="0.06" y1="1.1" x2="1.5" y2="1.1"/><line x1="0.06" y1="2.4" x2="1.5" y2="2.4"/></g>')
a(f'<line x1="1.5" y1="0.08" x2="1.5" y2="1.1" {CUR}/>')
a(f'<line x1="1.5" y1="2.4" x2="1.5" y2="3.42" {CUR}/>')
a(f'<rect x="0.08" y="1.2" width="0.6" height="0.55" {FUR}/>')
a(f'<rect x="0.08" y="1.75" width="0.6" height="0.55" {FUR}/>')
a(f'<rect x="5.4" y="0.1" width="0.5" height="0.5" {FUR}/>')
for bx in (2.2, 4.5):
    a(f'<rect x="{bx}" y="0.75" width="0.8" height="2" rx="0.1" {FUR}/>')
    a(f'<rect x="{bx+0.1}" y="0.83" width="0.6" height="0.35" rx="0.08" fill="#e9e1d6" stroke="#8a7d70" stroke-width="0.03"/>')
    a(f'<circle cx="{bx+0.4}" cy="0.45" r="0.15" fill="#e9e1d6" stroke="#8a7d70" stroke-width="0.03"/>')
a('<rect x="3.35" y="0.12" width="0.8" height="0.48" rx="0.06" fill="#d6e4ea" stroke="#5f7f8c" stroke-width="0.04"/>')
a('<circle cx="3.75" cy="0.36" r="0.15" fill="#fff" stroke="#5f7f8c" stroke-width="0.03"/>')
a(f'<line x1="3.75" y1="0.6" x2="3.75" y2="2.55" {CUR}/>')
a('<rect x="3.18" y="1.5" width="0.4" height="0.5" rx="0.05" fill="#e9e1d6" stroke="#8a7d70" stroke-width="0.03"/>')
a('<rect x="3.92" y="1.5" width="0.4" height="0.5" rx="0.05" fill="#e9e1d6" stroke="#8a7d70" stroke-width="0.03"/>')
a('</g>')
a('<g id="cam"><path d="M0 0 L-0.5 -0.95 L0.5 -0.95 Z" fill="#e2622b" opacity="0.28"/><circle r="0.3" fill="#e2622b"/></g>')
a('</defs>')

# 바닥
a(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#f6f1ea"/>')
for x in (0, 6, 12):
    a(f'<rect x="{x}" y="0" width="6" height="3.5" fill="#efe3d3"/>')
a('<rect x="12" y="8.5" width="6" height="3.5" fill="#efe3d3"/>')
a('<rect x="0" y="6.9" width="4.85" height="1.6" fill="#e6ecdf"/>')      # 발마사지
a('<rect x="0" y="8.5" width="2.2" height="3.5" fill="#e4e4e4"/>')        # 재고 + 린넨
a('<rect x="2.2" y="10.2" width="1.0" height="1.8" fill="#e4e4e4"/>')
a('<rect x="2.2" y="8.5" width="3.8" height="1.7" fill="#f1e1e3"/>')      # 파우더룸
a('<rect x="3.2" y="10.2" width="2.8" height="1.8" fill="#dfe8ee"/>')     # 직원휴게실
a('<rect x="13.5" y="7.0" width="4.5" height="1.5" fill="#fbf1dc"/>')     # 화장품

# 2인실
for x in (0, 6, 12):
    a(f'<use href="#room" transform="translate({x},0)"/>')
a('<use href="#room" transform="translate(18,12) scale(-1,-1)"/>')

# 발마사지: 암체어 5 + 바닥 발마사지기
for i in range(5):
    x = 0.2 + 0.92 * i
    a(f'<rect x="{x:.2f}" y="7.65" width="0.75" height="0.8" rx="0.2" fill="#fff" stroke="#6f8560" stroke-width="0.04"/>')
    a(f'<rect x="{x+0.12:.2f}" y="7.05" width="0.51" height="0.45" rx="0.08" fill="#cfdcc4" stroke="#6f8560" stroke-width="0.03"/>')

# 휴식, 상담, 대표 제품, 벤치
a(f'<g {FUR}>')
a('<circle cx="0.75" cy="4.3" r="0.36"/><circle cx="0.75" cy="5.7" r="0.36"/><circle cx="0.75" cy="5.0" r="0.22" fill="#e9e1d6"/>')
a('<rect x="6.4" y="3.64" width="1.7" height="0.45" rx="0.12"/><rect x="10" y="3.64" width="1.7" height="0.45" rx="0.12"/>')
a('<circle cx="6.9" cy="5.6" r="0.42" fill="#e9e1d6"/><circle cx="6.2" cy="5.6" r="0.25"/><circle cx="7.6" cy="5.6" r="0.25"/><circle cx="6.9" cy="4.9" r="0.25"/>')
a('</g>')
a('<circle cx="9" cy="7.2" r="0.55" fill="#3a332d"/><circle cx="9" cy="7.2" r="0.26" fill="#f6f1ea"/>')

# 라운지, TV, 커피바
a(f'<g {FUR}>')
a('<rect x="13.4" y="4.5" width="0.9" height="2.3" rx="0.22"/>')
a('<rect x="15.1" y="3.9" width="0.8" height="0.8" rx="0.25"/>')
a('<rect x="15" y="5.25" width="1" height="0.8" rx="0.15" fill="#e9e1d6"/>')
a('</g>')
a('<rect x="17.78" y="4.95" width="0.12" height="1.6" fill="#2b2622"/>')
a('<rect x="17.3" y="3.65" width="0.6" height="1.15" rx="0.06" fill="#d9c2a3" stroke="#8a6a3f" stroke-width="0.04"/>')

# 화장품: 벽면 조명 진열장 1면 + 테스터 스탠드
DSP = 'fill="#f3d9a8" stroke="#a9812f" stroke-width="0.04"'
a(f'<rect x="13.6" y="8.03" width="4.3" height="0.42" {DSP}/>')
a(f'<rect x="14.4" y="7.2" width="2.8" height="0.45" rx="0.08" {DSP}/>')
# 인허가 진열대, 데스크
a(f'<rect x="6.08" y="8.7" width="0.36" height="1.4" {DSP}/>')
a('<rect x="10.8" y="9.2" width="0.6" height="2.2" rx="0.18" fill="#fff" stroke="#3a332d" stroke-width="0.06"/>')
a('<circle cx="11.68" cy="10.3" r="0.2" fill="#e9e1d6" stroke="#8a7d70" stroke-width="0.03"/>')

# 파우더룸 화장대 3석
a('<rect x="2.4" y="9.65" width="2.4" height="0.45" fill="#fff" stroke="#a06f78" stroke-width="0.04"/>')
for cx in (2.9, 3.6, 4.3):
    a(f'<circle cx="{cx}" cy="9.38" r="0.17" fill="#fff" stroke="#a06f78" stroke-width="0.03"/>')
# 창고 선반, 수거함, 직원휴게실
a('<g fill="#fff" stroke="#888" stroke-width="0.04"><rect x="0.1" y="8.62" width="0.5" height="3.26"/><rect x="0.7" y="11.4" width="1.6" height="0.48"/></g>')
a('<rect x="2.45" y="11.3" width="0.55" height="0.55" rx="0.08" fill="#cfcfcf" stroke="#888" stroke-width="0.04"/>')
a('<g fill="#fff" stroke="#5f7f8c" stroke-width="0.04"><rect x="3.4" y="11.4" width="2.4" height="0.48" rx="0.12"/></g>')

# 벽
a('<g fill="none" stroke="#2b2622" stroke-linecap="square">')
a(f'<rect x="0" y="0" width="{W}" height="{H}" stroke-width="0.2"/>')
a('<g stroke-width="0.12">')
for l in ((0,3.5,18,3.5),(6,0,6,3.5),(12,0,12,3.5),(0,8.5,6,8.5),(6,8.5,6,12),(2.2,8.5,2.2,10.2),(2.2,10.2,6,10.2),(3.2,10.2,3.2,12),(12,8.5,12,12),(12,8.5,18,8.5)):
    a('<line x1="%s" y1="%s" x2="%s" y2="%s"/>' % l)
a('</g></g>')

# 문
a('<g stroke="#f6f1ea" stroke-width="0.18">')
for l in ((3.6,3.5,4.5,3.5),(8.55,3.5,9.45,3.5),(14.55,3.5,15.45,3.5),(12.4,8.5,13.3,8.5),(4.95,8.5,5.85,8.5),(6,10.6,6,11.5),(3.2,10.6,3.2,11.5)):
    a('<line x1="%s" y1="%s" x2="%s" y2="%s"/>' % l)
a('</g>')
a('<line x1="8.1" y1="12" x2="9.9" y2="12" stroke="#ffffff" stroke-width="0.26"/>')
a('<g fill="none" stroke="#2b2622" stroke-width="0.04">')
for d in ('M3.6 3.5 L3.6 2.6 A0.9 0.9 0 0 1 4.5 3.5','M8.55 3.5 L8.55 2.6 A0.9 0.9 0 0 1 9.45 3.5','M14.55 3.5 L14.55 2.6 A0.9 0.9 0 0 1 15.45 3.5',
          'M12.4 8.5 L12.4 9.4 A0.9 0.9 0 0 0 13.3 8.5','M5.85 8.5 L5.85 9.4 A0.9 0.9 0 0 1 4.95 8.5',
          'M6 10.6 L5.1 10.6 A0.9 0.9 0 0 0 6 11.5','M3.2 10.6 L2.3 10.6 A0.9 0.9 0 0 0 3.2 11.5',
          'M8.1 12 L8.1 11.1 A0.9 0.9 0 0 1 9 12','M9.9 12 L9.9 11.1 A0.9 0.9 0 0 0 9 12'):
    a(f'<path d="{d}"/>')
a('</g>')

# 이름
a('<g font-size="0.34" font-weight="700" fill="#2b2622" text-anchor="middle">')
for x, y, t in ((2.75,3.25,'2인실 1'),(10.4,3.2,'2인실 2'),(16.2,3.2,'2인실 3'),(15.4,9.0,'2인실 4'),(2.4,6.7,'셀프 발마사지 5석'),(3.6,9.0,'파우더룸'),
                (1.35,9.4,'재고'),(1.45,10.75,'린넨창고'),(4.15,11.15,'직원휴게실'),(16.1,6.7,'라운지'),(9,13.0,'출입구')):
    a(f'<text x="{x}" y="{y}">{t}</text>')
a('</g>')
a('<g font-size="0.27" fill="#5a4f45" text-anchor="middle">')
for x, y, t in ((16.9,5.85,'TV'),(16.55,4.3,'커피바') if False else (16.6,5.05,''),(14.4,7.92,'화장품 진열 벽'),(17.62,7.52,'카운터'),(7.45,9.5,'인허가 진열대'),(10.0,10.35,'데스크'),
                (9,8.1,'대표 제품'),(1.6,5.1,'휴식'),(7.25,4.45,'벤치'),(10.85,4.45,'벤치'),(6.9,6.4,'상담석'),(4.15,2.3,'커튼'),(0.78,0.7,'탈의'),(0.78,3.0,'탈의'),(1.08,1.85,'락커'),(2.72,11.2,'')):
    if t: a(f'<text x="{x}" y="{y}">{t}</text>')
a('<text x="17.15" y="4.3" text-anchor="end">커피바</text>')
a('</g>')

# 카메라 (1차 5개)
cams = ((9,11.2,0),(12.6,5.65,90),(5.4,6.5,250),(9,2.95,0),(14.75,6.6,160))
a('<g id="cameras">')
for x, y, h in cams:
    a(f'<use href="#cam" transform="translate({x},{y}) rotate({h})"/>')
a('<g font-size="0.34" font-weight="700" fill="#fff" text-anchor="middle">')
for i, (x, y, h) in enumerate(cams, 1):
    a(f'<text x="{x}" y="{y+0.12:.2f}">{i}</text>')
a('</g></g>')

# 치수선
a('<g stroke="#9a8f85" stroke-width="0.03" fill="#7a7068" font-size="0.28" text-anchor="middle">')
a('<line x1="0" y1="-0.35" x2="18" y2="-0.35"/>')
for x in (0, 6, 12, 18):
    a(f'<line x1="{x}" y1="-0.5" x2="{x}" y2="-0.2"/>')
for x in (3, 9, 15):
    a(f'<text x="{x}" y="-0.48" stroke="none">6m</text>')
a('<line x1="18.4" y1="0" x2="18.4" y2="12"/>')
for y in (0, 3.5, 8.5, 12):
    a(f'<line x1="18.25" y1="{y}" x2="18.55" y2="{y}"/>')
for y, t in ((1.85,'3.5m'),(6.1,'5m'),(10.35,'3.5m')):
    a(f'<text x="19" y="{y}" stroke="none">{t}</text>')
a('</g>')

# 범례
a('<g id="legend" font-size="0.28" fill="#5a4f45">')
a('<circle cx="0.3" cy="13.9" r="0.22" fill="#e2622b"/>')
a('<text x="0.7" y="14.0">카메라 1 입구에서 홀 · 2 라운지에서 TV 벽 · 3 발마사지 · 4 2인실 문 안쪽 · 5 화장품 진열</text>')
a(f'<line x1="0.1" y1="14.6" x2="0.5" y2="14.6" {CUR}/>')
a('<text x="0.7" y="14.7">천장형 커튼</text>')
a(f'<rect x="3.2" y="14.42" width="0.4" height="0.32" {DSP}/>')
a('<text x="3.8" y="14.7">조명 진열장</text>')
a('<rect x="6.4" y="14.42" width="0.4" height="0.32" fill="#f7ecd9" stroke="#b08d57" stroke-width="0.03"/>')
a('<text x="7.0" y="14.7">탈의·락커 구역</text>')
a('</g>')
a('</svg>')
open(__file__.replace('make_plan.py', 'floor-plan-draft.svg'), 'w', encoding='utf-8').write('\n'.join(o) + '\n')
