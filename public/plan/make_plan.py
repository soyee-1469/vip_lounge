"""매장 평면도를 SVG로 만든다. 4안 = 실제 도면(2026-11-26 레이아웃).

좌표는 reference/actual/daejeon_3d_261126.html 의 2층 데이터를 그대로 옮긴 actual-2f.json 에서 읽는다.
원본은 원점이 도면 좌하단이고 y가 위쪽이다. SVG는 y가 아래쪽이라 Y = TOP - y 로 뒤집는다.
2층에서 고객 구역은 왼쪽 약 16.5m(VIP 라운지와 관리실)뿐이고 오른쪽은 사무 구역이다. 이 도면은 고객 구역을 그린다.

1~3안은 _old/ 폴더에 있다. 앱(src/lib/views.ts)이 이 SVG를 줄 단위로 읽으므로 요소를 한 줄에 하나씩 쓴다.
"""
import json, os, sys
VARIANT = sys.argv[1] if len(sys.argv) > 1 else 'cafe'   # cafe = 카페 라운지, sales = 판매 라운지
HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, 'actual-2f.json'), encoding='utf-8'))
TOP = 17.45
XMAX = 19.9          # 고객 구역 + 경계 너머 사무 구역 한 줄까지만 그린다
def Y(y): return round(TOP - y, 3)
o = []
a = o.append
VB = (-1.6, -2.4, 25.2, 23.6)
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VB[0]} {VB[1]} {VB[2]} {VB[3]}" width="1512" height="1416" font-family="\'Apple SD Gothic Neo\',\'Noto Sans KR\',\'Malgun Gothic\',sans-serif">')
a(f'<rect x="-1.6" y="-2.4" width="{VB[2]}" height="{VB[3]}" fill="#ffffff"/>')
a('<text x="0" y="-1.5" font-size="0.6" font-weight="700" fill="#2b2622">토마톡 대전 2층 매장 평면도 (실제 도면)</text>')
a('<text x="0" y="-0.85" font-size="0.36" fill="#7a7068">2026-11-26 레이아웃과 3D 모델의 좌표를 그대로 옮겼다. 가정값이고 아닌 실제 치수다. 왼쪽이 고객 구역, 오른쪽은 사무 구역이다.</text>')

FILL = {'skin': '#efe3d3', 'path': '#f1ece4', 'wc': '#e3e9ee', 'circ': '#e2e2e2', 'core': '#e4e4e4',
        'office': '#e6eaf0', 'meeting': '#e6eaf0', 'void': '#eef1ee'}
CUR = 'fill="none" stroke="#b08d57" stroke-width="0.07" stroke-dasharray="0.18 0.12"'
FUR = 'fill="#fff" stroke="#8a7d70" stroke-width="0.04"'
DSP = 'fill="#f3d9a8" stroke="#a9812f" stroke-width="0.04"'

# 발마사지·커피바·TV·좌석을 넣으려고 실제 도면에서 빼거나 옮기는 것 (2026-11-26 제안)
REMOVE = {'아일랜드 매대1', '아일랜드 매대2', '윈도 진열대', '테스터 바', '결제 카운터', '대기 소파'}
if VARIANT == 'sales':   # 판매 라운지: 받은 도면의 아일랜드 매대와 테스터 바를 그대로 둔다
    REMOVE = {'윈도 진열대', '결제 카운터', '대기 소파'}
zones = [z for z in D['zones'] if z['x'] < XMAX and z['n'] not in REMOVE]
def rect(z, extra=''):
    w = min(z['w'], XMAX - z['x'])
    return f'<rect x="{z["x"]}" y="{Y(z["y"] + z["d"])}" width="{round(w,3)}" height="{z["d"]}" {extra}/>'
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
wait = next(z for z in zones if z['n'] == '체험 대기')
a(rect(wait, 'fill="#f3ead8"'))
powder = next(z for z in zones if z['n'] == '파우더룸')
a(rect(powder, 'fill="#f1e1e3"'))

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
# 셀프 커피바: 서쪽 창가 아래쪽 2.0 x 0.65. 위쪽 1.45m는 윈도 진열대를 남긴다
# 셀프 커피바는 벽면 진열장 안, TV 오른쪽 칸(2.0m)에 넣는다. 서쪽 창가는 실제 도면대로 낮은 윈도 진열대 3.86m
# 커피 스테이션: 벽면 진열장의 TV 바로 오른쪽 칸 1.15m (창가는 비운다)
a(f'<rect x="4.25" y="4.74" width="1.15" height="0.5" fill="#d9c2a3" {ADD}/>')
# 관리실 복도는 오른쪽(동쪽)으로만 드나든다. 진열장 왼쪽 끝과 서쪽 벽 사이 틈은 벽으로 막는다
a('<rect x="0.05" y="4.9" width="1.15" height="0.14" fill="#2b2622"/>')
a(f'<rect x="0.05" y="4.68" width="0.71" height="3.86" fill="#f3d9a8" stroke="#b08a3a" stroke-width="0.04"/>')

