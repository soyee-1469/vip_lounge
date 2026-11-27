"""매장 평면도를 SVG로 만든다. 4안 = 실제 도면(2026-11-26 레이아웃).

좌표는 reference/actual/daejeon_3d_261126.html 의 2층 데이터를 그대로 옮긴 actual-2f.json 에서 읽는다.
원본은 원점이 도면 좌하단이고 y가 위쪽이다. SVG는 y가 아래쪽이라 Y = TOP - y 로 뒤집는다.
2층에서 고객 구역은 왼쪽 약 16.5m(VIP 라운지와 관리실)뿐이고 오른쪽은 사무 구역이다. 이 도면은 고객 구역을 그린다.

1~3안은 _old/ 폴더에 있다. 앱(src/lib/views.ts)이 이 SVG를 줄 단위로 읽으므로 요소를 한 줄에 하나씩 쓴다.
"""
import json, os, re, sys
VARIANT = sys.argv[1] if len(sys.argv) > 1 else 'cafe'   # cafe = 카페 라운지, sales = 판매 라운지
HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, 'actual-2f.json'), encoding='utf-8'))
TOP = 17.45
XMAX = 19.9          # 고객 구역 + 경계 너머 사무 구역 한 줄까지만 그린다
# 2026-11-27 실측: 관리실 1~3 깊이 3.7m, 복도 1.2m, 복도에서 EV 홀 벽까지 5.8m(관리실 문 벽부터 7.0m).
# 받은 도면(3.47 / 1.21 / 7.17)을 구간별로 늘이고 줄인다. EV 홀 벽 아래(남쪽)는 1.15m 위로 당긴다.
def F(v):
    if v <= 3.47: return round(v * 3.7 / 3.47, 3)
    if v <= 4.68: return round(3.7 + (v - 3.47) * 1.2 / 1.21, 3)
    if v <= 11.85: return round(4.9 + (v - 4.68) * 5.8 / 7.17, 3)
    return round(v - 1.15, 3)
def Y(y): return F(TOP - y)
o = []
a = o.append
VB = (-1.6, -2.4, 25.2, 23.6)
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VB[0]} {VB[1]} {VB[2]} {VB[3]}" width="1512" height="1416" font-family="\'Apple SD Gothic Neo\',\'Noto Sans KR\',\'Malgun Gothic\',sans-serif">')
a(f'<rect x="-1.6" y="-2.4" width="{VB[2]}" height="{VB[3]}" fill="#ffffff"/>')
a('<text x="0" y="-1.5" font-size="0.6" font-weight="700" fill="#2b2622">토마톡 대전 2층 매장 평면도 (실제 도면)</text>')
a('<text x="0" y="-0.85" font-size="0.36" fill="#7a7068">2026-11-26 레이아웃을 2026-11-27 실측(관리실 3.7m, 복도 1.2m, 그 아래 5.8m)에 맞추고 손 스케치를 반영했다. 왼쪽이 고객 구역, 오른쪽은 사무 구역이다.</text>')

FILL = {'skin': '#efe3d3', 'path': '#f1ece4', 'wc': '#e3e9ee', 'circ': '#e2e2e2', 'core': '#e4e4e4',
        'office': '#e6eaf0', 'meeting': '#e6eaf0', 'void': '#eef1ee'}
CUR = 'fill="none" stroke="#b08d57" stroke-width="0.07" stroke-dasharray="0.18 0.12"'
FUR = 'fill="#fff" stroke="#8a7d70" stroke-width="0.04"'
DSP = 'fill="#f3d9a8" stroke="#a9812f" stroke-width="0.04"'

# 발마사지·커피바·TV·좌석을 넣으려고 실제 도면에서 빼거나 옮기는 것 (2026-11-26 제안)
REMOVE = {'아일랜드 매대1', '아일랜드 매대2', '윈도 진열대', '테스터 바', '결제 카운터', '대기 소파'}
if VARIANT == 'sales':   # 판매 라운지: 받은 도면의 아일랜드 매대와 테스터 바를 그대로 둔다
    REMOVE = {'윈도 진열대', '결제 카운터', '대기 소파'}
