"use client";

import { useSearchParams } from "next/navigation";
import { PlanMap } from "@/components/plan-map";
import {
  cameras,
  concepts,
  flows,
  openIssues,
  principles,
  zones,
  type Camera,
  type ConceptId,
  type ShopConcept,
} from "@/lib/shop";
import type { ViewIndex } from "@/lib/views";

type Props = {
  planMarkup: Record<string, string>;
  views: ViewIndex;
};

export function Viewer({ planMarkup, views }: Props) {
  const params = useSearchParams();

  const concept =
    concepts.find((item) => item.id === params.get("concept")) ?? concepts[0];
  const compare = params.get("compare") === "1";
  const flow = flows.find((item) => item.id === params.get("flow")) ?? null;
  const zoneList = zones.filter((item) => !item.only || item.only === concept.id);
  const zone = zoneList.find((item) => item.id === params.get("zone")) ?? zoneList[0];

  const hasImage = (cameraId: string, conceptId: ConceptId = concept.id) =>
    Boolean(views[conceptId]?.[cameraId]);
  const zoneCameras = zone.cameraIds
    .map((id) => cameras.find((camera) => camera.id === id))
    .filter((camera): camera is Camera => Boolean(camera));
  const requested = zoneCameras.find(
    (camera) => camera.id === params.get("cam"),
  );
  const camera =
    requested ??
    zoneCameras.find((item) => hasImage(item.id)) ??
    zoneCameras[0] ??
    null;

  const camerasWithImage = new Set(
    cameras
      .filter((item) => concepts.some((c) => hasImage(item.id, c.id)))
      .map((item) => item.id),
  );

  const aerialViews = [
    { key: "1", id: "aerial", label: "입구 쪽에서" },
    { key: "left", id: "aerial-left", label: "창가 쪽에서" },
    { key: "right", id: "aerial-right", label: "안내데스크 쪽에서" },
    { key: "back", id: "aerial-back", label: "관리실 쪽에서" },
  ].filter((item) => views[concept.id]?.[item.id]);
  const aerialView = aerialViews.find((item) => item.key === params.get("aerial"));
  const aerialSrc = aerialView ? views[concept.id]?.[aerialView.id] : undefined;
  const showAerial = Boolean(aerialSrc);

  function update(changes: Record<string, string | null>) {
    const next = new URLSearchParams(window.location.search);
    for (const [key, value] of Object.entries(changes)) {
      if (value === null) next.delete(key);
      else next.set(key, value);
    }
    const query = next.toString();
    window.history.replaceState(
      null,
      "",
      query ? `?${query}` : window.location.pathname,
    );
  }

  const shown = compare ? concepts : [concept];

  return (
    <div className="min-h-full bg-paper text-ink">
      <header className="border-b border-line px-5 py-4 md:px-8">
        <div className="mx-auto flex max-w-[1760px] flex-wrap items-end justify-between gap-4">
          <div>
            <p className="text-xs tracking-[0.22em] text-muted uppercase">
              VIP Interior
            </p>
            <h1 className="text-2xl leading-tight font-medium text-balance md:text-3xl">
              TOMATOK VIP LOUNGE 배치안
            </h1>
            <p className="mt-1 text-sm text-muted">
              도면을 누르면 오른쪽 사진이 열립니다. 컨셉 1안과 2안은 제목 옆 버튼으로 바꿉니다.
            </p>
          </div>
                <div className="flex w-fit overflow-hidden rounded-md border border-ink text-sm" role="group" aria-label="컨셉">
                  {concepts.map((item, index) => (
                    <button
                      key={item.id}
                      type="button"
                      aria-pressed={item.id === concept.id && !compare}
                      onClick={() => update({ concept: item.id, compare: null })}
                      className={`px-4 py-2 ${
                        item.id === concept.id && !compare ? "bg-ink text-paper" : "bg-panel"
                      }`}
                    >
                      컨셉 {index + 1}안
                    </button>
                  ))}
                </div>
        </div>
      </header>

      <main className="mx-auto max-w-[1760px] px-5 py-6 md:px-8">
        <div className="grid items-start gap-8 lg:grid-cols-[minmax(0,5fr)_minmax(0,6fr)]">
          <section className="min-w-0 lg:sticky lg:top-4" aria-label="평면도">
            {showAerial && aerialSrc ? (
              // eslint-disable-next-line @next/next/no-img-element
              <img
                src={aerialSrc}
                alt="전체 항공뷰"
                className="block w-full rounded-md border border-line bg-white"
              />
            ) : null}
            {showAerial ? (
              <div className="mt-2 flex flex-wrap gap-2 text-sm">
                {aerialViews.map((item) => (
                  <button
                    key={item.key}
                    type="button"
                    aria-pressed={aerialView?.key === item.key}
                    onClick={() => update({ aerial: item.key })}
                    className={`rounded-md border px-3 py-1.5 ${
                      aerialView?.key === item.key ? "border-ink bg-ink text-paper" : "border-line bg-panel"
                    }`}
                  >
                    {item.label}
                  </button>
                ))}
              </div>
            ) : null}
            <div className={showAerial ? "hidden" : ""}>
            <PlanMap
              markup={planMarkup[concept.id] ?? ""}
              conceptId={concept.id}
              zoneId={zone.id}
              cameraId={camera?.id ?? null}
              camerasWithImage={camerasWithImage}
              flow={flow}
              onSelectZone={(id) => update({ zone: id, cam: null })}
              onSelectCamera={(id) => {
                const target = cameras.find((item) => item.id === id);
                if (target) update({ zone: target.zoneId, cam: id });
              }}
            />
            </div>
            <div className="mt-3 flex flex-wrap items-center gap-2 text-sm">
              <button
                type="button"
                aria-pressed={showAerial}
                onClick={() => update({ aerial: showAerial ? null : "1" })}
                className={`rounded-md border px-3 py-1.5 font-medium ${
                  showAerial ? "border-ink bg-ink text-paper" : "border-ink bg-panel"
                }`}
              >
                {showAerial ? "도면으로 돌아가기" : "전체 항공뷰 보기"}
              </button>
              <a
                href="/tomatok-3d.html"
                target="_blank"
                rel="noreferrer"
                className="rounded-md border border-ink bg-panel px-3 py-1.5 font-medium"
              >
                3D 도면 보기
              </a>
              <span className="ml-2 text-muted">동선 표시</span>
              {flows.map((item) => (
                <button
                  key={item.id}
                  type="button"
                  aria-pressed={flow?.id === item.id}
                  onClick={() =>
                    update({ flow: flow?.id === item.id ? null : item.id })
                  }
                  className="flex items-center gap-2 rounded-md border px-3 py-1.5"
                  style={
                    flow?.id === item.id
                      ? {
                          borderColor: item.color,
                          background: item.color,
                          color: "#fff",
                        }
                      : {
                          borderColor: "var(--line)",
                          background: "var(--panel)",
                        }
                  }
                >
                  <span
                    className="h-2 w-2 rounded-sm"
                    style={{
                      background: flow?.id === item.id ? "#fff" : item.color,
                    }}
                  />
                  {item.label}
                </button>
              ))}
            </div>
            {flow ? (
              <div className="mt-3 text-sm leading-6">
                <ol className="flex flex-wrap gap-x-3 gap-y-1">
                  {flow.stops.map((stop, index) => (
                    <li key={stop.label} className="flex items-center gap-1.5">
                      <span
                        className="grid h-5 w-5 place-items-center rounded-sm text-xs text-white"
                        style={{ background: flow.color }}
                      >
                        {index + 1}
                      </span>
                      {stop.label}
                    </li>
                  ))}
                </ol>
                <p className="mt-1 text-muted">{flow.note}</p>
              </div>
            ) : (
              <p className="mt-3 text-sm leading-6 text-muted">
                2026-11-26에 받은 실제 도면입니다. 2층의 왼쪽 16.5m가 고객
                구역(VIP 라운지 101.5㎡와 관리실 4개)이고, 오른쪽은 사무
                구역입니다. 번호는 이미지를 찍을 카메라 위치이고, 흐린 번호는
                아직 이미지가 없는 시점입니다.
              </p>
            )}
          </section>

          <section
            className="min-w-0 border-t border-line pt-8"
            aria-label="선택한 구역"
            aria-live="polite"
          >
            <div className="grid gap-y-6">
              <div className="min-w-0">
                <p className="text-sm text-muted">{zone.where}</p>
                <h2 className="text-2xl font-medium">{zone.name}</h2>
                <p className="mt-1 text-sm">{zone.size}</p>

                {zoneCameras.length > 1 ? (
                  <div className="mt-3 flex flex-wrap gap-2 text-sm">
                    {zoneCameras.map((item) => (
                      <button
                        key={item.id}
                        type="button"
                        aria-pressed={item.id === camera?.id}
                        onClick={() => update({ cam: item.id })}
                        className={`rounded-full border px-3 py-1 ${
                          item.id === camera?.id
                            ? "border-ink bg-ink text-paper"
                            : "border-line bg-panel"
                        }`}
                      >
                        {item.no}. {item.label}
                        {hasImage(item.id) ? "" : " · 이미지 없음"}
                      </button>
                    ))}
                  </div>
                ) : null}

                <div
                  className={`mt-3 grid gap-3 ${compare ? "sm:grid-cols-2" : ""}`}
                >
                  {shown.map((item) => (
                    <Shot
                      key={item.id}
                      concept={item}
                      camera={camera}
                      src={camera ? views[item.id]?.[camera.id] : undefined}
                      zoneName={zone.name}
                      showConcept={compare}
                    />
                  ))}
                </div>
                {camera && camera.zoneId !== zone.id ? (
                  <p className="mt-2 text-sm text-muted">
                    이 구역만 찍은 이미지는 아직 없어, 이 구역이 함께 보이는 「
                    {camera.label}」 시점을 보여 줍니다.
                  </p>
                ) : null}
              </div>
              <div className="min-w-0 lg:-mt-7">
                <Block title="왜 여기에 두었나">
                  <ul className="space-y-2">
                    {zone.why.map((line) => (
                      <li key={line} className="flex gap-2.5">
                        <span className="mt-[0.7em] h-1 w-1 shrink-0 rounded-full bg-copper" />
                        <span>{line}</span>
                      </li>
                    ))}
                  </ul>
                </Block>

                <Block title="크기를 이렇게 잡은 근거">
                  <ul className="space-y-1.5">
                    {zone.dims.map((line) => (
                      <li key={line} className="flex gap-2.5">
                        <span className="mt-[0.7em] h-1 w-1 shrink-0 rounded-full bg-muted" />
                        <span>{line}</span>
                      </li>
                    ))}
                  </ul>
                </Block>

                <Block title="여기에 들어가는 물품과 이유">
                  <dl className="divide-y divide-line border-y border-line">
                    {zone.items.map((item) => (
                      <div
                        key={item.name}
                        className="grid gap-x-4 gap-y-0.5 py-2.5 sm:grid-cols-[minmax(0,2fr)_minmax(0,3fr)]"
                      >
                        <dt className="font-medium">
                          {item.name}
                          {item.proposed ? (
                            <span className="ml-2 rounded-sm border border-line px-1.5 py-0.5 text-xs font-normal text-muted">
                              제안
                            </span>
                          ) : null}
                        </dt>
                        <dd className="text-muted">{item.why}</dd>
                      </div>
                    ))}
                  </dl>
                  {zone.items.some((item) => item.proposed) ? (
                    <p className="mt-2 text-xs text-muted">
                      「제안」은 실제 도면에는 없고 우리가 제안하는 항목입니다.
                      아직 확정하지 않았습니다.
                    </p>
                  ) : null}
                </Block>

                <Block title="동선">
                  <ul className="space-y-2">
                    {zone.flow.map((line) => (
                      <li key={line}>{line}</li>
                    ))}
                  </ul>
                </Block>

                <Block title="확인할 것">
                  <ul className="space-y-2 text-muted">
                    {zone.check.map((line) => (
                      <li key={line}>{line}</li>
                    ))}
                  </ul>
                </Block>
              </div>
            </div>
          </section>
        </div>

        <section
          className="mt-12 border-t border-line pt-8"
          aria-label="전체 배치 원칙"
        >
          <h2 className="text-xl font-medium">전체를 이렇게 배치한 이유</h2>
          <ol className="mt-4 grid gap-x-8 gap-y-5 sm:grid-cols-2 lg:grid-cols-3">
            {principles.map((item, index) => (
              <li key={item.title}>
                <p className="font-medium">
                  <span className="mr-2 text-copper">{index + 1}</span>
                  {item.title}
                </p>
                <p className="mt-1 text-sm leading-6 text-muted">{item.body}</p>
              </li>
            ))}
          </ol>
        </section>

        <section className="mt-10 grid gap-8 border-t border-line pt-8 lg:grid-cols-2">
          <div>
            <h2 className="text-xl font-medium">아직 정해지지 않은 것</h2>
            <ul className="mt-3 space-y-2 text-sm leading-6">
              {openIssues.map((line) => (
                <li key={line} className="flex gap-2.5">
                  <span className="mt-[0.7em] h-1 w-1 shrink-0 rounded-full bg-muted" />
                  <span>{line}</span>
                </li>
              ))}
            </ul>
          </div>
          <div>
            <h2 className="text-xl font-medium">컨셉</h2>
            <div className="mt-3 grid gap-5 sm:grid-cols-2">
              {concepts.map((item) => (
                <div key={item.id}>
                  <p className="font-medium">{item.label}</p>
                  <div className="mt-2 flex gap-1" aria-hidden="true">
                    {item.palette.map((color) => (
                      <span
                        key={color}
                        className="h-5 flex-1 rounded-sm border border-line"
                        style={{ background: color }}
                      />
                    ))}
                  </div>
                  <p className="mt-2 text-sm leading-6">{item.summary}</p>
                  <ul className="mt-2 space-y-1 text-sm text-muted">
                    {item.materials.map((material) => (
                      <li key={material}>{material}</li>
                    ))}
                  </ul>
                </div>
              ))}
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}

function Block({
  title,
  children,
}: {
  title: string;
  children: React.ReactNode;
}) {
  return (
    <div className="mt-7">
      <h3 className="mb-2.5 text-sm tracking-wide text-copper">{title}</h3>
      <div className="text-[15px] leading-7">{children}</div>
    </div>
  );
}

function Shot({
  concept,
  camera,
  src,
  zoneName,
  showConcept,
}: {
  concept: ShopConcept;
  camera: Camera | null;
  src: string | undefined;
  zoneName: string;
  showConcept: boolean;
}) {
  return (
    <figure className="min-w-0">
      <div className="overflow-hidden rounded-md border border-line bg-panel">
        {src && camera ? (
          <a href={src} target="_blank" rel="noopener" title="크게 보기">
            {/* 사람이 넣은 파일을 그대로 보여 준다. 폴더에 넣고 새로고침하면 바로 보여야 해서 최적화를 거치지 않는다. */}
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img
              src={src}
              alt={`${concept.label} ${camera.label} 시점`}
              className="block h-auto w-full"
            />
          </a>
        ) : (
          <div className="grid aspect-[3/2] place-items-center px-6 text-center text-sm leading-6 text-muted">
            {camera ? (
              <p>
                「{camera.label}」 시점 이미지는 실제 도면 기준으로 아직 뽑지 않았습니다.
                <br />
                <code className="text-xs">
                  public/views/{concept.id}/{camera.id}.webp
                </code>
                에 넣으면 여기에 보입니다.
              </p>
            ) : (
              <p>{zoneName}은 시점 이미지를 만들지 않는 구역입니다.</p>
            )}
          </div>
        )}
      </div>
      {camera ? (
        <figcaption className="mt-1.5 text-sm text-muted">
          {showConcept ? `${concept.label} · ` : ""}
          카메라 {camera.no} · {camera.label}
        </figcaption>
      ) : null}
    </figure>
  );
}
