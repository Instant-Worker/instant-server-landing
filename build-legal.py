#!/usr/bin/env python3
"""Generate legal pages (Terms / Privacy / Refund) for instantserver.dev, ID + EN.

Run: python3 build-legal.py   (writes *.html next to this script)
Shared layout keeps all six pages visually identical to the landing page.
"""
import html
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://instantserver.dev"
PANEL = "https://panel.instantserver.dev"
STATUS = "https://status.instantserver.dev"
SUPPORT = "support@instantserver.dev"
UPDATED = "2 Oktober 2026"
UPDATED_EN = "2 October 2026"
OPERATOR = "PT Inovasi Pemuda Bangsa"
OPERATOR_ADDRESS = ("Gd. Rabithah Alawiyah, Jl. TB Simatupang No. 7A, Tanjung Barat, Jagakarsa, "
                    "Jakarta Selatan, DKI Jakarta, Indonesia")
OPERATOR_ADDRESS_EN = ("Gd. Rabithah Alawiyah, Jl. TB Simatupang No. 7A, Tanjung Barat, Jagakarsa, "
                       "South Jakarta, DKI Jakarta, Indonesia")

LAYOUT = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Instant Server</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/legal.css">
</head>
<body>
<header class="top">
  <div class="wrap">
    <a class="brand" href="{site}/"><span class="mark">IS</span> Instant Server</a>
    <nav>{nav}</nav>
  </div>
</header>
<main>
  <div class="wrap">
{body}
  </div>
</main>
<footer class="site">
  <div class="wrap">
    <span>© 2026 Instant Server. {rights}</span>
    <span><a href="{support_href}">{support}</a> · <a href="{status}">{status_label}</a> · <a href="{panel}">{panel_label}</a></span>
  </div>
</footer>
</body>
</html>
"""

NAV_ID = ('<a href="/">Beranda</a><a href="/terms">Syarat Layanan</a>'
          '<a href="/privacy">Kebijakan Privasi</a><a href="/refund">Refund</a>')
NAV_EN = ('<a href="/">Home</a><a href="/en/terms">Terms of Service</a>'
          '<a href="/en/privacy">Privacy Policy</a><a href="/en/refund">Refunds</a>')


def page(path, lang, title, desc, body, nav):
    out = LAYOUT.format(
        lang=lang, title=title, desc=desc, body=body, nav=nav,
        site=SITE, support=SUPPORT, support_href="mailto:" + SUPPORT, status=STATUS,
        panel=PANEL,
        rights="Seluruh hak dilindungi." if lang == "id" else "All rights reserved.",
        status_label="Status Layanan" if lang == "id" else "Service Status",
        panel_label="Portal Klien" if lang == "id" else "Client Portal",
    )
    (ROOT / path).write_text(out, encoding="utf-8")
    print("wrote", path, len(out), "bytes")


# ---------------------------------------------------------------- ID: Terms
TERMS_ID = """
<h1>Syarat Layanan</h1>
<p class="sub">Terakhir diperbarui: {updated} · Berlaku untuk <strong>instantserver.dev</strong> dan
<strong>panel.instantserver.dev</strong> · Versi Bahasa Indonesia mengikat.</p>

<div class="callout"><p><strong>Penyelenggara:</strong> {operator}, berkedudukan di {address}
(&ldquo;kami&rdquo;). Dengan membuat akun atau memesan layanan, Anda menyetujui Syarat Layanan ini
beserta <a href="/privacy">Kebijakan Privasi</a> dan <a href="/refund">Kebijakan Refund</a> kami.</p></div>

<h2>1. Layanan yang Kami Sediakan</h2>
<p>Instant Server menyediakan layanan infrastruktur digital berlangganan yang diprovisikan secara
otomatis melalui panel kami:</p>
<ul>
  <li><strong>Cloud Server</strong> — mesin virtual (VPS) dengan alamat IPv4 publik, akses root penuh
  melalui SSH, penyimpanan NVMe, dan HTTPS otomatis.</li>
  <li><strong>Object Storage</strong> — penyimpanan objek yang kompatibel dengan S3.</li>
  <li><strong>Backup Otomatis</strong> — add-on opsional untuk pencadangan berkala (lihat bagian 10).</li>
</ul>
<p>Layanan berjalan di pusat data di Indonesia. Spesifikasi tiap paket (vCPU, memori, penyimpanan,
transfer) tercantum pada halaman harga dan menjadi bagian dari perjanjian ini.</p>

<h2>2. Akun</h2>
<ul>
  <li>Anda wajib memberikan data yang benar, akurat, dan terkini saat mendaftar.</li>
  <li>Anda bertanggung jawab menjaga kerahasiaan kredensial akun dan seluruh aktivitas yang terjadi
  melalui akun Anda.</li>
  <li>Satu akun digunakan untuk satu pelanggan atau satu badan usaha. Akun tidak boleh diperjualbelikan
  atau dialihkan tanpa persetujuan tertulis kami.</li>
  <li>Kami dapat meminta verifikasi identitas atau data usaha sebelum mengaktifkan layanan, sebagai
  bagian dari kewajiban kepatuhan.</li>
</ul>

<h2>3. Pesanan dan Aktivasi</h2>
<ul>
  <li>Pesanan diproses otomatis. Layanan umumnya aktif dalam beberapa menit setelah pembayaran
  terkonfirmasi; target kami di bawah 5 menit.</li>
  <li>Bila provisi gagal karena sebab di luar kendali kami, kami akan mengaktifkan layanan secara
  manual atau mengembalikan dana penuh untuk pesanan tersebut.</li>
  <li>Penyediaan sumber daya dapat bergantung pada ketersediaan kapasitas pada lokasi yang dipilih.</li>