# 2026-11-27 손 스케치 반영: 관리동(린넨·소독·재고)은 왼쪽 아래 그대로, 서쪽 끝에 세탁실. 파우더룸은 같은 자리에서 1.6 × 2.4m.
# 발마사지를 빼고 결제·상담 데스크를 둔다. 자동문은 1.0m로 줄이고 나머지는 벽. 관리실 4는 그대로, 문만 동쪽 끝으로.
REMOVE |= {'파우더룸', '벽면 진열장'}   # 벽면 진열장(D450) 대신 얇은 가벽(70mm)을 세운다
zones = [z for z in D['zones'] if z['x'] < XMAX and z['n'] not in REMOVE]
# 관리실 1~3: 문을 복도 쪽 벽 가운데로 옮기고 미닫이로 한다. 방 안 가구는 아래에서 새로 그린다(손 스케치)
zones = [z for z in zones if not re.match(r'(베드|미용기기|매니저 의자)[1-4]-|(세면대|커튼)[1-4]$', z['n'])]
for z in zones:
    if z['n'] in ('관리실1', '관리실2', '관리실3'):
        z['doors'] = [{'side': 'S', 'at': 0.5, 'slide': True}]
    if z['n'] == '관리실4':   # 관리실 4도 문을 체험 대기 쪽 벽 가운데 미닫이로
        z['doors'] = [{'side': 'N', 'at': 0.5, 'slide': True}]
    if z['n'] == '린넨·소독·재고창고':   # 깊이 1.5m(안쪽 1.4m), 길이 5.4m. 문은 가운데 쪽
        z['y'], z['d'], z['w'], z['doors'] = TOP - 11.85, 11.85 - 9.995, 5.4, [{'side': 'N', 'at': 0.02}]   # 변환 후 깊이 1.5m   # 문은 받은 도면대로 서쪽 끝(x 0.1~1.0)
def rect(z, extra=''):
    w = min(z['w'], XMAX - z['x'])
    t, b = Y(z["y"] + z["d"]), Y(z["y"])
    return f'<rect x="{z["x"]}" y="{t}" width="{round(w,3)}" height="{round(b - t, 3)}" {extra}/>'
def poly(pts): return ' '.join(f'{min(x, XMAX)},{Y(y)}' for x, y in pts)

a('<defs><g id="cam"><path d="M0 0 L-0.5 -0.95 L0.5 -0.95 Z" fill="#e2622b" opacity="0.28"/><circle r="0.3" fill="#e2622b"/></g></defs>')

# 바닥: 고객 구역 슬래브
a(f'<polygon points="{poly(D["slab"])}" fill="#f6f1ea"/>')
lounge = next(z for z in zones if z['n'].startswith('VIP 라운지'))
a(f'<polygon points="{poly(lounge["poly"])}" fill="#f8f2e6"/>')
for z in zones:
    if z['g'] in ('furn', 'outlet') or z['n'].startswith(('커튼', 'VIP 라운지', '구획벽', '유리 자동문', '윈도 진열대', '체험 대기', '파우더룸', '업무 라운지')):
        continue
    if 'poly' in z:
        a(f'<polygon points="{poly(z["poly"])}" fill="{FILL.get(z["g"], "#eee")}"/>')
    else:
        a(rect(z, f'fill="{FILL.get(z["g"], "#eee")}"'))
a('<rect x="11.09" y="5.4" width="5.4" height="4.64" fill="#f3ead8"/>')   # 체험 대기 (실측 좌표)
a('<rect x="5.4" y="8.3" width="1.6" height="2.4" fill="#f1e1e3"/>')

# 상담 테이블 2개는 뺀다. 체험 대기는 소파 위주로 채운다
zones = [z for z in zones if not z['n'].startswith('상담')]

# 가구
for z in zones:
    if z['n'].startswith('커튼'):
        a(f'<line x1="{z["x"]}" y1="{Y(z["y"])}" x2="{z["x"]}" y2="{Y(z["y"] + z["d"])}" {CUR}/>')
    elif z['g'] == 'furn':
        style = DSP if z['n'] in ('벽면 진열장', '윈도 진열대', '결제 카운터', '테스터 바') or z['n'].startswith('아일랜드') else FUR
        if z['n'].startswith('세면대'):
            style = 'fill="#d6e4ea" stroke="#5f7f8c" stroke-width="0.04"'
        rx = 0.2 if '의자' in z['n'] else 0.06
        if z['n'].startswith(('상담 테이블', '상담 의자')):
            rx = z['w'] / 2   # 상담 테이블과 의자는 원형
        a(rect(z, f'rx="{rx}" {style}'))

