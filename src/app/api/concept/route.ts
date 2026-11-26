import { generateText, Output } from "ai";
import { z } from "zod";
import { composeConcept } from "@/lib/concept";
import type { Brief } from "@/lib/types";

export const maxDuration = 60;

const briefSchema = z.object({
  spaceId: z.enum(["living", "bedroom", "kitchen"]),
  styleId: z.enum(["modern", "nordic", "japandi", "midcentury"]),
  area: z.number().min(12).max(80),
  note: z.string().max(280),
});

const copySchema = z.object({
  title: z.string().min(2).max(40),
  narrative: z.string().min(20).max(280),
  materials: z.array(z.string().min(2).max(24)).length(4),
});

export async function POST(request: Request) {
  if (!process.env.AI_GATEWAY_API_KEY && !process.env.VERCEL_OIDC_TOKEN) {
    return Response.json(
      { error: "AI_GATEWAY_API_KEY가 없어 기획 문장은 기본 사양으로 유지됩니다." },
      { status: 503 },
    );
  }

  let brief: Brief;
  try {
    const json = await request.json();
    brief = briefSchema.parse(json);
  } catch {
    return Response.json({ error: "기획 입력을 확인해주세요." }, { status: 400 });
  }

  const base = composeConcept(brief);
  const furniture = base.furniture.map((item) => `${item.label} (${item.placement})`).join(", ");

  try {
    const result = await generateText({
      model: "google/gemini-3.8-flash",
      output: Output.object({ schema: copySchema }),
      prompt: [
        "인테리어 기획 문장을 한국어로 다듬어라.",
        "도면의 가구 배치와 개수는 바꾸지 마라. 재료 4개는 스타일에 맞게 구체적으로.",
        `공간: ${base.spaceLabel}, ${base.widthM}m x ${base.depthM}m, ${base.area}㎡`,
        `스타일: ${base.styleLabel}`,
        `고정 가구: ${furniture}`,
        `메모: ${brief.note || "없음"}`,
      ].join("\n"),
    });

    if (!result.output) {
      return Response.json({ error: "기획 문장을 만들지 못했습니다." }, { status: 502 });
    }

    return Response.json({
      title: result.output.title,
      narrative: result.output.narrative,
      materials: result.output.materials,
    });
  } catch {
    return Response.json({ error: "기획 문장 생성에 실패했습니다." }, { status: 502 });
  }
}