</ul>

<h2>4. Harga dan Pembayaran</h2>
<ul>
  <li>Semua harga ditampilkan dalam Dolar AS (USD) dan <strong>belum termasuk pajak</strong> yang berlaku.
  Pajak ditambahkan pada faktur bila diwajibkan oleh hukum.</li>
  <li>Langganan bersifat <strong>prabayar bulanan</strong>. Layanan berjalan selama periode yang telah
  dibayar.</li>
  <li>Pembayaran dengan kartu diproses oleh <strong>Creem</strong>, yang bertindak sebagai
  <em>Merchant of Record</em>. Untuk transaksi tersebut, Creem adalah pihak yang menjual kepada
  pelanggan akhir dan menangani kepatuhan pajak terkait; ketentuan Creem juga berlaku.</li>
  <li>Kami tidak menyimpan nomor kartu penuh. Data pembayaran diproses langsung oleh penyedia
  pembayaran.</li>
  <li>Faktur yang belum dibayar melewati jatuh tempo dapat menyebabkan penangguhan sesuai bagian 5.</li>
  <li>Harga dapat berubah dengan pemberitahuan minimal 30 hari sebelum periode penagihan berikutnya.
  Perubahan tidak berlaku surut untuk periode yang sudah dibayar.</li>
</ul>

<h2>5. Penangguhan dan Penghentian Layanan</h2>
<ul>
  <li><strong>Faktur terlambat:</strong> layanan ditangguhkan 2 hari setelah jatuh tempo dan
  dihentikan (terminated) 14 hari setelah jatuh tempo.</li>
  <li><strong>Terminasi karena kelalaian pembayaran:</strong> seluruh data pada layanan tersebut
  dihapus dan tidak dapat dipulihkan. Backup kami bukan pengganti kewajiban Anda menyimpan data
  sendiri.</li>
  <li><strong>Pelanggaran kebijakan:</strong> kami dapat menangguhkan atau menghentikan layanan
  segera, tanpa refund, bila terdapat pelanggaran bagian 7, permintaan aparat penegak hukum yang
  sah, atau risiko keamanan bagi infrastruktur dan pelanggan lain.</li>
  <li>Anda dapat berhenti kapan saja dari panel. Penghentian berlaku pada akhir periode berjalan
  yang telah dibayar.</li>
</ul>

<h2>6. Kebijakan Penggunaan yang Dapat Diterima (AUP)</h2>
<p>Anda dilarang menggunakan layanan kami untuk:</p>
<ul>
  <li>spam, phishing, penipuan, atau rekayasa sosial dalam bentuk apa pun;</li>
  <li>menyebarkan malware, ransomware, botnet, atau perangkat lunak berbahaya lainnya;</li>
  <li>serangan terhadap sistem pihak lain, termasuk pemindaian port massal, brute force, DDoS, dan
  upaya akses tidak sah;</li>
  <li>penambangan mata uang kripto tanpa izin tertulis dari kami;</li>
  <li>materi yang melanggar hukum, termasuk konten seksual yang menampilkan anak, konten kekerasan,
  dan materi yang melanggar hak kekayaan intelektual pihak lain;</li>
  <li>perjudian tanpa lisensi, layanan keuangan ilegal, atau aktivitas lain yang melanggar hukum
  Republik Indonesia;</li>
  <li>layanan proxy/VPN publik untuk penyalahgunaan anonim, termasuk penggunaan sebagai jalur keluar
  untuk aktivitas yang dilarang di atas;</li>
  <li>mengirim email massal (bulk email) tanpa mekanisme opt-in dan tanpa penanganan keluhan;</li>
  <li>menyimpan atau memproses data yang menurut hukum Indonesia wajib disimpan pada infrastruktur
  tertentu, bila layanan ini tidak memenuhi syarat tersebut;</li>
  <li>menyalahgunakan sumber daya bersama secara berlebihan sehingga mengganggu pelanggan lain.</li>
</ul>
<p>Kami dapat meminta penjelasan atas penggunaan yang mencurigakan. Bila pelanggaran terkonfirmasi,
kami dapat menangguhkan layanan tanpa refund dan melaporkannya kepada pihak berwenang bila
diwajibkan.</p>

<h2>7. Refund dan Pembatalan</h2>
<p>Ketentuan lengkap ada pada <a href="/refund">Kebijakan Refund</a>. Ringkasnya: garansi uang kembali
7 hari untuk pembelian pertama layanan Cloud Server atau Object Storage; biaya pihak ketiga dan
periode setelah bulan pertama tidak dapat dikembalikan; pembatalan dapat dilakukan kapan saja dari
panel dan berlaku pada akhir periode berjalan.</p>

<h2>8. Tingkat Layanan (SLA) dan Dukungan</h2>
<ul>
  <li><strong>Target ketersediaan:</strong> 99,9% per bulan untuk konektivitas jaringan dan daya
  host. Pemeliharaan terjadwal yang diumumkan sebelumnya, gangguan pada layanan pelanggan itu sendiri,
  dan kegagalan yang disebabkan konfigurasi pelanggan tidak dihitung sebagai downtime.</li>
  <li><strong>Dukungan:</strong> {support}, Senin&ndash;Jumat 09.00&ndash;18.00 WIB (hari libur nasional
  dikecualikan). Target respons pertama maksimal 1 hari kerja dan penyelesaian maksimal 3 hari kerja.</li>
  <li><strong>Pemantauan:</strong> status layanan dipublikasikan di <a href="{status}">{status}</a>.</li>
</ul>

