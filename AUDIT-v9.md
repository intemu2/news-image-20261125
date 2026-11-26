# AUDIT v9 (ROOMIER STRIP) — news-image-20261125 (27 Nov 2026 ~04:45 WIB)

## Aturan bounty (dibaca ulang dari halaman resmi 04:10 WIB, tidak berubah)
- Hadiah $100, 50 tempat: 1 $20, 2 $12, 3 $6, 4–10 $2, 11–50 $1,20.
- Deadline Fri 27 Nov 2026 12:00 AM UTC = 07:00 WIB 27 Nov 2026.
- Gambar utuh PNG/JPEG maks 1 MiB, 1024×1024 px. Program main.py/main.ts,
  tanpa network, dua run harus hasilkan byte sama. Maks 10 submit/hari, 20 total.

## Kepatuhan file v9
- entry-v9.png: 1024×1024 PNG, 437.452 byte (< 1 MiB). Lolos.
- Deterministik: dua run build_v9.py menghasilkan SHA256 sama
  2f4e214655f3de756f9f7391e6a80e4ff4c12c91bd06ca0a3114bcf9d4a38011.
- Build lokal tanpa network: PIL + file SVG lokal + 6 file ilustrasi tetap
  (assets/hero/ 3 file, assets/strip/ 3 file). Program hanya menyalin aset
  tetap + merender teks — byte hasil identik tiap run.

## Tentang 1000029409.png — JUJUR
- File bernama 1000029409.png TIDAK ada di workspace Muse (dicari di
  ~/workspace dan /tmp — tidak ketemu). File itu adalah salinan lokal di HP
  Firt, hampir pasti unduhan v8 (entry-v8.png). Perbaikan ini dikerjakan
  terhadap v8 yang bisa saya lihat.

## Perbaikan tata letak vs v8
- 3 panel ilustrasi di bawah peta kini jauh lebih lega: seni strip 56 → 88 px
  (+57%), kartu strip 86 → 120 px, sehingga petenis, komedian, dan chip
  terbaca jelas, bukan lagi potongan kecil.
- Blok AMERICAS / EUROPE / ASIA • MIDEAST • AFRICA turun 14 px (header
  582 → 596) untuk memberi ruang itu; pitch baris briefs sedikit dirapatkan
  (51 → 48 px) agar semua tetap muat tanpa memotong teks.
- Ruang diambil dari kartu hero (seni 90 → 76 px) dan panel peta digeser naik
  10 px (340 → 330); peta sendiri sedikit lebih ramping (116 → 104 px)
  tapi pin, label, dan kompas tetap terbaca.
- Perbaikan tambahan saat cek visual: baris sumber hero ("25 NOV • ...")
  pada draf pertama v9 menyentuh garis bawah kartu — sudah diperbaiki
  (kartu hero 150–326, sumber di y 308, margin 5 px di dalam kartu).
  Pada render akhir semua teks tajam, kontras tinggi, tidak ada yang
  terpotong atau tumpang tindih (dicek visual).

## Cek duplikasi & ketajaman (AST atas build_v9.py + cek visual)
- Hero 3 + pin 5 + adegan 3 + brief 18 = 29 cerita; 42 slot judul,
  42 judul unik, NOL judul ganda; tiap kata kunci cerita muncul di tepat
  SATU blok (0 keyword salah tempat). Sub-bar "6 SCENE PANELS • 18 BRIEFS"
  dan footer "29 unique stories" konsisten dengan isi aktual.

## Daftar 29 cerita unik (tanpa pengulangan)
- Hero (3): Shenzhou-24/Tiangong; tarif AS 14 mitra; Houthi klaim Ras Tanura.
- Pin peta (5): Huawei (New York), veteran UK (London), kebakaran tanker
  Kairo, runtuhan Karachi, upah garmen Dhaka.
- Adegan strip (3): Sinner operasi lutut; komedian Taiwan; Nvidia/Huang.
- Brief (18): Ábrego García; DOJ anti-scam; CIA & ODNI diretas; dana perang
  Iran; futures AS; Coast Guard Cessna; pemilu dini Spanyol; 30+ negara desak
  Rusia; Hongaria-Ukraina; inquiry 7 Okt Israel; watchdog AI UK; London
  Museum; serangan Gaza; Iran klaim 2 drone AS; India kutuk serangan Riyadh;
  koalisi Saudi serang Hodeidah; nuklir Korut; banjir tambang Indonesia.

## Audit fakta — standar: "terverifikasi" = dateline 25 Nov 2026 di sumber yang dibaca
### Tingkat KUAT (Reuters / Xinhua-SCIO / WSJ / AP, dateline 25 Nov)
- Shenzhou-24 (meluncur 08:18, dock 11:56 Beijing; Ali orang Pakistan pertama
  di orbit, tamu asing pertama di Tiangong).
- Tarif AS (Section 301 8 bulan; China 20% s.d. 40%, EU 15%; 14 mitra).
- Ras Tanura (klaim Houthi Rabu 25 Nov; koalisi jatuhkan 4 drone).
- CIA & ODNI diretas; Sinner operasi lutut; Hongaria-Ukraina; watchdog AI UK;
  London Museum reopen; komedian Taiwan; futures AS (Off the Wire, 25 Nov).

### Tingkat TUNGGAL (sumber agregator/digest, dateline 25 Nov seperti dibaca —
### tidak sempat dicek silang independen di sesi ini)
- webindia123: DOJ 800+/400 kasus; Trump dana Iran s/d Jan; Coast Guard
  Cessna 6; Iran klaim 2 drone; India kutuk Riyadh; koalisi Saudi Hodeidah.
- DailyDigest: veteran UK 100.000; Gaza 9 tewas; Korut nuklir.
- StandardTopic: pemilu Spanyol; 30+ negara desak Rusia; Nvidia/Huang.
- otrecord.news: inquiry 7 Okt Israel; banjir tambang Indonesia.
- Russell Record / Democracy Now: Ábrego García tiba di Spanyol.

## CATATAN JUJUR — belum / tidak bisa diklaim penuh
1. Huawei (TERBATAS — zona waktu): vonis DILAPORKAN 25 Nov (dateline Reuters/
   BusinessWorld 25 Nov); laporan AS menyebut juri memutuskan "Selasa"
   = 24 Nov waktu AS. Gambar tidak mengklaim jam putusan.
2. Riyadh (India condemns): yang bertanggal 25 Nov adalah KECAMAN India
   (MEA). Serangan menaranya sendiri terjadi Selasa 24 Nov (11 luka,
   termasuk 2 orang India) — fakta luka itu dilaporkan 25 Nov.
3. Peta skematik: garis pantai disederhanakan, Antartika dipotong, pulau kecil
   tidak digambar, posisi pin perkiraan kota, label kontinen di posisi
   perkiraan. Bukan peta presisi; dinyatakan di kaki gambar.
4. Semua 6 panel adegan adalah ilustrasi orisinal (bukan foto kejadian);
   petenis/komedian digambarkan sebagai figur generik, bukan potret orang
   yang sebenarnya.
5. BELUM TERVERIFIKASI: jumlah submit terpakai akun intemu2, jumlah entri/
   field live dan rank — tidak ada di halaman bounty yang dibaca.
6. File v2 lama (33 cerita) tetap tidak ditemukan di workspace; tidak dipakai.