# 셀프 발마사지 4석: 창고 벽을 등지고 라운지를 본다. 의자 0.85m, 의자 사이 0.4m를 띄우고 그 사이에 사이드 테이블
a('<rect x="0.95" y="8.7" width="4.7" height="1.55" fill="#e6ecdf"/>')
for i in range(4):
    x = 1.0 + 1.25 * i
    a(f'<rect x="{x:.2f}" y="9.38" width="0.85" height="0.85" rx="0.2" fill="#fff" {ADD}/>')
    a(f'<rect x="{x + 0.2:.2f}" y="8.8" width="0.45" height="0.5" rx="0.08" fill="#cfdcc4" {ADD}/>')
for i in range(3):
    a(f'<circle cx="{1.0 + 1.25 * i + 1.05:.2f}" cy="9.8" r="0.17" fill="#e9e1d6" {ADD}/>')
# TV 85인치: 벽면 진열장 가운데 칸, 발마사지 의자 정면(거리 4.2m)
a('<rect x="2.35" y="5.19" width="1.9" height="0.12" fill="#2b2622"/>')
# 쉼 라운지: 긴 모듈 소파 4.4m(7석)가 진열장과 TV를 본다. 동쪽에 1인 암체어 2개가 마주 보고 ㄱ자 응접 자리를 만든다(9석)
a(f'<rect x="1.0" y="6.6" width="4.4" height="0.9" rx="0.25" fill="#fff" {ADD}/>')
for k in range(1, 7):
    a(f'<line x1="{1.0 + 4.4 * k / 7:.2f}" y1="6.68" x2="{1.0 + 4.4 * k / 7:.2f}" y2="7.2" stroke="#2f6b4f" stroke-width="0.03"/>')
a(f'<circle cx="2.3" cy="5.95" r="0.25" fill="#e9e1d6" {ADD}/><circle cx="4.2" cy="5.95" r="0.25" fill="#e9e1d6" {ADD}/>')
# 대기석: 반원으로 휘어진 곡선 소파(5석)가 낮은 테이블을 감싸고, 양 끝에 1인 암체어 2개가 마주 앉는다(7석). 남쪽(안내데스크 진열)으로 열린 응접 자리
a('<path d="M12.44 6.36 A1.3 1.3 0 0 1 14.96 6.36" fill="none" stroke="#2f6b4f" stroke-width="1.0" stroke-linecap="round"/>')
a('<path d="M12.44 6.36 A1.3 1.3 0 0 1 14.96 6.36" fill="none" stroke="#ffffff" stroke-width="0.9" stroke-linecap="round"/>')
a(f'<rect x="11.95" y="7.15" width="0.8" height="0.8" rx="0.3" fill="#fff" {ADD}/><rect x="14.65" y="7.15" width="0.8" height="0.8" rx="0.3" fill="#fff" {ADD}/>')
a(f'<ellipse cx="13.7" cy="6.95" rx="0.7" ry="0.42" fill="#e9e1d6" {ADD}/>')
a(f'<circle cx="13.9" cy="8.98" r="0.2" fill="#fff" {ADD}/><circle cx="14.4" cy="8.98" r="0.2" fill="#fff" {ADD}/><circle cx="14.9" cy="8.98" r="0.2" fill="#fff" {ADD}/>')   # 테스터 스툴 3개
# 브랜드 월: 벽면 진열장 가운데 x 7.2~9.4(2.2m). 유리 자동문(x 7.6~9.0)의 중심 8.3과 한 줄이다
a(f'<rect x="7.2" y="4.74" width="2.2" height="0.5" fill="#8d4b32" {ADD}/>')
a('<line x1="8.3" y1="5.4" x2="8.3" y2="11.2" stroke="#8d4b32" stroke-width="0.04" stroke-dasharray="0.12 0.16"/>')
# 안내데스크: 관리실 4의 모서리를 ㄱ자로 감싸는 곡선 카운터(깊이 0.6). 북쪽 변 3.4m + 서쪽 변 2.3m, 모서리는 둥글게.
# 직원은 카운터와 관리실 4 벽 사이(폭 0.9m)에 선다. 작은 결제 카운터를 대신한다
a(f'<path d="M11.09 11.03 L11.09 10.25 Q11.09 9.35 11.99 9.35 L15.0 9.35 L15.0 9.95 L12.19 9.95 Q11.69 9.95 11.69 10.45 L11.69 11.03 Z" fill="#f3d9a8" {ADD}/>')
a(f'<line x1="13.6" y1="9.35" x2="13.6" y2="9.95" stroke="#2f6b4f" stroke-width="0.05"/>')   # 접수·판매 | 테스터