<h2>9. Data Pelanggan dan Privasi</h2>
<p>Anda memiliki seluruh data yang Anda unggah atau proses pada layanan. Kami memproses data akun dan
data teknis sesuai <a href="/privacy">Kebijakan Privasi</a>. Kami tidak mengakses isi layanan Anda
kecuali Anda meminta bantuan, atau bila diwajibkan oleh hukum. Anda bertanggung jawab atas kepatuhan
pemrosesan data pribadi pihak ketiga yang Anda simpan pada layanan kami.</p>

<h2>10. Backup</h2>
<p>Add-on <strong>Backup Otomatis</strong> bersifat opsional dan berbayar 20% dari harga paket
(frekuensi 24 jam; 12 jam dan 6 jam tersedia dengan biaya tambahan). Add-on ini mencadangkan data
layanan Anda secara berkala ke penyimpanan objek kami.</p>
<p><strong>Tanpa add-on tersebut, tidak ada pencadangan otomatis</strong> dan Anda bertanggung jawab
penuh membuat backup sendiri. Backup adalah pelengkap, bukan pengganti praktik terbaik Anda. Membeli
add-on tidak memberi kami izin menjalankan perintah di dalam server Anda, dan tidak mengubah
kebijakan privasi.</p>

<h2>11. Kekayaan Intelektual</h2>
<p>Seluruh perangkat lunak, merek, dan materi platform Instant Server tetap milik kami atau pemberi
lisensinya. Kami memberi Anda lisensi terbatas, tidak eksklusif, dan tidak dapat dialihkan untuk
menggunakan layanan selama perjanjian ini berlaku. Anda memberi kami lisensi terbatas hanya untuk
menjalankan layanan atas nama Anda.</p>

<h2>12. Batasan Tanggung Jawab</h2>
<p>Sejauh diizinkan hukum, tanggung jawab kami atas klaim apa pun yang timbul dari perjanjian ini
dibatasi pada jumlah biaya layanan yang Anda bayarkan untuk bulan terjadinya klaim. Kami tidak
bertanggung jawab atas kehilangan keuntungan, kehilangan data, atau kerugian tidak langsung lainnya.
Kami tidak memberikan jaminan atas kesesuaian layanan untuk tujuan tertentu di luar yang tertulis
pada halaman produk.</p>

<h2>13. Keadaan Memaksa</h2>
<p>Kami tidak bertanggung jawab atas kegagalan atau keterlambatan yang disebabkan oleh keadaan di
luar kendali wajar kami, termasuk bencana alam, pemadaman listrik, gangguan jaringan telekomunikasi,
serangan siber berskala besar, kebijakan pemerintah, atau kegagalan pihak ketiga.</p>

<h2>14. Perubahan Syarat</h2>
<p>Kami dapat memperbarui Syarat Layanan ini. Perubahan material akan diberitahukan melalui email
terdaftar atau pengumuman di panel minimal 14 hari sebelum berlaku. Tanggal &ldquo;terakhir
diperbarui&rdquo; di atas selalu menunjukkan versi yang berlaku.</p>

<h2>15. Hukum yang Berlaku dan Sengketa</h2>
<p>Perjanjian ini diatur oleh hukum Republik Indonesia. Para pihak sepakat menyelesaikan sengketa
melalui musyawarah terlebih dahulu; bila tidak tercapai, sengketa diselesaikan pada pengadilan yang
berwenang di Indonesia.</p>

<h2>16. Kontak</h2>
<p>Pertanyaan mengenai Syarat Layanan ini, tagihan, atau permintaan dukungan:
<a href="mailto:{support}">{support}</a>. Sertakan ID layanan atau nomor faktur agar kami dapat
membantu lebih cepat.</p>
"""

# -------------------------------------------------------------- ID: Privacy
PRIVACY_ID = """
<h1>Kebijakan Privasi</h1>
<p class="sub">Terakhir diperbarui: {updated} · Berlaku untuk <strong>instantserver.dev</strong> dan
<strong>panel.instantserver.dev</strong> · Versi Bahasa Indonesia mengikat.</p>

<div class="callout"><p><strong>Pengendali data:</strong> {operator}, {address}. Pertanyaan atau
permintaan terkait data pribadi: <a href="mailto:{support}">{support}</a>. Kami menanggapi dalam
maksimal 3 hari kerja.</p></div>

<h2>1. Ringkasan</h2>
<p>Kami mengumpulkan data yang diperlukan untuk membuat akun, menyediakan layanan, menagih
pembayaran, dan memenuhi kewajiban hukum. Kami tidak menjual data pribadi Anda, dan kami tidak
mengakses isi layanan Anda kecuali Anda meminta bantuan atau bila diwajibkan hukum.</p>

<h2>2. Data yang Kami Kumpulkan</h2>
<h3>a. Data akun dan identitas</h3>
<ul>
  <li>Nama lengkap atau nama badan usaha, alamat email, nomor telepon/WhatsApp;</li>
  <li>Alamat penagihan dan, bila diwajibkan, nomor identitas usaha untuk keperluan verifikasi
  (<em>know your customer</em>);</li>
  <li>Kredensial akun (kata sandi disimpan dalam bentuk hash, tidak pernah dalam bentuk teks biasa).</li>
</ul>
<h3>b. Data transaksi</h3>
<ul>
  <li>Riwayat pesanan, faktur, langganan, dan status pembayaran.</li>
  <li>Kami <strong>tidak menyimpan nomor kartu penuh atau CVC</strong>. Data kartu diproses langsung
  oleh penyedia pembayaran atau <em>Merchant of Record</em>.</li>