# ── 추가 제안: 실제 도면에 없던 것. 좌표는 SVG 기준(y 아래쪽) ──
ADD = 'stroke="#2f6b4f" stroke-width="0.05"'
a('<g id="proposed">')
# 벽면 진열장 W9000 · D450 · H2100 (받은 도면 그대로, x 1.2~10.2, y 4.9~5.35): 복도와 라운지를 나눈다.
# 서쪽 끝과 창 사이 1.15m는 얇은 벽으로 막고, 동쪽 끝(x 10.2~)은 복도 입구로 열어 둔다
a(f'<rect x="1.2" y="4.9" width="9.0" height="0.45" {DSP}/>')
a('<rect x="0.05" y="4.9" width="1.15" height="0.1" fill="#2b2622"/>')
# 창가 벤치: 서쪽 통유리를 따라 깊이 0.5m, 3석. 관리동 문(x 0.1~1.0)이 열리는 자리 앞에서 끝난다
# 벤치 0.8m 3칸 사이사이에 작은 원형 테이블(지름 0.4m) 2개. 커피잔을 옆에 놓는다. y 5.05~8.25
for y0 in (5.05, 6.25, 7.45):
    a(f'<rect x="0.05" y="{y0}" width="0.5" height="0.8" rx="0.08" fill="#fff" {ADD}/>')
for cy in (6.05, 7.25):
    a(f'<circle cx="0.3" cy="{cy}" r="0.2" fill="#e9e1d6" {ADD}/>')
# TV 85인치: 진열장 앞면에 건다. 발마사지 의자에서 약 2.5m
a('<rect x="2.25" y="5.35" width="1.9" height="0.08" fill="#2b2622"/>')
# 커피머신: 가벽 앞으로 0.6m 튀어나온 카운터. 소파 동쪽 끝 옆이라 소파 앞 통로를 막지 않는다
# 진열장의 커피 칸 1.2m를 비우고 하부장(깊이 0.6, 진열장보다 0.15m 나옴)을 넣는다. 위에 전자동 머신 0.35 × 0.45, 오른쪽에 잔 트레이
a(f'<rect x="4.55" y="4.9" width="1.2" height="0.6" fill="#d9c2a3" {ADD}/>')
a('<rect x="4.65" y="4.98" width="0.35" height="0.45" fill="#2b2622"/>')
a('<rect x="5.1" y="5.05" width="0.55" height="0.35" fill="#efe6d6" stroke="#8a7d70" stroke-width="0.03"/>')
# 셀프 발마사지 4석: 관리동 벽(y 9.2)에 등을 대고 TV를 본다. 발마사지기 0.5 + 의자 0.85. 앞은 비워 둔다(소파는 뺐다)
for i in range(4):
    x = 1.1 + 1.12 * i
    a(f'<rect x="{x:.2f}" y="8.35" width="0.85" height="0.85" rx="0.2" fill="#fff" {ADD}/>')
    a(f'<rect x="{x + 0.2:.2f}" y="7.85" width="0.45" height="0.5" rx="0.08" fill="#cfdcc4" {ADD}/>')
# 체험 대기 (2026-11-27): 동쪽 벽 TV를 보고 앉는다. 3인 소파가 서쪽에 등을 두고 TV를 정면으로 보고(거리 2.9m),
# 낮은 테이블 양옆에 1인 암체어 2개가 마주 앉아 TV 쪽으로 열린 ㄷ자가 된다. 5석.
# 관리실 4 벽 앞(y 8.6~10.04)은 1.4m 비워 문까지 가는 길로 쓴다
a(f'<rect x="12.6" y="6.1" width="0.85" height="2.0" rx="0.22" fill="#fff" {ADD}/>')
for k in (1, 2):
    a(f'<line x1="12.7" y1="{6.1 + 2.0 * k / 3:.2f}" x2="13.2" y2="{6.1 + 2.0 * k / 3:.2f}" stroke="#2f6b4f" stroke-width="0.03"/>')
