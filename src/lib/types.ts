export type SpaceId = "living" | "bedroom" | "kitchen";
export type StyleId = "modern" | "nordic" | "japandi" | "midcentury";
export type Edge = "n" | "s" | "e" | "w";

export type Furniture = {
  id: string;
  label: string;
  placement: string;
  x: number;
  y: number;
  w: number;
  h: number;
};

export type Opening = {
  edge: Edge;
  kind: "window" | "door";
  from: number;
  to: number;
};

export type Camera = {
  id: string;
  label: string;
  detail: string;
  x: number;
  y: number;
  heading: number;
};

export type Concept = {
  title: string;
  narrative: string;
  materials: string[];
  palette: string[];
  spaceId: SpaceId;
  styleId: StyleId;
  spaceLabel: string;
  styleLabel: string;
  area: number;
  widthM: number;
  depthM: number;
  furniture: Furniture[];
  openings: Opening[];
  cameras: Camera[];
  enriched: boolean;
};

export type Brief = {
  spaceId: SpaceId;
  styleId: StyleId;
  area: number;
  note: string;
};

export type ViewImage = {
  mediaType: string;
  base64: string;
};