</ul>
<h3>c. Data teknis dan operasional</h3>
<ul>
  <li>Alamat IP, waktu akses, jenis peramban, dan catatan aktivitas pada panel;</li>
  <li>Metrik penggunaan sumber daya (CPU, memori, penyimpanan, transfer data) untuk penagihan dan
  pengelolaan kapasitas;</li>
  <li>Catatan komunikasi dengan tim dukungan.</li>
</ul>
<h3>d. Data yang Anda simpan pada layanan</h3>
<p>Isi server virtual dan objek yang Anda simpan di object storage tetap milik Anda. Kami hanya
mengaksesnya bila Anda meminta dukungan teknis, untuk pemeliharaan yang Anda setujui, atau bila
diwajibkan oleh hukum.</p>

<h2>3. Dasar dan Tujuan Pemrosesan</h2>
<table>
  <tr><th>Tujuan</th><th>Dasar</th></tr>
  <tr><td>Membuat akun dan menyediakan layanan</td><td>Pelaksanaan perjanjian</td></tr>
  <tr><td>Penagihan, faktur, dan penagihan tunggakan</td><td>Pelaksanaan perjanjian</td></tr>
  <tr><td>Pencegahan penipuan, keamanan, penyalahgunaan layanan</td><td>Kepentingan sah</td></tr>
  <tr><td>Dukungan teknis dan pemberitahuan layanan</td><td>Pelaksanaan perjanjian / kepentingan sah</td></tr>
  <tr><td>Pemenuhan kewajiban pajak dan hukum</td><td>Kewajiban hukum</td></tr>
</table>

<h2>4. Pembayaran dan Merchant of Record</h2>
<p>Pembayaran dengan kartu diproses oleh <strong>Creem</strong> sebagai
<em>Merchant of Record</em>. Dalam peran tersebut, Creem menjadi pihak penjual kepada pelanggan akhir
dan memproses data pembayaran serta kepatuhan pajak terkait menurut kebijakan privasinya sendiri.
Untuk pembayaran lokal, kami menggunakan penyedia pembayaran yang berizin di Indonesia. Kami hanya
menerima status transaksi (berhasil, gagal, refund), bukan data kartu.</p>

<h2>5. Pembagian Data dengan Pihak Ketiga</h2>
<p>Kami membagikan data hanya sebatas yang diperlukan kepada:</p>
<ul>
  <li><strong>Penyedia infrastruktur dan pusat data</strong> — menjalankan server dan penyimpanan;</li>
  <li><strong>Penyedia pembayaran dan Merchant of Record</strong> — memproses transaksi dan pajak;</li>
  <li><strong>Penyedia email transaksional</strong> — mengirim faktur dan pemberitahuan layanan;</li>
  <li><strong>Aparat penegak hukum atau otoritas</strong> — bila ada permintaan yang sah dan mengikat.</li>
</ul>
<p>Kami tidak menjual, menyewakan, atau memperdagangkan data pribadi Anda. Daftar penyedia dapat
berubah; versi terbaru selalu ada di halaman ini.</p>

<h2>6. Transfer Data Internasional</h2>
<p>Sebagian penyedia layanan kami dapat beroperasi di luar Indonesia. Bila terjadi transfer data
keluar wilayah Indonesia, kami memastikan adanya dasar transfer yang sah dan perlindungan yang
memadai sesuai peraturan yang berlaku.</p>

<h2>7. Retensi</h2>
<ul>
  <li>Data akun dan layanan: selama akun aktif;</li>
  <li>Setelah akun ditutup atau layanan dihentikan: dihapus dalam 90 hari, kecuali data yang wajib
  disimpan untuk keperluan pajak dan akuntansi (umumnya 10 tahun sesuai ketentuan perpajakan);</li>
  <li>Log teknis: maksimal 30 hari;</li>
  <li>Data pada layanan yang dihentikan karena kelalaian pembayaran dihapus pada saat terminasi.</li>
</ul>

<h2>8. Keamanan</h2>
<p>Kami menerapkan langkah teknis dan organisasi yang wajar: enkripsi TLS pada seluruh koneksi panel,
isolasi container antar pelanggan, pembatasan akses staf berdasarkan kebutuhan, pencadangan berkala,
dan pemantauan keamanan. Tidak ada sistem yang sepenuhnya bebas risiko; kami akan memberitahukan
insiden yang berdampak pada data pribadi Anda sesuai kewajiban hukum.</p>

<h2>9. Hak Anda</h2>
<p>Sesuai Undang-Undang Perlindungan Data Pribadi Indonesia (UU No. 27 Tahun 2022), Anda berhak:</p>
<ul>
  <li>memperoleh informasi tentang data pribadi yang kami proses dan tujuannya;</li>
  <li>meminta akses dan salinan data pribadi Anda;</li>
  <li>meminta koreksi data yang tidak akurat;</li>
  <li>meminta penghapusan data, sepanjang tidak bertentangan dengan kewajiban hukum kami;</li>
  <li>menarik persetujuan dan mengajukan keberatan atas pemrosesan tertentu;</li>
  <li>mengajukan keluhan kepada kami dan, bila perlu, kepada otoritas pengawas.</li>
</ul>
<p>Ajukan permintaan ke <a href="mailto:{support}">{support}</a>. Kami dapat meminta verifikasi
identitas sebelum memproses permintaan.</p>

<h2>10. Cookie dan Teknologi Serupa</h2>
<p>Kami hanya menggunakan cookie yang diperlukan untuk menjalankan layanan: cookie sesi login dan
cookie keamanan (misalnya perlindungan CSRF). Kami tidak memasang cookie iklan atau pelacak pihak
ketiga pada panel pelanggan.</p>

<h2>11. Anak di Bawah Umur</h2>
<p>Layanan kami ditujukan untuk pengguna berusia 18 tahun ke atas. Kami tidak dengan sengaja
mengumpulkan data pribadi anak di bawah umur. Bila Anda mengetahui hal tersebut, hubungi kami agar
kami dapat menghapusnya.</p>

