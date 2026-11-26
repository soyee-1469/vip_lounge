import { generateText } from "ai";
import { z } from "zod";
import { viewPrompt } from "@/lib/prompts";
import type { Concept } from "@/lib/types";

export const maxDuration = 60;

const conceptSchema = z.object({
  title: z.string(),
  narrative: z.string(),
  materials: z.array(z.string()).min(1).max(8),
  palette: z.array(z.string()),
  spaceId: z.enum(["living", "bedroom", "kitchen"]),
  styleId: z.enum(["modern", "nordic", "japandi", "midcentury"]),
  spaceLabel: z.string(),
  styleLabel: z.string(),
  area: z.number(),
  widthM: z.number(),
  depthM: z.number(),
  furniture: z.array(
    z.object({
      id: z.string(),
      label: z.string(),
      placement: z.string(),
      x: z.number(),
      y: z.number(),
      w: z.number(),
      h: z.number(),
    }),
  ),
  openings: z.array(
    z.object({
      edge: z.enum(["n", "s", "e", "w"]),
      kind: z.enum(["window", "door"]),
      from: z.number(),
      to: z.number(),
    }),
  ),
  cameras: z.array(
    z.object({
      id: z.string(),
      label: z.string(),
      detail: z.string(),
      x: z.number(),
      y: z.number(),
      heading: z.number(),
    }),
  ),
  enriched: z.boolean(),
});

const bodySchema = z.object({
  concept: conceptSchema,
  cameraId: z.string(),
  reference: z
    .object({
      base64: z.string().min(32),
      mediaType: z.string().regex(/^image\//),
    })
    .optional(),
});

export async function POST(request: Request) {
  if (!process.env.AI_GATEWAY_API_KEY && !process.env.VERCEL_OIDC_TOKEN) {
    return Response.json(
      { error: "시점 이미지를 만들려면 AI_GATEWAY_API_KEY가 필요합니다." },
      { status: 503 },
    );
  }

  let body: z.infer<typeof bodySchema>;
  try {
    body = bodySchema.parse(await request.json());
  } catch {
    return Response.json({ error: "시점 요청을 확인해주세요." }, { status: 400 });
  }

  const concept = body.concept as Concept;
  const camera = concept.cameras.find((item) => item.id === body.cameraId);
  if (!camera) {
    return Response.json({ error: "도면에 없는 시점입니다." }, { status: 400 });
  }

  const prompt = viewPrompt(concept, camera, Boolean(body.reference));
  const content = [
    { type: "text" as const, text: prompt },
    ...(body.reference
      ? [
          {
            type: "file" as const,
            mediaType: body.reference.mediaType,
            data: body.reference.base64,
          },
        ]
      : []),
  ];

  try {
    const result = await generateText({
      model: "google/gemini-3.1-flash-image",
      messages: [{ role: "user", content }],
    });
    const file = result.files.find((item) => item.mediaType.startsWith("image/"));
    if (!file) {
      return Response.json({ error: "모델이 이미지를 반환하지 않았습니다." }, { status: 502 });
    }

    return Response.json({ mediaType: file.mediaType, base64: file.base64 });
  } catch {
    return Response.json({ error: "시점 이미지 생성에 실패했습니다." }, { status: 502 });
  }
}
