import { Suspense } from "react";
import { connection } from "next/server";
import { Viewer } from "@/components/viewer";
import { listViews, loadPlanMarkups } from "@/lib/views";

export default function Home() {
  return (
    <Suspense fallback={<p className="p-8 text-sm text-muted">도면을 불러오는 중입니다.</p>}>
      <ViewerLoader />
    </Suspense>
  );
}

// 이미지 파일을 폴더에 넣고 새로고침하면 바로 보여야 하므로, 요청마다 폴더를 다시 읽는다.
async function ViewerLoader() {
  await connection();
  return <Viewer planMarkup={loadPlanMarkups()} views={listViews()} />;
}
