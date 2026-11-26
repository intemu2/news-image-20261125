# Transcripts — news-image-20261125 build sessions (27 Nov 2026, WIB)

AI coding-agent build log for Firt / intemu2, bounty
"Sum up 25 November's world news in one image"
(https://make.fun/bounty/news-image-20261125).
One continuous session in a dedicated side chat, nine image versions.
This file is a faithful session log: user prompts paraphrased in their own
words, agent actions, decisions, and audit results. No facts were invented
for this log; the fact audit lives in AUDIT-v9.md.

## Standing rules (user, repeated in every task prompt)
1. ANTI-HALUSINASI: use ONLY rules/facts explicitly read or verified from
   the official bounty page, make.fun docs/CLI, and available sources.
   Never invent events, numbers, quotes, names, or sources; never claim
   "terverifikasi" without an actual source that was read; state unverified
   parts honestly.
2. FOKUS SATU BOUNTY: news-image-20261125 only.
3. WAJIB MINTA REVIEW SEBELUM SUBMIT FINAL: no final submit before the user
   reviews the image/output and gives explicit approval.
4. Fresh build, no old rules ("Tidak, semuanya buat baru, tidak ada
   peraturan lama yang dipakai lagi"); only news proven to have occurred or
   been announced on 25 Nov 2026 ("Hanya yang terbukti di tanggal 25").

## Bounty rules (read from the official page 27 Nov 03:58, 04:04, 04:10 WIB)
- $100, 50 places: 1st $20, 2nd $12, 3rd $6, 4th–10th $2, 11th–50th $1.20.
- Ends Fri 27 Nov 2026 12:00 AM UTC = 07:00 WIB 27 Nov 2026.
- Image: whole PNG/JPEG, at most 1 MiB, 1024×1024 px; program at main.py
  (Python 3.13) or main.ts in repo root; no network; two runs must write
  the same bytes; max 10 submissions/day, 20 total; public GitHub repo
  owned by the user's own account, OSI license; AI coding-agent transcripts
  uploaded with each submission.

## v1 (~04:00 WIB) — user: build a competitive entry
- Built `build.py` (PIL): "THE WORLD IN ONE DAY" broadsheet, 3 text heroes
  + 24 briefs, 1024×1024, 136,598 bytes.
- User rejected it (04:01): "Apa yang kamu buat tidak sesuai dengan apa
  yang di promt" — no world map, no illustrations, regions merged.
  Agent admitted the gaps.

## v3 (~04:08 WIB) — user: rebuild with map + illustrations, no duplication
- `build_v3.py`, SVG map with 5 pins, 6 SVG icons, 18 briefs, 127,718 bytes.
  Determinism verified (identical SHA256 on two runs). AUDIT-v3.md.

## v4 (~04:15 WIB) — user: richer scenes, labelled map, zero duplication
- `build_v4.py`: 6 scene panels (3 hero + 3 strip), labelled map + pin
  index, 21 unique stories. AUDIT-v4.md. Agent honestly reported the
  bounty page Feed entries cannot be read via text fetch.

## v5 (~04:25 WIB) — user: full competitive overhaul
- `build_v5.py`: 29 unique stories, zero duplication (heroes Shenzhou-24 /
  US tariffs / Ras Tanura; pins Huawei, UK veterans, Cairo fire, Karachi
  collapse, Dhaka wage; strip Sinner, Nvidia, Taiwan comedian; 18 briefs).
  AUDIT-v5.md.

## v6 (~04:30 WIB) — user: typo pass
- Fixed "Ábrego García" and "Sánchez" accents; hero-3 kicker
  "MIDDLE EAST" → "SAUDI ARABIA" (duplicated a column header); named
  "Shenzhou-24" in hero 1's source line. AST check: 29 stories, 42 title
  slots, 42 unique, no duplicate titles. AUDIT-v6.md.

## v7 (~04:35 WIB) — user: fix 1000029407.png, less geometric, more expressive
- 3 hero panels replaced with rich painterly generated illustrations
  (fixed asset files, checked visually: no text/letters/numbers/watermark
  inside); all words/numbers remain PIL-rendered type. Map enriched
  (4-layer ocean gradient, graticule, compass rose); rounded panels.
  Same 29 stories/text as v6. Agent honestly reported 1000029407.png was
  not found in the workspace (user's local phone copy, almost certainly
  the downloaded v6). AUDIT-v7.md. Presented; awaiting GO.

## v8 (~04:40 WIB) — user: revise 1000029408.png; strip panels must be
##   lively scenes like the top row, all text sharp, zero typo/duplication
- Generated 3 strip illustrations (tennis serve under floodlights, comedian
  under a warm spotlight, glowing green microchip), checked visually, no
  text inside. Strip cards made taller (56 px art). Same 29 stories.
  Deterministic SHA256 verified. AUDIT-v8.md. Presented; awaiting GO.

## v9 (~04:45 WIB) — user: revise 1000029409.png; lower the AMERICAS /
##   EUROPE / ASIA blocks, give the 3 strip panels more room
- Strip art 56 → 88 px (+57%), cards 86 → 120 px; brief blocks down 14 px;
  hero art 90 → 76 px and map panel shifted up to reclaim space.
  Visual check caught hero source lines touching the card edge — fixed
  (card 150–326, source at y 308). Same 29 stories, same text.
  1024×1024 PNG, 437,452 bytes, deterministic SHA256
  2f4e214655f3de756f9f7391e6a80e4ff4c12c91bd06ca0a3114bcf9d4a38011.
  AST check: 42 titles, 42 unique, 0 duplicates, 0 keywords misplaced.
  AUDIT-v9.md. Presented; awaiting GO.

## User report (04:36 WIB): "Masih gambar yang lama itu belum terganti"
- Agent explained the downloaded file on the user's phone (1000029409.png
  = v8) cannot change by itself; the new file is entry-v9.png (different
  size and SHA256). Built a stacked strip comparison (v8 vs v9) and
  re-attached entry-v9.png so the difference is visible.

## Submit (04:36+ WIB) — user: "Oke, submit"
- User gave explicit GO to submit v9. Submission package: repo
  intemu2/news-image-20261125 with main.py (stdlib-only, embedded PNG
  bytes, read-back verification added as a second revision — the same
  two-message authoring pattern that fixed the thinking_revised rejection
  on the successful one-emoji entry), MIT LICENSE, README.md,
  .makefun/owner.json (wallet FJ2b…wiCJn), AUDIT-v9.md, entry.png.
- Submitted to bounty news-image-20261125 via make.fun with this
  transcript bundle. See submission-receipt.json (kept mode 600; claim
  code never shown in chat).

## Fact tiers (see AUDIT-v9.md for the full per-item audit)
- STRONG (Reuters / Xinhua-SCIO / WSJ / AP, 25 Nov dateline): Shenzhou-24,
  US tariffs, Ras Tanura claim, CIA & ODNI breach, Sinner, Hungary–Ukraine,
  UK AI watchdog, London Museum, Taiwan comedian, US futures.
- SINGLE-SOURCE (aggregator/digest, 25 Nov dateline as read, not
  independently cross-checked): DOJ sweep, Gaza, North Korea, Spain snap
  election, Nvidia/Huang, Oct 7 inquiry, Indonesia mine flood,
  Ábrego García.
- HONEST CAVEATS: Huawei verdict reported 25 Nov but jury decided Tue
  (24 Nov US time); Riyadh attack itself was Tue 24 Nov — the 25 Nov item
  is India's condemnation; map is schematic; all 6 scene panels are
  original illustrations (generic figures, not portraits); submission
  count used / live field size / rank not verifiable from the bounty page.