a(f'<rect x="13.85" y="6.75" width="0.8" height="0.7" rx="0.15" fill="#e9e1d6" {ADD}/>')
a(f'<rect x="13.85" y="5.8" width="0.8" height="0.8" rx="0.3" fill="#fff" {ADD}/><rect x="13.85" y="7.6" width="0.8" height="0.8" rx="0.3" fill="#fff" {ADD}/>')
# 브랜드 월: 벽면 진열장 가운데 x 7.2~9.4(2.2m). 유리 자동문(x 7.6~9.0)의 중심 8.3과 한 줄이다
a(f'<rect x="6.4" y="4.95" width="2.2" height="0.38" fill="#8d4b32" {ADD}/>')   # 브랜드 월: 진열장 가운데 2.2m 칸
a(f'<rect x="8.65" y="4.95" width="1.5" height="0.38" fill="#f6e2b8" {ADD}/>')   # 화장품 진열: 브랜드 월 오른쪽 칸 1.6m
a('<line x1="7.5" y1="5.4" x2="7.5" y2="10.1" stroke="#8d4b32" stroke-width="0.04" stroke-dasharray="0.12 0.16"/>')
# 결제·상담 카운터: 자동문 오른쪽, EV 홀 벽에서 북쪽으로 짧게 뺀다(0.65 × 1.52m). 둥글게 길게 빼지 않는다
# 손님은 자동문 쪽(서쪽)에서, 직원은 동쪽에서 선다
# 결제·상담 프론트: 관리실 4 서쪽 벽 선(x 11.0)을 따라 EV 홀 벽에서 북쪽으로 1.4m 뒷벽을 세우고,
# 그 앞에 카운터(0.6 × 1.2)를 둔다. 직원은 카운터와 뒷벽 사이(0.8m)에 서고 북쪽으로 드나든다.
# 손님은 입구 쪽(서쪽)에서 응대받는다. 자동문 길(x 7~8)에서 1.6m 떨어진다
a('<rect x="11.0" y="9.3" width="0.1" height="1.4" fill="#2b2622"/>')
a(f'<rect x="9.6" y="9.4" width="0.6" height="1.2" rx="0.06" {DSP}/>')
# 데스크 서쪽 변은 x 10.2~10.8로 0.6m 들여서 끝을 관리실 4의 모서리에 붙인다. 직원은 오른쪽 끝으로 드나든다
# 파우더룸 1.6 × 2.4m (같은 자리, 크기 확정): 자동문 왼쪽. 동쪽 창살 벽에 화장대, 라운지 쪽(북)으로 열린다
a('<g stroke="#2f6b4f" stroke-width="0.12" stroke-linecap="butt" stroke-dasharray="0.06 0.08"><line x1="7.0" y1="8.3" x2="7.0" y2="10.7"/></g>')
a(f'<rect x="6.45" y="8.5" width="0.5" height="2.1" fill="#fff" stroke="#a06f78" stroke-width="0.045"/>')
for cy in (8.9, 9.55, 10.2):
    a(f'<circle cx="6.15" cy="{cy}" r="0.2" fill="#fff" stroke="#a06f78" stroke-width="0.035"/>')
