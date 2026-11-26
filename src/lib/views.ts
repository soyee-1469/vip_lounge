import { readdirSync, readFileSync } from "node:fs";
import path from "node:path";
import { concepts } from "@/lib/shop";

/** 컨셉 id → 카메라 id → 이미지 URL */
export type ViewIndex = Record<string, Record<string, string>>;

const IMAGE_EXT = new Set([".jpg", ".jpeg", ".png", ".webp"]);

/** public/views/<컨셉>/ 폴더를 읽어 어떤 시점 이미지가 있는지 알아낸다. */
export function listViews(): ViewIndex {
  const index: ViewIndex = {};
  for (const concept of concepts) {
    index[concept.id] = {};
    let names: string[] = [];
    try {
      names = readdirSync(path.join(process.cwd(), "public", "views", concept.id));
    } catch {
      continue;
    }
    for (const name of names.sort()) {
      const ext = path.extname(name).toLowerCase();
      if (!IMAGE_EXT.has(ext)) continue;
      const cameraId = path.basename(name, path.extname(name));
      index[concept.id][cameraId] ??= `/views/${concept.id}/${name}`;
    }
  }
  return index;
}

/**
 * 도면 SVG의 안쪽 마크업만 꺼낸다. 제목, 미리 그려 둔 카메라와 범례는 앱이 대신 그리므로 뺀다.
 * make_plan.py가 요소를 한 줄에 하나씩 쓰기 때문에 줄 단위로 걸러낸다.
 */
/** 컨셉 id → 도면 마크업. 컨셉마다 배치가 달라 도면도 따로다. */
export function loadPlanMarkups(): Record<string, string> {
  return Object.fromEntries(concepts.map((c) => [c.id, loadPlanMarkup(c.id)]));
}

export function loadPlanMarkup(conceptId: string): string {
  const file = path.join(process.cwd(), "public", "plan", `floor-plan-${conceptId}.svg`);
  const lines = readFileSync(file, "utf8").split("\n");
  const kept: string[] = [];
  let skipUntil: string | null = null;
  for (const line of lines) {
    if (skipUntil) {
      if (line === skipUntil) skipUntil = null;
      continue;
    }
    if (line.startsWith("<svg") || line === "</svg>") continue;
    if (line.startsWith('<rect x="-1.6"')) continue;
    if (line.includes("매장 평면도 (") || line.includes("가정값이고")) continue;
    if (line.startsWith('<g id="cameras">')) {
      skipUntil = "</g></g>";
      continue;
    }
    if (line.startsWith('<g id="legend"')) {
      skipUntil = "</g>";
      continue;
    }
    kept.push(line);
  }
  return kept.join("\n");
}