<h2>12. Perubahan Kebijakan</h2>
<p>Kami dapat memperbarui kebijakan ini. Perubahan material akan diberitahukan melalui email atau
pengumuman di panel. Tanggal &ldquo;terakhir diperbarui&rdquo; di atas menunjukkan versi yang
berlaku.</p>

<h2>13. Kontak</h2>
<p>{operator}<br>{address}<br>Email: <a href="mailto:{support}">{support}</a><br>
Status layanan: <a href="{status}">{status}</a></p>
"""

# --------------------------------------------------------------- ID: Refund
REFUND_ID = """
<h1>Kebijakan Refund</h1>
<p class="sub">Terakhir diperbarui: {updated} · Berlaku untuk seluruh layanan berlangganan Instant
Server.</p>

<h2>1. Garansi Uang Kembali 7 Hari</h2>
<p>Untuk <strong>pembelian pertama</strong> layanan Cloud Server atau Object Storage, Anda dapat
mengajukan pengembalian dana penuh dalam <strong>7 hari kalender</strong> sejak layanan aktif, tanpa
perlu alasan. Garansi ini berlaku satu kali per pelanggan.</p>
<p>Garansi tidak berlaku untuk: perpanjangan langganan, langganan bulan kedua dan seterusnya,
add-on Backup Otomatis, dan biaya pihak ketiga yang sudah kami keluarkan atas nama Anda (misalnya
pendaftaran domain atau lisensi perangkat lunak).</p>

<h2>2. Cara Mengajukan Refund</h2>
<ol>
  <li>Kirim email ke <a href="mailto:{support}">{support}</a> dari alamat email akun Anda;</li>
  <li>Sertakan nomor faktur atau ID layanan dan alasan singkat;</li>
  <li>Kami konfirmasi penerimaan dalam maksimal 3 hari kerja dan menyelesaikan penilaian dalam
  maksimal 5 hari kerja;</li>
  <li>Dana dikembalikan ke metode pembayaran asal dalam maksimal 14 hari kerja setelah disetujui.
  Waktu tiba di rekening atau kartu Anda bergantung pada penyedia pembayaran.</li>
</ol>
<p>Bila pembayaran dilakukan melalui Creem (kartu), refund diproses melalui Creem
sesuai ketentuan mereka.</p>

<h2>3. Yang Tidak Dapat Dikembalikan</h2>
<ul>
  <li>Langganan bulan kedua dan seterusnya, serta perpanjangan otomatis yang sudah berjalan;</li>
  <li>Sisa periode setelah layanan dihentikan karena pelanggaran <a href="/terms">Syarat Layanan</a>
  atau kebijakan penggunaan yang dapat diterima;</li>
  <li>Add-on Backup Otomatis dan biaya layanan tambahan yang sudah terpakai;</li>
  <li>Biaya pihak ketiga (domain, lisensi, sertifikat, biaya transfer bank);</li>
  <li>Layanan yang ditangguhkan karena pelanggaran hukum atau permintaan aparat berwenang.</li>
</ul>

<h2>4. Pembatalan Langganan</h2>
<p>Anda dapat membatalkan langganan kapan saja dari panel klien. Pembatalan menghentikan penagihan
berikutnya dan berlaku pada akhir periode yang sudah dibayar — layanan tetap berjalan sampai tanggal
tersebut. Kami tidak memberikan refund prorata untuk periode berjalan, kecuali diwajibkan oleh
hukum.</p>

<h2>5. Kelebihan Pembayaran dan Gangguan Layanan</h2>
<p>Bila terjadi kelebihan pembayaran, kami mengembalikannya atau mengalihkannya sebagai kredit akun
atas persetujuan Anda. Bila kami gagal mengaktifkan layanan yang sudah Anda bayar karena sebab di
pihak kami, dana dikembalikan penuh.</p>

<h2>6. Chargeback</h2>
<p>Bila ada masalah tagihan, hubungi kami lebih dulu — hampir semua kasus dapat diselesaikan tanpa
sengketa bank. <em>Chargeback</em> tanpa upaya penyelesaian sebelumnya dapat menyebabkan penangguhan
layanan dan biaya administrasi sesuai ketentuan penyedia pembayaran.</p>

<h2>7. Kontak</h2>
<p>Semua permintaan refund: <a href="mailto:{support}">{support}</a> (Senin&ndash;Jumat
09.00&ndash;18.00 WIB).</p>
"""

# --------------------------------------------------------------- EN versions
TERMS_EN = """
<h1>Terms of Service</h1>
<p class="sub">Last updated: {updated} · Applies to <strong>instantserver.dev</strong> and
<strong>panel.instantserver.dev</strong> · The Indonesian version is the binding one.</p>

<div class="callout"><p><strong>Operator:</strong> {operator}, {address_en}
(&ldquo;we&rdquo;). By creating an account or ordering a service you agree to these Terms of Service,
our <a href="/en/privacy">Privacy Policy</a> and our <a href="/en/refund">Refund Policy</a>.</p></div>

<h2>1. Services We Provide</h2>
<p>Instant Server provides subscription-based digital infrastructure, provisioned automatically
through our panel:</p>
<ul>
  <li><strong>Cloud Server</strong> — virtual machines (VPS) with a public IPv4 address, full root
  access over SSH, NVMe storage and automatic HTTPS.</li>
  <li><strong>Object Storage</strong> — S3-compatible object storage.</li>
  <li><strong>Automatic Backup</strong> — optional recurring-backup add-on (see section 10).</li>
