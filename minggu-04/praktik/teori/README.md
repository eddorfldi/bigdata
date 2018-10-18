Airbnb memiliki lebih dari 100+ kontributor yang menulis Pipeline Flow dari AirFlow.<br>
Di data enginnering sendiri, abstrack sering diartikan sebagai mengidentifikasi dan mengoptimasikan pola ETL. <br>

Mengidentifikasi tabel fakta dan dimensi yang releva untuk enghitung mertrik yag diaman terdiri dari beberapa potongan dimensi yang berguna<br>

Implikasi dari framework, mereka atau framework secara praktis meningkatkan cata kerja data scientist.<br>
Input : Tempat end-user menemtukan bagaimana memberikan nilai pada skala <br>
Data Processing : Ini inti dari semua framework daya enginering, dimana Pipelines ETL dipakai secara dinamis.<br>
Output : DAG yang dihasilkan dari langkah sebelumnya membuat data turunan dan hasulnya sering disipan dalam tabel.<br>


# Incrementa Computation Framework
Untuk menghitung pro-metrik ini sehingga end-user hanya perlu mereferensikan metrik dalam satu / lebih beberapa data dari table ringaksan. Input : menentukan metrik mana yang harus dihitung dan tabel <br>
Data Processing : menyatukan tabel ringkasan dari partisi sebelumnya dengan tabel fakta.<br>
Output: mengoptimalisasikan tabel yang dimana jumlah kumulatif sangat banyak.<br>

Ini membangun user untuk menghindari pola query yang tidak efisien dan mengoptimasikan agerasi yang memnosankan

# Backfilling Framework
Strategi yang termasuk partisi dinamis dan backfiling logic ke SQL enggunakan Jinjja Template.<br>
Input : UI sederhana tempat pengguna dapat menentukan nama pekerjaan, tangga mulai, tanggal akhir dari perkejaan untuk paralelisasi.<br>
Data Processing : Mementukan bagaimana backfilling senity Check, Snap Staging Stage akan dijalankan, kerangka kerja membuar airflow line. <br>
Output: Sebuah tabel yang sepenuhnya siap untuk digunakan. <br>

Ini mernitimasikan jaminan kualitas dengan menyiapkan perbandingan otomatis dan tabel dengan produksi setelah di Tes.

# Global Metrik Framework
Mengidentifikasikan resource yang benar untuk menentukan metrik dan dimensi.
Input : Menentukan satu atau lebih metrik yabel fakta dalam tabel akhir, kunci primer dan foreign key untuk bergabung.
Data Processing : Mengidentifikasi metrik dan potongan dimensi lalu mengabungkan tabel dimensi dengan tabel fakta untuk membuat tabel denormalited sevara otomatis <br>
Output : Kumpulan metrik yang sama tetapi di demnsi yang berbeda.

Yang nantinya digunakan di daskboard, analitik dan banyak lagi.

<br>

# Expremiantation Reporting Framework
Semua lapisan lebih komplek dibanding sebelumnya memungkinkan produk di perusahaan untuk menjalankan ratusan/ / ribuan eksperimen secara bersama <br>
Input : Membangun UI sehingga user dapat menjalankan dengan baik.<br>
Data Processing : Metrik pipeline yang menghitung untuk setiap eksperimen, metrik singkat subjek dan dimensi yang sesuai.<br>
Output : Menyiapkan data untuk ditampilkan di UI. <br>

Framework ini adalah pengganda yang luar biasa untk kerja dan alur kerja para data scientist dan data enginner adlah bidang yang penting tetapi kurang dihargai.<br>