# 관리동 안 세탁실: 서쪽 끝 1.6m. 세탁기, 온수기 100L
a('<rect x="1.6" y="9.2" width="0.08" height="0.65" fill="#2b2622"/>')   # 칸막이 남쪽 0.85m는 린넨 쪽으로 열어 둔다
a('<rect x="0.15" y="9.9" width="0.7" height="0.7" fill="#fff" stroke="#8a7d70" stroke-width="0.04"/>')
a('<circle cx="1.2" cy="9.6" r="0.28" fill="#fff" stroke="#8a7d70" stroke-width="0.04"/>')
# 관리실 1~3 (손 스케치 2026-11-27): 문은 복도 쪽 벽 가운데 미닫이. 들어서면 두 베드 사이 통로이고,
# 가운데 커튼으로 베드를 나눈다. 세면대는 북쪽 벽 가운데, 북쪽 두 모서리는 곡선 커튼 탈의 칸, 문 양옆 구석에 옷장과 수납
# 관리실 4는 문이 북쪽이라 같은 배치를 위아래로 뒤집는다(머리는 남쪽 벽)
def room(x0, w, top, depth, flip):
    def yy(v, h=0):   # 북쪽 벽에서 v 떨어진 높이 h짜리 물건의 윗변
        return round(top + depth - v - h, 2) if flip else round(top + v, 2)
    m = x0 + w / 2
    for bx, cx in ((m - 1.7, m - 2.35), (m + 1.0, m + 1.85)):   # 베드 0.7 × 1.9, 머리는 문 반대쪽 벽. 카트는 바깥쪽
        a(f'<rect x="{bx:.2f}" y="{yy(0.6, 1.9)}" width="0.7" height="1.9" rx="0.06" {FUR}/>')
        a(f'<circle cx="{bx + 0.35:.2f}" cy="{yy(0.32)}" r="0.2" {FUR}/>')
        a(f'<rect x="{cx:.2f}" y="{yy(1.1, 0.5)}" width="0.5" height="0.5" rx="0.05" {FUR}/>')
    a(f'<rect x="{m - 0.22:.2f}" y="{yy(0.08, 0.6)}" width="0.45" height="0.6" fill="#d6e4ea" stroke="#5f7f8c" stroke-width="0.04"/>')   # 세면대
    a(f'<line x1="{m:.2f}" y1="{yy(0.8)}" x2="{m:.2f}" y2="{yy(2.5)}" {CUR}/>')                                                       # 가운데 커튼
    # 탈의 커튼: 머리맡 쪽 두 모서리에 반지름 0.95m 곡선 레일 커튼(손 스케치)
    sw = 1 if flip else 0
    a(f'<path d="M{x0 + 0.06:.2f} {yy(0.95)} A0.95 0.95 0 0 {sw} {x0 + 0.95:.2f} {yy(0.06)}" {CUR}/>')
    a(f'<path d="M{x0 + w - 0.95:.2f} {yy(0.06)} A0.95 0.95 0 0 {sw} {x0 + w - 0.06:.2f} {yy(0.95)}" {CUR}/>')
    for tx in (x0 + 0.33, x0 + w - 0.33):
        a(f'<text x="{tx:.2f}" y="{yy(0.42) if not flip else yy(0.42) + 0.07}" font-size="0.2" fill="#5a4f45" text-anchor="middle">탈의</text>')
    sy = yy(depth - 0.65, 0.55)   # 문 쪽 벽에서 0.1m
    a(f'<rect x="{x0 + 0.1:.2f}" y="{sy}" width="0.9" height="0.55" fill="#d9d2c4" {ADD}/>')        # 옷장
    a(f'<rect x="{x0 + w - 1.3:.2f}" y="{sy}" width="1.2" height="0.55" fill="#d9d2c4" {ADD}/>')    # 수납
    a(f'<text x="{x0 + 0.55:.2f}" y="{sy + 0.35:.2f}" font-size="0.2" fill="#5a4f45" text-anchor="middle">옷장</text>')
    a(f'<text x="{x0 + w - 0.7:.2f}" y="{sy + 0.35:.2f}" font-size="0.2" fill="#5a4f45" text-anchor="middle">수납</text>')
for x0, w in ((0.05, 5.64), (5.69, 5.4), (11.09, 5.4)):
    room(x0, w, 0.0, 3.7, False)
room(11.09, 5.4, F(11.03), F(14.61) - F(11.03), True)
# 소파 뒤 낮은 플랜터(0.35 × 2.0): 라운지 쪽에서 소파 등을 가린다. 서쪽에 복도 가는 길 1.0m가 남는다
a('<rect x="12.15" y="6.1" width="0.35" height="2.0" rx="0.1" fill="#9db88f" stroke="#4f7a4a" stroke-width="0.05"/>')
# 뒤 소파 3인(0.85 × 2.0): 플랜터에 등을 대고 서쪽(라운지·결제 카운터 쪽)을 본다. 체험 대기 8석
a(f'<rect x="11.3" y="6.1" width="0.85" height="2.0" rx="0.22" fill="#fff" {ADD}/>')
for k in (1, 2):
    a(f'<line x1="11.65" y1="{6.1 + 2.0 * k / 3:.2f}" x2="12.05" y2="{6.1 + 2.0 * k / 3:.2f}" stroke="#2f6b4f" stroke-width="0.03"/>')