</ul>
<p>Services run in a data centre in Indonesia. The specifications of each plan (vCPU, memory,
storage, transfer) are listed on the pricing page and form part of this agreement.</p>

<h2>2. Accounts</h2>
<ul>
  <li>You must provide accurate, current and complete information when registering.</li>
  <li>You are responsible for keeping your credentials confidential and for all activity carried out
  through your account.</li>
  <li>One account is for one customer or one business entity. Accounts may not be resold or
  transferred without our written consent.</li>
  <li>We may request identity or business verification before activating services as part of our
  compliance obligations.</li>
</ul>

<h2>3. Orders and Activation</h2>
<ul>
  <li>Orders are processed automatically. Services normally go live within minutes of a confirmed
  payment; our target is under 5 minutes.</li>
  <li>If provisioning fails for reasons within our control we will activate the service manually or
  refund that order in full.</li>
  <li>Resource availability may depend on capacity in the selected location.</li>
</ul>

<h2>4. Pricing and Payment</h2>
<ul>
  <li>All prices are shown in US Dollars (USD) and <strong>exclude applicable taxes</strong>.
  Taxes are added to the invoice where required by law.</li>
  <li>Subscriptions are <strong>prepaid monthly</strong>. The service runs for the period paid.</li>
  <li>Card payments are processed by <strong>Creem</strong>, acting as Merchant
  of Record. For those transactions Creem is the seller to the end customer and handles the related
  tax compliance; Creem&rsquo;s own terms also apply.</li>
  <li>We do not store full card numbers. Payment data is processed directly by the payment
  provider.</li>
  <li>Invoices past their due date may lead to suspension as set out in section 5.</li>
  <li>Prices may change with at least 30 days&rsquo; notice before the next billing period. Changes
  are not retroactive for periods already paid.</li>
</ul>

<h2>5. Suspension and Termination</h2>
<ul>
  <li><strong>Overdue invoice:</strong> services are suspended 2 days after the due date and
  terminated 14 days after the due date.</li>
  <li><strong>Termination for non-payment:</strong> all data on that service is deleted and cannot be
  recovered. Our backups are not a substitute for your own data retention.</li>
  <li><strong>Policy violations:</strong> we may suspend or terminate immediately, without refund,
  for breaches of section 6, lawful requests from authorities, or security risks to our
  infrastructure and other customers.</li>
  <li>You may cancel at any time from the panel. Cancellation takes effect at the end of the paid
  period.</li>
</ul>

<h2>6. Acceptable Use Policy (AUP)</h2>
<p>You may not use our services for:</p>
<ul>
  <li>spam, phishing, fraud or social engineering of any kind;</li>
  <li>distributing malware, ransomware, botnets or other harmful software;</li>
  <li>attacking other systems, including mass port scanning, brute forcing, DDoS and unauthorised
  access attempts;</li>
  <li>cryptocurrency mining without our written permission;</li>
  <li>unlawful material, including child sexual abuse material, violent content and material
  infringing third-party intellectual property;</li>
  <li>unlicensed gambling, illegal financial services, or any activity unlawful under the laws of the
  Republic of Indonesia;</li>
  <li>public proxy/VPN services used for anonymous abuse, including as an egress path for the
  activities listed above;</li>
  <li>bulk email without opt-in and without complaint handling;</li>
  <li>storing or processing data that Indonesian law requires to be held on specifically certified
  infrastructure, where this service does not qualify;</li>
  <li>excessive use of shared resources that disrupts other customers.</li>
</ul>
<p>We may ask for an explanation of suspicious usage. If a violation is confirmed we may suspend the
service without refund and report it to the authorities where required.</p>

<h2>7. Refunds and Cancellation</h2>
<p>Full details are in the <a href="/en/refund">Refund Policy</a>. In short: a 7-day money-back
guarantee on the first purchase of a Cloud Server or Object Storage plan; third-party costs and
periods after the first month are non-refundable; cancellation is available at any time from the
panel and takes effect at the end of the current period.</p>

<h2>8. Service Level and Support</h2>
<ul>
  <li><strong>Availability target:</strong> 99.9% per month for network connectivity and host power.
  Announced scheduled maintenance, faults in your own service, and failures caused by your
  configuration do not count as downtime.</li>
  <li><strong>Support:</strong> {support}, Monday&ndash;Friday 09:00&ndash;18:00 WIB (Indonesian
  public holidays excluded). First-response target within 1 business day, resolution within 3
  business days.</li>
  <li><strong>Monitoring:</strong> service status is published at <a href="{status}">{status}</a>.</li>
</ul>

<h2>9. Customer Data and Privacy</h2>
<p>You own all data you upload to or process on the service. We process account and technical data as
described in the <a href="/en/privacy">Privacy Policy</a>. We do not access the contents of your
service unless you ask us to, or where the law requires it. You are responsible for the lawful
processing of any third-party personal data you store with us.</p>

<h2>10. Backups</h2>
<p>The <strong>Automatic Backup</strong> add-on is optional and priced at 20% of the plan price
(24-hour frequency; 12-hour and 6-hour options at an additional fee). It backs up your service data
periodically to our object storage.</p>
<p><strong>Without that add-on there are no automatic backups</strong> and you are fully responsible
for making your own. Backups complement, never replace, your own practices. Buying the add-on does
not grant us permission to run commands inside your server and does not change the privacy
policy.</p>

<h2>11. Intellectual Property</h2>
<p>All Instant Server software, branding and platform material remain ours or our licensors&rsquo;.
We grant you a limited, non-exclusive, non-transferable licence to use the service while this
agreement is in force. You grant us a limited licence solely to operate the service on your
behalf.</p>

