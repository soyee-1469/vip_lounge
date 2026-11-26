import type { Camera, Furniture, Opening, SpaceId, StyleId } from "./types";

export const spaces: Record<
  SpaceId,
  {
    label: string;
    aspect: number;
    summary: string;
    furniture: Furniture[];
    openings: Opening[];
    cameras: Camera[];
  }
> = {
  living: {
    label: "거실",
    aspect: 1.55,
    summary: "남쪽에 소파, 북쪽에 창과 TV, 입구는 남서쪽",
    openings: [
      { edge: "n", kind: "window", from: 0.18, to: 0.82 },
      { edge: "s", kind: "door", from: 0.08, to: 0.2 },
    ],
    furniture: [
      { id: "sofa", label: "소파", placement: "남쪽 벽 중앙, 창을 바라봄", x: 28, y: 68, w: 44, h: 18 },
      { id: "table", label: "테이블", placement: "소파 앞 중앙", x: 38, y: 48, w: 24, h: 16 },
      { id: "tv", label: "TV장", placement: "북쪽 창 아래 벽", x: 34, y: 8, w: 32, h: 10 },
      { id: "chair", label: "암체어", placement: "서쪽, 소파를 비스듬히 봄", x: 8, y: 42, w: 16, h: 16 },
      { id: "side", label: "사이드보드", placement: "동쪽 벽", x: 78, y: 36, w: 14, h: 28 },
    ],
    cameras: [
      { id: "entry", label: "입구", detail: "남서쪽 문 안쪽에서 북동쪽 창 모서리를 바라봄", x: 18, y: 78, heading: 32 },
      { id: "sofa", label: "소파 정면", detail: "TV장 앞에서 남쪽 소파를 정면으로 바라봄", x: 50, y: 28, heading: 180 },
      { id: "window", label: "창가", detail: "북쪽 창 앞에서 방을 가로질러 동쪽을 바라봄", x: 42, y: 16, heading: 90 },
      { id: "corner", label: "코너", detail: "남동쪽 코너에서 소파와 창을 함께 바라봄", x: 78, y: 74, heading: 318 },
    ],
  },
  bedroom: {
    label: "침실",
    aspect: 1.25,
    summary: "북쪽 침대, 동쪽 창, 서쪽 옷장, 남쪽 문",
    openings: [
      { edge: "e", kind: "window", from: 0.22, to: 0.7 },
      { edge: "s", kind: "door", from: 0.72, to: 0.88 },
    ],
    furniture: [
      { id: "bed", label: "침대", placement: "북쪽 벽 중앙, 헤드보드가 벽에 붙음", x: 28, y: 8, w: 44, h: 34 },
      { id: "left", label: "협탁", placement: "침대 왼쪽", x: 16, y: 14, w: 10, h: 12 },
      { id: "right", label: "협탁", placement: "침대 오른쪽", x: 74, y: 14, w: 10, h: 12 },
      { id: "wardrobe", label: "옷장", placement: "서쪽 벽", x: 6, y: 48, w: 14, h: 32 },
      { id: "bench", label: "벤치", placement: "침대 발치", x: 36, y: 48, w: 28, h: 10 },
    ],
    cameras: [
      { id: "entry", label: "입구", detail: "남쪽 문에서 침대 헤드보드를 바라봄", x: 70, y: 82, heading: 350 },
      { id: "foot", label: "침대 발치", detail: "벤치 앞에서 침대를 정면으로 바라봄", x: 50, y: 66, heading: 0 },
      { id: "window", label: "창가", detail: "동쪽 창 옆에서 침대와 옷장을 바라봄", x: 82, y: 46, heading: 250 },
      { id: "corner", label: "코너", detail: "남서쪽 코너에서 침대와 창을 함께 바라봄", x: 22, y: 78, heading: 28 },
    ],
  },
  kitchen: {
    label: "주방·다이닝",
    aspect: 1.7,
    summary: "북쪽 조리대, 중앙 아일랜드, 남쪽 식탁, 동쪽 창",
    openings: [
      { edge: "e", kind: "window", from: 0.12, to: 0.55 },
      { edge: "w", kind: "door", from: 0.62, to: 0.78 },
    ],
    furniture: [
      { id: "counter", label: "조리대", placement: "북쪽 벽 전체", x: 8, y: 6, w: 84, h: 14 },
      { id: "island", label: "아일랜드", placement: "주방 중앙", x: 30, y: 30, w: 36, h: 18 },
      { id: "chairs", label: "의자", placement: "식탁 주변", x: 28, y: 60, w: 44, h: 28 },
      { id: "table", label: "식탁", placement: "남쪽 다이닝", x: 34, y: 64, w: 32, h: 20 },
    ],
    cameras: [
      { id: "entry", label: "입구", detail: "서쪽 문에서 식탁과 창을 바라봄", x: 12, y: 70, heading: 48 },
      { id: "island", label: "아일랜드", detail: "아일랜드 남쪽에서 북쪽 조리대를 바라봄", x: 48, y: 54, heading: 0 },
      { id: "dining", label: "식탁", detail: "식탁 동쪽 끝에서 식탁 길이를 바라봄", x: 72, y: 74, heading: 270 },
      { id: "window", label: "창가", detail: "동쪽 창 앞에서 아일랜드와 식탁을 바라봄", x: 86, y: 34, heading: 230 },
    ],
  },
};

export const styles: Record<
  StyleId,
  {
    label: string;
    intent: string;
    look: string;
    materials: string[];
    palette: string[];
  }
> = {
  modern: {
    label: "모던",
    intent: "선을 줄이고 따뜻한 회색과 오크로 무게를 낮춥니다.",
    look: "warm modern interior, limewashed plaster, wide oak floor, blackened steel, linen, quiet daylight",
    materials: ["웜 그레이 미장", "와이드 오크 바닥", "블랙 스틸", "리넨 패브릭"],
    palette: ["#e7e1d6", "#8d8a84", "#c4a484", "#1c1915"],
  },
  nordic: {
    label: "북유럽",
    intent: "하얀 벽과 옅은 나무, 울 텍스타일로 빛을 퍼뜨립니다.",
    look: "scandinavian interior, white walls, ash wood, wool textiles, pale oak, soft north light",
    materials: ["화이트 벽", "애쉬 바닥", "울 러그", "라이트 우드"],
    palette: ["#f7f4ee", "#d7c4a3", "#8fa398", "#4d463d"],
  },
  japandi: {
    label: "재팬디",
    intent: "낮은 가구와 회벽, 월넛으로 여백을 남깁니다.",
    look: "japandi interior, clay plaster, walnut, low furniture, paper lantern light, matte textures",
    materials: ["회벽", "월넛", "한지 조명", "리넨"],
    palette: ["#efe6d6", "#8c6a43", "#5e6a62", "#2a2622"],
  },
  midcentury: {
    label: "미드센추리",
    intent: "월넛 다리와 테라조, 머스타드 포인트로 시대감을 줍니다.",
    look: "mid-century modern interior, walnut tapered legs, terrazzo, mustard accent, brass, warm lamp light",
    materials: ["월넛", "테라조", "머스타드 패브릭", "브라스"],
    palette: ["#f3e6cf", "#c47b2d", "#6e8b74", "#3a2a22"],
  },
};

export const spaceOrder: SpaceId[] = ["living", "bedroom", "kitchen"];
export const styleOrder: StyleId[] = ["modern", "nordic", "japandi", "midcentury"];