# 결제·상담 카운터 아일랜드 스툴 2개: 카운터 서쪽에 붙여 손님이 앉아 상담·결제한다. 직원은 카운터 동쪽에 선다.
# 자동문 길(x 7~8)에서 1.3m 떨어져 입구를 막지 않는다

# 화분: 체험 대기 모서리, TV 옆, 진열장 앞 커피·브랜드 월 사이와 그 동쪽
for px, py in ((16.15, 5.3), (16.15, 8.3)):
    a(f'<circle cx="{px}" cy="{py}" r="0.25" fill="#9db88f" stroke="#4f7a4a" stroke-width="0.05"/>')
# 대기 소파 위 TV: 체험 대기의 동쪽 벽(안내데스크와 관리실 3 사이). 보른 소파와 테스터 스툴에서 본다
a('<rect x="16.36" y="6.35" width="0.1" height="1.5" fill="#2b2622"/>')   # TV 75인치: 동쪽 벽, 소파 정면
a('<text x="16.15" y="7.1" font-size="0.26" fill="#5a4f45" text-anchor="middle" transform="rotate(-90 16.15 7.1)">TV 75"</text>')
# 호출 안내 화면: 체험 대기에서 보이는 복도 쪽

a('</g>')

# 벽: 닫힌 방의 외곽선
a('<g fill="none" stroke="#2b2622" stroke-width="0.12" stroke-linejoin="miter">')
for z in zones:
    if z['g'] in ('furn', 'outlet') or z['h'] < 2.0 or z['n'].startswith(('커튼', '구획벽', '유리 자동문', '윈도 진열대')):
        continue
    a(f'<polygon points="{poly(z["poly"])}"/>' if 'poly' in z else rect(z))
a('</g>')
a(f'<polygon points="{poly(D["slab"])}" fill="none" stroke="#2b2622" stroke-width="0.2"/>')
# 고객 구역과 사무 구역 경계(유리 파티션), 유리 자동문
part = next(z for z in zones if z['n'] == '구획벽')
a(rect(part, 'fill="#9fb6c4" stroke="#2b2622" stroke-width="0.05"'))
gd = next(z for z in zones if z['n'] == '유리 자동문')
a(rect(gd, 'fill="#bcd6e6" stroke="#5f7f8c" stroke-width="0.05"'))
# 2026-11-27: EV 홀 쪽은 벽, 유리 자동문은 x 7.0~8.0(폭 1.0m) 한 짝. 오른쪽으로 밀려 열린다
yg = Y(gd["y"] + gd["d"])
a(f'<rect x="2.83" y="{yg - 0.02}" width="8.26" height="{gd["d"] + 0.04}" fill="#2b2622"/>')
a(f'<rect x="7.0" y="{yg - 0.03}" width="1.0" height="{gd["d"] + 0.06}" fill="#bcd6e6" stroke="#5f7f8c" stroke-width="0.05"/>')
a(f'<path d="M7.5 {Y(gd["y"]) + 0.42} h1.1 m0 0 l-0.25 -0.13 m0.25 0.13 l-0.25 0.13" fill="none" stroke="#5f7f8c" stroke-width="0.05"/>')


