import type { Metadata } from "next";
import { Instrument_Serif, Noto_Sans_KR } from "next/font/google";
import "./globals.css";

const display = Instrument_Serif({
  variable: "--font-display-family",
  subsets: ["latin"],
  weight: "400",
});

const body = Noto_Sans_KR({
  variable: "--font-body",
  subsets: ["latin"],
  weight: ["400", "500"],
});

export const metadata: Metadata = {
  title: "VIP Interior",
  description: "인테리어 컨셉을 도면과 여러 시점으로 보는 스튜디오",
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html lang="ko" className={`${display.variable} ${body.variable} h-full antialiased`}>
      <body className="min-h-full">{children}</body>
    </html>
  );
}