a(f'<circle cx="12.6" cy="10.4" r="0.2" fill="#e9e1d6" {ADD}/><circle cx="14.2" cy="10.4" r="0.2" fill="#e9e1d6" {ADD}/>')
# 안내데스크 뒷벽(관리실 4의 벽): 벽 전체를 조명 진열장으로. 가운데 칸에 TOMATOK 조명 로고, 양옆 칸에 화장품, 왼쪽 끝 칸에 인증서 액자
# 안내데스크 뒷벽: 벽 4.1m 전체가 화장품 조명 진열장. 가운데 TOMATOK 조명 로고, 문 옆 칸에 인증서
a(f'<rect x="11.2" y="10.72" width="4.1" height="0.3" fill="#f3d9a8" {ADD}/>')
a(f'<rect x="12.6" y="10.7" width="1.3" height="0.34" fill="#8d4b32" {ADD}/>')
# 데스크 서쪽 변은 x 10.2~10.8로 0.6m 들여서 끝을 관리실 4의 모서리에 붙인다. 직원은 오른쪽 끝으로 드나든다
# 파우더룸(1.9 x 4.0, 받은 도면 그대로): 출입문 쪽(동쪽)에 높이 1.8m 창살 벽, 화장대 3석을 그 벽에 붙인다. 뒤(남)는 분전반 벽, 서쪽은 창고 벽
a('<g stroke="#2f6b4f" stroke-width="0.12" stroke-linecap="butt" stroke-dasharray="0.06 0.08"><line x1="7.57" y1="7.93" x2="7.57" y2="11.85"/><line x1="5.67" y1="8.4" x2="5.67" y2="10.25"/></g>')
a(f'<rect x="7.02" y="8.5" width="0.5" height="3.2" fill="#fff" stroke="#a06f78" stroke-width="0.045"/>')
for cy in (9.05, 10.1, 11.15):
    a(f'<circle cx="6.72" cy="{cy}" r="0.2" fill="#fff" stroke="#a06f78" stroke-width="0.035"/>')
# 관리실 안 탈의: 부스 없이 베드 커튼 안에서 갈아입는다. 커튼을 베드 발치까지 ㄱ자로 돌려 베드마다 한 칸을 만든다. 칸마다 2단 락커 1개
def RY(top, flip, y):   # 관리실 4는 문이 반대쪽이라 위아래를 뒤집는다
    return round(top + (3.58 - y), 2) if flip else round(top + y, 2)
for west, c, top, flip in ((0.05, 2.47, 0.0, False), (5.69, 8.12, 0.0, False), (11.09, 13.51, 0.0, False), (11.09, 13.51, 11.03, True)):
    f1, f2, n0 = RY(top, flip, 3.25), RY(top, flip, 2.8), RY(top, flip, 0.12)
    a(f'<polyline points="{west + 0.08},{f1} {c},{f1}" {CUR}/>')                                   # 안쪽 베드: 발치 커튼
    a(f'<polyline points="{c},{f2} {c + 1.98:.2f},{f2} {c + 1.98:.2f},{n0}" {CUR}/>')            # 문 쪽 베드: 발치에서 옆으로 ㄱ자
    for lx, ly in ((west + 0.12, 2.7), (c + 1.42, 2.22)):
        yy = RY(top, flip, ly + 0.5) if flip else RY(top, flip, ly)
        a(f'<rect x="{lx:.2f}" y="{yy}" width="0.5" height="0.5" fill="#d9d2c4" {ADD}/>')
        a(f'<text x="{lx + 0.25:.2f}" y="{yy + 0.33:.2f}" font-size="0.2" fill="#5a4f45" text-anchor="middle">락커</text>')
# 그린: 허리 높이 플랜터로 영역을 나눈다. 대기 소파 뒤 곡선 플랜터(복도 입구와 나눔), 쉼 소파 뒤 긴 플랜터(발마사지와 나눔), 구석 화분
a('<path d="M11.95 6.05 A1.95 1.95 0 0 1 15.45 6.05" fill="none" stroke="#4f7a4a" stroke-width="0.42" stroke-linecap="round"/>')
a('<path d="M11.95 6.05 A1.95 1.95 0 0 1 15.45 6.05" fill="none" stroke="#9db88f" stroke-width="0.32" stroke-linecap="round"/>')
a('<rect x="1.0" y="7.55" width="4.4" height="0.35" rx="0.1" fill="#9db88f" stroke="#4f7a4a" stroke-width="0.05"/>')
for px, py in ((16.15, 5.1), (16.15, 8.9), (10.6, 5.0), (7.2, 7.6)):   # 창가에는 아무것도 두지 않는다
    a(f'<circle cx="{px}" cy="{py}" r="0.25" fill="#9db88f" stroke="#4f7a4a" stroke-width="0.05"/>')