# 문: 방의 한 변에서 at 비율 위치에 폭 0.9m
a('<g>')
for z in zones:
    for dr in z.get('doors', []):
        if z['n'] in ('구획벽',) or z['g'] in ('circ',) or z['x'] > 16.5:
            continue
        s, t = dr['side'], dr['at']
        if s in ('N', 'S'):
            cx = z['x'] + t * z['w']; yy = Y(z['y'] + z['d']) if s == 'N' else Y(z['y'])
            dw = 1.0 if dr.get('slide') else 0.9   # 관리실 미닫이 문은 폭 1.0m (실측)
            x1 = max(z['x'] + 0.1, min(cx - dw / 2, z['x'] + z['w'] - 1.0)); x2 = x1 + dw
            a(f'<line x1="{x1:.2f}" y1="{yy}" x2="{x2:.2f}" y2="{yy}" stroke="#f6f1ea" stroke-width="0.2"/>')
            inward = 1 if s == 'N' else -1      # 방 안쪽으로 열리는 방향(SVG y)
            if dr.get('slide'):   # 미닫이: 문짝이 방 바깥쪽 벽면에 달려 동쪽으로 밀린다
                ly = yy - inward * 0.12
                a(f'<line x1="{x1 + 0.45:.2f}" y1="{ly:.2f}" x2="{x2 + 0.45:.2f}" y2="{ly:.2f}" stroke="#2b2622" stroke-width="0.07"/>')
                a(f'<path d="M{x1 + 0.1:.2f} {ly - inward * 0.18:.2f} h0.5 l-0.12 -0.08 m0.12 0.08 l-0.12 0.08" fill="none" stroke="#2b2622" stroke-width="0.03"/>')
                continue
            a(f'<path d="M{x2:.2f} {yy} L{x2:.2f} {yy + inward * 0.9:.2f} A0.9 0.9 0 0 {1 if inward < 0 else 0} {x1:.2f} {yy}" fill="none" stroke="#2b2622" stroke-width="0.04"/>')
        else:
            cy = z['y'] + t * z['d']; xx = z['x'] + z['w'] if s == 'E' else z['x']
            y1 = Y(cy + 0.45); y2 = y1 + 0.9
            a(f'<line x1="{xx}" y1="{y1:.2f}" x2="{xx}" y2="{y2:.2f}" stroke="#f6f1ea" stroke-width="0.2"/>')
a('</g>')
# 경계벽의 문(관리실 복도 끝 → 사무 구역)
py = Y(part['y'] + 0.713 * part['d'])
# (복도 오른쪽 끝의 사무 구역 문은 없앤다. 벽으로 막는다)

# 이름
a('<g font-size="0.42" font-weight="700" fill="#2b2622" text-anchor="middle">')
for x, y, t in ((2.87, 14.55, '관리실 1'), (8.39, 14.55, '관리실 2'), (13.79, 14.55, '관리실 3'), (13.8, 5.2, '관리실 4'),
                (8.3, 13.25, '관리실 복도'), (9.3, 9.7, 'VIP 라운지'), 
                (3.9, 6.15, '린넨·소독·재고'), (9.15, 4.55, 'EV 홀'),
                (18.4, 10.0, '사무 구역'), (1.35, 4.3, '남 화장실'), (1.25, 1.5, '여 화장실'), (5.35, 1.6, '계단'), (8.3, 1.3, '승강기')):
    a(f'<text x="{x}" y="{Y(y)}">{t}</text>')
a('</g>')
a('<g font-size="0.3" fill="#5a4f45" text-anchor="middle">')
for x, y, t in (
                (7.5, 4.95, '유리 자동문 1.0m'), (9.15, 4.1, '고객 출입'), (18.4, 9.45, '(별도 구역)'),
                (2.87, 16.5, '세면대')):
    a(f'<text x="{x}" y="{Y(y)}">{t}</text>')
a(f'<text x="0.85" y="6.6" transform="rotate(-90 0.85 6.6)">창가 벤치</text>')
for x, y, t in ((3.2, 5.75, 'TV 85"'), (3.0, 7.7, '셀프 발마사지 4석'), (5.15, 5.85, '커피머신'),
                (7.5, 5.7, '브랜드 월'), (9.4, 5.7, '화장품 진열'), (10.3, 9.15, '결제·상담 프론트'), (14.25, 9.45, '관리실 4 가는 길'), (13.03, 8.45, '3인 소파'), (11.72, 8.45, '3인 소파'),  (6.2, 8.1, '파우더룸 1.6 × 2.4m')):   # 실측 좌표(SVG)
    a(f'<text x="{x}" y="{y}">{t}</text>')
