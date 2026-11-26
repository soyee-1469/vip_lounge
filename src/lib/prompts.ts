import { styles } from "./catalog";
import type { Camera, Concept } from "./types";

export function conceptLock(concept: Concept) {
  const style = styles[concept.styleId];
  const furniture = concept.furniture
    .map((item) => `${item.label}: ${item.placement}`)
    .join("; ");

  return [
    `One ${concept.spaceLabel} interior, about ${concept.widthM}m wide by ${concept.depthM}m deep.`,
    style.look,
    `Materials: ${concept.materials.join(", ")}.`,
    `Furniture lock: ${furniture}.`,
    "Keep this exact furniture set, material, and color. Do not add people, text, logos, or extra rooms.",
  ].join(" ");
}

export function viewPrompt(concept: Concept, camera: Camera, hasReference: boolean) {
  const reference = hasReference
    ? "The attached photo is the same room. Match its materials, furniture design, and colors. Change only the camera."
    : "This is the first photograph of the room. Later angles must be able to match it.";

  return [
    "Photorealistic architectural interior photograph, 35mm lens, eye level 1.5m, natural light, no stylization.",
    conceptLock(concept),
    `Camera "${camera.label}": ${camera.detail}.`,
    reference,
  ].join(" ");
}
