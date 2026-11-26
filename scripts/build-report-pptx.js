const pptxgen = require("pptxgenjs");
const { applyTheme } = require("/Users/ymy/.claude/skills/synced/6b601eff-70e4-4ae2-9559-72d2311464d4_8c4a8f4c-2781-45a5-a06b-64e72561f4c5/pptx/scripts/apply_theme.js");

const THEME = {
  name: "TOMATOK Lounge",
  headFontFace: "Cambria",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "1C1915",
    lt1: "FFFFFF",
    dk2: "5C564E",
    lt2: "F3EEE6",
    accent1: "8D4B32",
    accent2: "6E8B8B",
    accent3: "3E4A44",
    accent4: "C4A484",
    accent5: "2A2622",
    accent6: "E4DDD2",
    hlink: "8D4B32",
    folHlink: "5C564E",
  },
};

const plan = "/tmp/floor-plan-cafe.svg.png";
const views = "/Users/ymy/project/vip_interrier/public/views/cafe";

const slides = [
  {
    file: "aerial.jpg",
    place: "전체",
    line: "오른쪽에서 접수하고 사고, 왼쪽에서 쉰다.",
  },
  {
    file: "entry.jpg",
    place: "입구",
    line: "들어오면 정면에 브랜드가 보이고, 바로 오른쪽이 안내다.",
  },
  {
    file: "desk.jpg",
    place: "안내데스크",
    line: "문 옆이라 들어와서 바로 접수하고, 나갈 때 같은 자리에서 결제한다.",
  },
  {
    file: "wait.jpg",
    place: "체험 대기",
    line: "데스크 앞에 앉으면 진열과 로고가 정면이다.",
  },
  {
    file: "sales.jpg",
    place: "쉼 라운지",
    line: "왼쪽은 누구나 쉬다 가는 자리. 앉으면 진열장이 정면이다.",
  },
  {
    file: "foot.jpg",
    place: "발마사지",
    line: "안쪽 벽을 등져 통로 시선에서 벗어나고, 쉬는 자리와 이어진다.",
  },
  {
    file: "powder.jpg",
    place: "파우더룸",
    line: "나가는 문 바로 왼쪽이라 나가기 직전에 들른다.",
  },
  {
    file: "room.jpg",
    place: "관리실",
    line: "위쪽에 두어 라운지와 떨어져 있다.",
  },
];

const pres = new pptxgen();
pres.defineLayout({ name: "WIDE", width: 13.333, height: 7.5 });
pres.layout = "WIDE";
pres.theme = { headFontFace: "Cambria", bodyFontFace: "Calibri" };
pres.title = "TOMATOK VIP LOUNGE 컨셉";
pres.author = "VIP Interior";
pres.subject = "도면과 시점";

const C = pres.SchemeColor;

pres.defineSlideMaster({
  title: "Pair",
  background: { color: C.background1 },
  objects: [
    {
      placeholder: {
        options: {
          name: "body",
          type: "body",
          x: 0.45,
          y: 6.15,
          w: 11.6,
          h: 0.95,
          fontFace: "Calibri",
          fontSize: 18,
          color: C.text1,
          margin: 0,
        },
        text: "",
      },
    },
  ],
  slideNumber: {
    x: 12.2,
    y: 7.05,
    w: 0.6,
    h: 0.28,
    fontFace: "Calibri",
    fontSize: 12,
    color: "5C564E",
  },
});

pres.addSection({ title: "컨셉" });

for (const item of slides) {
  const slide = pres.addSlide({ masterName: "Pair", sectionTitle: "컨셉" });
  slide.transition = { type: "fade", speed: "fast" };
  slide.addImage({
    path: plan,
    x: 0.4,
    y: 0.28,
    w: 6.15,
    h: 5.65,
    sizing: { type: "contain", x: 0.4, y: 0.28, w: 6.15, h: 5.65 },
    objectName: "도면",
  });
  slide.addImage({
    path: `${views}/${item.file}`,
    x: 6.75,
    y: 0.28,
    w: 6.15,
    h: 5.65,
    sizing: { type: "contain", x: 6.75, y: 0.28, w: 6.15, h: 5.65 },
    objectName: item.place,
  });
  slide.addText(
    [
      {
        text: item.place,
        options: { fontFace: "Cambria", fontSize: 22, color: C.accent1, breakLine: true },
      },
      {
        text: item.line,
        options: { fontFace: "Calibri", fontSize: 18, color: C.text1 },
      },
    ],
    { placeholder: "body" },
  );
  slide.addNotes(`${item.place}. ${item.line}`);
}

const out = "/Users/ymy/project/vip_interrier/TOMATOK_VIP_LOUNGE_진행보고.pptx";
pres
  .writeFile({ fileName: out })
  .then(() => applyTheme(out, THEME))
  .then(() => console.log(out))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