<h2>12. Limitation of Liability</h2>
<p>To the extent permitted by law, our liability for any claim arising from this agreement is limited
to the service fees you paid for the month in which the claim arose. We are not liable for lost
profits, lost data or other indirect losses. We make no warranty that the service is fit for a
particular purpose beyond what is stated on the product page.</p>

<h2>13. Force Majeure</h2>
<p>We are not liable for failure or delay caused by events beyond our reasonable control, including
natural disasters, power outages, telecommunications failures, large-scale cyber attacks,
government action, or third-party failures.</p>

<h2>14. Changes to These Terms</h2>
<p>We may update these Terms. Material changes are announced by email to the registered address or in
the panel at least 14 days before they take effect. The &ldquo;last updated&rdquo; date above always
shows the version in force.</p>

<h2>15. Governing Law and Disputes</h2>
<p>This agreement is governed by the laws of the Republic of Indonesia. The parties will first try to
resolve disputes amicably; if that fails, disputes are settled before the competent courts in
Indonesia.</p>

<h2>16. Contact</h2>
<p>Questions about these Terms, billing, or support requests:
<a href="mailto:{support}">{support}</a>. Include your service ID or invoice number so we can help
faster.</p>
"""

PRIVACY_EN = """
<h1>Privacy Policy</h1>
<p class="sub">Last updated: {updated} · Applies to <strong>instantserver.dev</strong> and
<strong>panel.instantserver.dev</strong> · The Indonesian version is the binding one.</p>

<div class="callout"><p><strong>Data controller:</strong> {operator}, {address_en}. Questions or personal
data requests: <a href="mailto:{support}">{support}</a>. We respond within 3 business days.</p></div>

<h2>1. Summary</h2>
<p>We collect the data needed to create your account, provide the service, bill you and meet our legal
obligations. We do not sell your personal data, and we do not access the contents of your service
unless you ask us to or the law requires it.</p>

<h2>2. Data We Collect</h2>
<h3>a. Account and identity data</h3>
<ul>
  <li>Full name or business name, email address, phone/WhatsApp number;</li>
  <li>Billing address and, where required, business registration details for verification
  (<em>know your customer</em>);</li>
  <li>Account credentials (passwords are stored hashed, never in plain text).</li>
</ul>
<h3>b. Transaction data</h3>
<ul>
  <li>Order, invoice, subscription and payment-status history.</li>
  <li>We <strong>do not store full card numbers or CVCs</strong>. Card data is processed directly by
  the payment provider or Merchant of Record.</li>
</ul>
<h3>c. Technical and operational data</h3>
<ul>
  <li>IP address, access times, browser type and activity logs in the panel;</li>
  <li>Resource-usage metrics (CPU, memory, storage, data transfer) for billing and capacity
  management;</li>
  <li>Records of communication with our support team.</li>
</ul>
<h3>d. Data you store on the service</h3>
<p>The contents of your virtual servers and the objects you store in object storage remain yours. We
access them only when you request technical support, for maintenance you have approved, or where the
law requires it.</p>

<h2>3. Why We Process Data</h2>
<table>
  <tr><th>Purpose</th><th>Basis</th></tr>
  <tr><td>Creating your account and providing the service</td><td>Performance of contract</td></tr>
  <tr><td>Billing, invoicing and collecting overdue amounts</td><td>Performance of contract</td></tr>
  <tr><td>Fraud prevention, security, abuse prevention</td><td>Legitimate interest</td></tr>
  <tr><td>Technical support and service notices</td><td>Contract / legitimate interest</td></tr>
  <tr><td>Tax and legal compliance</td><td>Legal obligation</td></tr>
</table>

<h2>4. Payments and Merchant of Record</h2>
<p>Card payments are processed by <strong>Creem</strong> as Merchant of Record. In
that role Creem is the seller to the end customer and processes payment data and related tax
compliance under its own privacy policy. For local payments we use a licensed Indonesian payment
provider. We only receive transaction status (succeeded, failed, refunded), never card data.</p>

<h2>5. Sharing Data with Third Parties</h2>
<p>We share data only as far as necessary with:</p>
<ul>
  <li><strong>Infrastructure and data-centre providers</strong> — to run servers and storage;</li>
  <li><strong>Payment providers and the Merchant of Record</strong> — to process transactions and
  taxes;</li>
  <li><strong>Transactional email providers</strong> — to send invoices and service notices;</li>
  <li><strong>Law enforcement or regulators</strong> — where a lawful, binding request is made.</li>
</ul>
<p>We never sell, rent or trade your personal data. The provider list may change; the current version
is always on this page.</p>

<h2>6. International Data Transfers</h2>
<p>Some of our providers may operate outside Indonesia. Where personal data is transferred outside
Indonesia we ensure a lawful transfer basis and adequate safeguards under applicable law.</p>

<h2>7. Retention</h2>
<ul>
  <li>Account and service data: while the account is active;</li>
  <li>After account closure or service termination: deleted within 90 days, except records we must
  keep for tax and accounting purposes (generally 10 years under Indonesian tax rules);</li>
  <li>Technical logs: at most 30 days;</li>
  <li>Data on services terminated for non-payment is deleted at termination.</li>
</ul>

<h2>8. Security</h2>
<p>We apply reasonable technical and organisational measures: TLS encryption on all panel connections,
container isolation between customers, need-to-know staff access, regular backups and security
monitoring. No system is entirely risk-free; we will notify you of incidents affecting your personal
data as required by law.</p>

