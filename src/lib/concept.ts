import { spaces, styles } from "./catalog";
import type { Brief, Concept } from "./types";

export function roomMeters(area: number, aspect: number) {
  const width = Math.sqrt(area * aspect);
  const depth = area / width;
  return {
    widthM: Math.round(width * 10) / 10,
    depthM: Math.round(depth * 10) / 10,
  };
}

export function composeConcept(brief: Brief): Concept {
  const space = spaces[brief.spaceId];
  const style = styles[brief.styleId];
  const meters = roomMeters(brief.area, space.aspect);
  const note = brief.note.trim();

  return {
    title: `${style.label} ${space.label}`,
    narrative: note
      ? `${brief.area}㎡ ${space.label}. ${style.intent} ${note}`
      : `${brief.area}㎡ ${space.label}. ${style.intent} ${space.summary}.`,
    materials: style.materials,
    palette: style.palette,
    spaceId: brief.spaceId,
    styleId: brief.styleId,
    spaceLabel: space.label,
    styleLabel: style.label,
    area: brief.area,
    widthM: meters.widthM,
    depthM: meters.depthM,
    furniture: space.furniture,
    openings: space.openings,
    cameras: space.cameras,
    enriched: false,
  };
}

export function specKey(concept: Concept) {
  return [
    concept.spaceId,
    concept.styleId,
    concept.area,
    concept.narrative,
    concept.materials.join("|"),
  ].join("::");
}