a('<text x="14.0" y="5.35" font-size="0.42" font-weight="700" fill="#2b2622" text-anchor="middle">체험 대기</text>')
a('<text x="1.2" y="10.5" font-size="0.36" font-weight="700" fill="#2b2622" text-anchor="middle">세탁</text>')

a('</g>')

# 카메라 (아직 이미지 없음)
cams = ((7.5, 6.3, 0), (6.2, 8.6, 190), (15.9, 9.3, 300), (9.0, 14.4, 30))
a('<g id="cameras">')
for x, y, h in cams:
    a(f'<use href="#cam" transform="translate({x},{Y(y)}) rotate({h})"/>')
a('<g font-size="0.34" font-weight="700" fill="#fff" text-anchor="middle">')
for i, (x, y, h) in enumerate(cams, 1):
    a(f'<text x="{x}" y="{Y(y) + 0.12:.2f}">{i}</text>')
a('</g></g>')

# 치수선
a('<g stroke="#9a8f85" stroke-width="0.03" fill="#7a7068" font-size="0.32" text-anchor="middle">')
a('<line x1="0" y1="-0.35" x2="16.49" y2="-0.35"/>')
for x in (0, 5.69, 11.09, 16.49):
    a(f'<line x1="{x}" y1="-0.5" x2="{x}" y2="-0.2"/>')
for x, t in ((2.85, '5.64m'), (8.39, '5.40m'), (13.79, '5.40m')):
    a(f'<text x="{x}" y="-0.5" stroke="none">{t}</text>')
a('<line x1="-0.4" y1="0" x2="-0.4" y2="14.61"/>')
for y in (17.45, 13.98, 12.77, 5.6, 2.84):
    a(f'<line x1="-0.55" y1="{Y(y)}" x2="-0.25" y2="{Y(y)}"/>')
for y, t in ((15.7, '3700'), (13.4, '1200'), (9.2, '5800'), (4.2, '2.76')):
    a(f'<text x="-0.95" y="{Y(y) + 0.1:.2f}" stroke="none">{t}</text>')
a('<line x1="0" y1="18.2" x2="16.49" y2="18.2"/><line x1="0" y1="18.05" x2="0" y2="18.35"/><line x1="16.49" y1="18.05" x2="16.49" y2="18.35"/>')
a('<text x="8.25" y="18.7" stroke="none">고객 구역 폭 16.49m</text>')
a('</g>')

# 범례
a('<g id="legend" font-size="0.32" fill="#5a4f45">')
a('<circle cx="0.3" cy="19.6" r="0.22" fill="#e2622b"/>')
a('<text x="0.7" y="19.7">카메라 1 입구에서 라운지 · 2 판매 라운지 · 3 체험 대기 · 4 관리실</text>')
a(f'<line x1="0.1" y1="20.3" x2="0.5" y2="20.3" {CUR}/>')
a('<text x="0.7" y="20.4">커튼</text>')
a(f'<rect x="2.2" y="20.12" width="0.4" height="0.32" {DSP}/>')
a('<text x="2.8" y="20.4">진열·매대·카운터</text>')
a('<rect x="6.6" y="20.12" width="0.4" height="0.32" fill="#bcd6e6" stroke="#5f7f8c" stroke-width="0.04"/>')
a('<text x="7.2" y="20.4">유리</text>')
a('<rect x="8.6" y="20.12" width="0.4" height="0.32" fill="#fff" stroke="#2f6b4f" stroke-width="0.05"/>')
a('<text x="9.2" y="20.4">초록 테두리 = 실제 도면에 없던 추가 제안</text>')
a('</g>')
a('</svg>')
if VARIANT == 'sales':
    o = [l.replace('>카페 테이블<', '>아일랜드 매대<') for l in o]
open(os.path.join(HERE, f'floor-plan-{VARIANT}.svg'), 'w', encoding='utf-8').write('\n'.join(o) + '\n')
if VARIANT == 'cafe':
    open(os.path.join(HERE, 'floor-plan-medical.svg'), 'w', encoding='utf-8').write('\n'.join(o) + '\n')   # 두 컨셉은 배치가 같다
    open(os.path.join(HERE, 'floor-plan-draft.svg'), 'w', encoding='utf-8').write('\n'.join(o) + '\n')