<h2>9. Your Rights</h2>
<p>Under Indonesia&rsquo;s Personal Data Protection Law (Law No. 27 of 2022) you have the right to:</p>
<ul>
  <li>be informed about the personal data we process and why;</li>
  <li>request access to and a copy of your personal data;</li>
  <li>request correction of inaccurate data;</li>
  <li>request deletion, where it does not conflict with our legal obligations;</li>
  <li>withdraw consent and object to certain processing;</li>
  <li>lodge a complaint with us and, if needed, with a supervisory authority.</li>
</ul>
<p>Send requests to <a href="mailto:{support}">{support}</a>. We may ask you to verify your identity
before acting on a request.</p>

<h2>10. Cookies and Similar Technologies</h2>
<p>We use only cookies required to operate the service: login-session and security cookies (for
example CSRF protection). We do not place advertising cookies or third-party trackers in the customer
panel.</p>

<h2>11. Children</h2>
<p>Our services are intended for users aged 18 and over. We do not knowingly collect personal data
from children. If you become aware of this, contact us so we can delete it.</p>

<h2>12. Changes to This Policy</h2>
<p>We may update this policy. Material changes are announced by email or in the panel. The
&ldquo;last updated&rdquo; date above shows the version in force.</p>

<h2>13. Contact</h2>
<p>{operator}<br>{address_en}<br>Email: <a href="mailto:{support}">{support}</a><br>
Service status: <a href="{status}">{status}</a></p>
"""

REFUND_EN = """
<h1>Refund Policy</h1>
<p class="sub">Last updated: {updated} · Applies to all Instant Server subscription services.</p>

<h2>1. 7-Day Money-Back Guarantee</h2>
<p>On the <strong>first purchase</strong> of a Cloud Server or Object Storage plan you may request a
full refund within <strong>7 calendar days</strong> of the service going live, without giving a
reason. The guarantee applies once per customer.</p>
<p>It does not cover renewals, the second and later subscription months, the Automatic Backup add-on,
or third-party costs already incurred on your behalf (for example domain registration or software
licences).</p>

<h2>2. How to Request a Refund</h2>
<ol>
  <li>Email <a href="mailto:{support}">{support}</a> from your account email address;</li>
  <li>Include the invoice number or service ID and a short reason;</li>
  <li>We confirm receipt within 3 business days and complete the assessment within 5 business
  days;</li>
  <li>Funds are returned to the original payment method within 14 business days of approval. The time
  to reach your account or card depends on the payment provider.</li>
</ol>
<p>Where payment was made through Creem (cards), refunds are processed through Creem
under their terms.</p>

<h2>3. What Cannot Be Refunded</h2>
<ul>
  <li>The second and later subscription months, and automatic renewals already processed;</li>
  <li>Remaining periods after termination for breach of the <a href="/en/terms">Terms of Service</a>
  or the acceptable use policy;</li>
  <li>The Automatic Backup add-on and additional services already consumed;</li>
  <li>Third-party costs (domains, licences, certificates, bank transfer fees);</li>
  <li>Services suspended for legal violations or at the request of authorities.</li>
</ul>

<h2>4. Cancelling a Subscription</h2>
<p>You can cancel at any time from the client panel. Cancellation stops the next charge and takes
effect at the end of the paid period — the service keeps running until that date. We do not refund
the current period pro rata unless the law requires it.</p>

<h2>5. Overpayments and Service Failures</h2>
<p>Overpayments are refunded or converted into account credit with your agreement. If we fail to
activate a service you paid for for reasons on our side, the amount is refunded in full.</p>

<h2>6. Chargebacks</h2>
<p>If you have a billing problem, contact us first — almost every case can be resolved without a bank
dispute. A chargeback raised without first contacting us may lead to suspension and administration
fees as set by the payment provider.</p>

<h2>7. Contact</h2>
<p>All refund requests: <a href="mailto:{support}">{support}</a> (Monday&ndash;Friday
09:00&ndash;18:00 WIB).</p>
"""


def render(body, lang):
    upd = UPDATED if lang == "id" else UPDATED_EN
    return body.format(
        updated=upd,
        support=SUPPORT,
        status=STATUS,
        operator=OPERATOR,
        address=OPERATOR_ADDRESS,
        address_en=OPERATOR_ADDRESS_EN,
    )


def titles(body):
    first = body.strip().split("\n", 1)[0]
    t = first.replace("<h1>", "").replace("</h1>", "").strip()
    return t


PAGES = [
    ("terms.html", "id", "terms", TERMS_ID, NAV_ID,
     "Syarat layanan Instant Server: harga, penagihan, penangguhan, penggunaan yang dapat diterima, SLA dan refund."),
    ("privacy.html", "id", "privacy", PRIVACY_ID, NAV_ID,
     "Kebijakan privasi Instant Server: data yang dikumpulkan, dasar pemrosesan, retensi, keamanan dan hak Anda."),
    ("refund.html", "id", "refund", REFUND_ID, NAV_ID,
     "Kebijakan refund Instant Server: garansi uang kembali 7 hari, cara mengajukan, dan pengecualian."),
    ("en/terms.html", "en", "terms", TERMS_EN, NAV_EN,
     "Instant Server terms of service: pricing, billing, suspension, acceptable use, SLA and refunds."),
    ("en/privacy.html", "en", "privacy", PRIVACY_EN, NAV_EN,
     "Instant Server privacy policy: data we collect, why we process it, retention, security and your rights."),
    ("en/refund.html", "en", "refund", REFUND_EN, NAV_EN,
     "Instant Server refund policy: 7-day money-back guarantee, how to request a refund, and exclusions."),
]

if __name__ == "__main__":
    for path, lang, kind, body, nav, desc in PAGES:
        p = Path(path)
        if p.parent != ROOT:
            p.parent.mkdir(parents=True, exist_ok=True)
        page(path, lang, titles(body), desc, render(body, lang), nav)
    print("done")
