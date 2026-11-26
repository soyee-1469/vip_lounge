"use client";

import type { KeyboardEvent } from "react";
import { PLAN, cameras, zones, type Flow } from "@/lib/shop";

type Props = {
  markup: string;
  conceptId: string;
  zoneId: string;
  cameraId: string | null;
  /** 어느 컨셉에든 이미지가 있는 카메라 */
  camerasWithImage: Set<string>;
  flow: Flow | null;
  onSelectZone: (zoneId: string) => void;
  onSelectCamera: (cameraId: string) => void;
};

function activate(run: () => void) {
  return (event: KeyboardEvent) => {
    if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      run();
    }
  };
}

export function PlanMap({
  markup,
  conceptId,
  zoneId,
  cameraId,
  camerasWithImage,
  flow,
  onSelectZone,
  onSelectCamera,
}: Props) {
  return (
    <svg
      viewBox={PLAN.viewBox}
      className="block w-full rounded-md border border-line bg-white"
      role="group"
      aria-label="매장 평면도. 구역이나 카메라를 누르면 설명이 열립니다."
    >
      <g dangerouslySetInnerHTML={{ __html: markup }} />

      <g>
        {zones.filter((zone) => !zone.only || zone.only === conceptId).map((zone) => {
          const selected = zone.id === zoneId;
          return (
            <g
              key={zone.id}
              role="button"
              tabIndex={0}
              aria-label={`${zone.name} 구역`}
              aria-pressed={selected}
              className="cursor-pointer outline-none [&:focus-visible>rect]:stroke-ink"
              onClick={() => onSelectZone(zone.id)}
              onKeyDown={activate(() => onSelectZone(zone.id))}
            >
              <title>{zone.name}</title>
              {zone.rects.map(([x, y, w, h], index) => (
                <rect
                  key={`${index}-${x}-${y}`}
                  x={x}
                  y={y}
                  width={w}
                  height={h}
                  rx={0.12}
                  strokeWidth={selected ? 0.16 : 0.07}
                  className={
                    selected
                      ? "fill-copper/30 stroke-copper"
                      : "fill-transparent stroke-transparent transition-colors hover:fill-copper/10 hover:stroke-copper/70"
                  }
                />
              ))}
              {selected ? (
                <g pointerEvents="none">
                  {(() => {
                    const [x, y, w, h] = zone.rects[0];
                    const label = zone.name;
                    const width = Math.max(1.6, label.length * 0.28 + 0.35);
                    const left = x + w / 2 - width / 2;
                    const top = y + 0.12;
                    return (
                      <g>
                        <rect x={left} y={top} width={width} height={0.48} rx={0.08} fill="#8d4b32" />
                        <text
                          x={left + width / 2}
                          y={top + 0.33}
                          fontSize={0.26}
                          fontWeight={700}
                          fill="#fff"
                          textAnchor="middle"
                        >
                          {label}
                        </text>
                      </g>
                    );
                  })()}
                </g>
              ) : null}
            </g>
          );
        })}
      </g>

      {flow ? (
        <g pointerEvents="none">
          {flow.lines.map((line, index) => (
            <polyline
              key={index}
              points={line.map(([x, y]) => `${x},${y}`).join(" ")}
              fill="none"
              stroke={flow.color}
              strokeWidth={0.11}
              strokeLinejoin="round"
              strokeLinecap="round"
              strokeDasharray="0.02 0.24"
            />
          ))}
          {flow.stops.map((stop, index) => (
            <g key={stop.label} transform={`translate(${stop.x} ${stop.y})`}>
              <rect x={-0.2} y={-0.2} width={0.4} height={0.4} rx={0.08} fill={flow.color} />
              <text y={0.1} fontSize={0.27} fontWeight={700} fill="#fff" textAnchor="middle">
                {index + 1}
              </text>
            </g>
          ))}
        </g>
      ) : null}

      {/* 동선을 볼 때는 번호가 겹치지 않게 카메라를 숨긴다 */}
      <g display={flow ? "none" : undefined}>
        {cameras.map((camera) => {
          const selected = camera.id === cameraId;
          const dim = !camerasWithImage.has(camera.id);
          return (
            <g
              key={camera.id}
              role="button"
              tabIndex={0}
              aria-label={`카메라 ${camera.no} ${camera.label}${dim ? " (이미지 없음)" : ""}`}
              aria-pressed={selected}
              className="cursor-pointer outline-none [&:focus-visible>circle]:stroke-ink"
              opacity={dim && !selected ? 0.4 : 1}
              transform={`translate(${camera.x} ${camera.y})`}
              onClick={() => onSelectCamera(camera.id)}
              onKeyDown={activate(() => onSelectCamera(camera.id))}
            >
              <title>{`${camera.no}. ${camera.label}`}</title>
              <path
                d="M0 0 L-0.55 -1.15 L0.55 -1.15 Z"
                transform={`rotate(${camera.heading})`}
                fill={selected ? "#8d4b32" : "#8a7d70"}
                opacity={selected ? 0.85 : 0.25}
              />
              <circle
                r={selected ? 0.42 : 0.3}
                fill={selected ? "#8d4b32" : "#8a7d70"}
                stroke="#fff"
                strokeWidth={selected ? 0.1 : 0.05}
              />
              <text y={0.12} fontSize={selected ? 0.36 : 0.3} fontWeight={700} fill="#fff" textAnchor="middle" pointerEvents="none">
                {camera.no}
              </text>
              {selected ? (
                <g pointerEvents="none">
                  <rect
                    x={0.55}
                    y={-0.28}
                    width={camera.label.length * 0.24 + 0.4}
                    height={0.5}
                    rx={0.08}
                    fill="#1c1915"
                  />
                  <text x={0.72} y={0.08} fontSize={0.26} fontWeight={700} fill="#fff">
                    {camera.label}
                  </text>
                </g>
              ) : null}
            </g>
          );
        })}
      </g>
    </svg>
  );
}