# 대기 소파 위 TV: 체험 대기의 동쪽 벽(안내데스크와 관리실 3 사이). 보른 소파와 테스터 스툴에서 본다
a('<rect x="16.36" y="6.55" width="0.1" height="1.9" fill="#2b2622"/>')
a('<text x="16.2" y="7.3" font-size="0.26" fill="#5a4f45" text-anchor="middle" transform="rotate(-90 16.2 7.3)">TV</text>')
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
# 자동문은 실제 도면에서 x 7.6~9.0(폭 1.4m). 미닫이라 유리면을 따라 옆으로 열린다. 여는 방향은 도면에 없다
a(f'<rect x="7.6" y="{Y(gd["y"] + gd["d"]) - 0.03}" width="1.4" height="{gd["d"] + 0.06}" fill="#ffffff" stroke="#5f7f8c" stroke-width="0.05"/>')
a(f'<path d="M8.3 {Y(gd["y"]) + 0.42} h1.5 m0 0 l-0.25 -0.13 m0.25 0.13 l-0.25 0.13" fill="none" stroke="#5f7f8c" stroke-width="0.05"/>')
# 파우더룸과 맞닿은 유리 1.9m는 아래 1.2m만 불투명으로 한다
a(f'<rect x="5.67" y="{Y(gd["y"] + gd["d"]) - 0.02}" width="1.9" height="{gd["d"] + 0.04}" fill="#2b2622"/>')   # 현장 사진 확인: 파우더룸 뒤는 유리가 아니라 벽(분전반이 있다)
# 파우더룸 뒤(남쪽)는 벽이다


# 문: 방의 한 변에서 at 비율 위치에 폭 0.9m
a('<g>')
for z in zones:
    for dr in z.get('doors', []):
        if z['n'] in ('구획벽',) or z['g'] in ('circ',) or z['x'] > 16.5:
            continue
        s, t = dr['side'], dr['at']
        if s in ('N', 'S'):
            cx = z['x'] + t * z['w']; yy = Y(z['y'] + z['d']) if s == 'N' else Y(z['y'])
            x1 = max(z['x'] + 0.1, min(cx - 0.45, z['x'] + z['w'] - 1.0)); x2 = x1 + 0.9
            a(f'<line x1="{x1:.2f}" y1="{yy}" x2="{x2:.2f}" y2="{yy}" stroke="#f6f1ea" stroke-width="0.2"/>')
            inward = 1 if s == 'N' else -1      # 방 안쪽으로 열리는 방향(SVG y)
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
for x, y, t in ((2.9, 14.5, '관리실 1'), (8.4, 14.5, '관리실 2'), (13.8, 14.5, '관리실 3'), (13.8, 5.2, '관리실 4'),
                (8.3, 13.25, '관리실 복도'), (8.9, 9.7, 'VIP 라운지'), (13.4, 8.6, '체험 대기'),
                (6.3, 7.15, '파우더룸'), (2.8, 6.3, '린넨·소독·재고'), (9.15, 4.55, 'EV 홀'),
                (18.4, 10.0, '사무 구역'), (1.35, 4.3, '남 화장실'), (1.25, 1.5, '여 화장실'), (5.35, 1.6, '계단'), (8.3, 1.3, '승강기')):
    a(f'<text x="{x}" y="{Y(y)}">{t}</text>')
a('</g>')
a('<g font-size="0.3" fill="#5a4f45" text-anchor="middle">')
for x, y, t in ((7.0, 12.95, ''), (8.3, 11.9, '브랜드 월'), (14.6, 6.4, '인증서'), (11.85, 6.4, '화장품'), (13.25, 6.4, '로고'), (10.2, 7.7, '안내데스크'), (12.6, 7.7, '접수·판매'), (14.3, 7.7, '테스터'), (3.3, 11.85, 'TV'), (3.3, 9.05, '셀프 발마사지 4석'),  (3.2, 10.45, '쉼 라운지'), 

                (8.3, 4.95, '유리 자동문'), (9.15, 4.1, '고객 출입'), (6.3, 6.6, '화장대 3석'),   (18.4, 9.45, '(별도 구역)'),
                (5.42, 14.95, '세면')):
    a(f'<text x="{x}" y="{Y(y)}">{t}</text>')
a(f'<text x="0.44" y="6.6" transform="rotate(-90 0.44 6.6)">윈도 진열대</text>')
a(f'<text x="4.82" y="5.55">커피</text>')

a('</g>')

# 카메라 (아직 이미지 없음)
cams = ((8.3, 6.3, 0), (6.6, 10.1, 250), (15.9, 9.3, 300), (9.0, 14.4, 30))
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
for y, t in ((15.7, '3.47'), (13.4, '1.21'), (9.2, '7.17'), (4.2, '2.76')):
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
