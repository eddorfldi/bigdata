# Pertemuan minggu-03 Teori BIG DATA (20/09/2018)

Data Enginnering = membangun arsitektur managemen data dan infrastuktur big data dam mengammbil beberapa data yang penting dan dibutuhkan.

Data Science dari hirarki kebutuhan

> 1. AL, DEEP LEARNING
2. A/B TESTING, EXPERMENTION, SIMPLE ML ALGORITHMS 
3. ANALYTORS, METRICS, SEGMENTS, AGGREGATES, FEATURES, TRAINING DATA
4. CLEANING, PREP, ANOMALY DETECTION
5. RELIABLE DATA FLOW, INFRASTUCTURE, PIPELINES, ETL, STRUCTURED AND UNSTRUCTURED DATA STROAGES
6. INSTRUMENTATION, LOGGING, SENSORS, EXTERNAL DATA, USER GENERATED CONTENT

Data Warehouse merupakan tempat atau wadah kumpulan data dari internal dan eksternal yang sudah tersaring.

Mengapa Data Warehouse penting :
> 1. Tanpa DW atau Data warehouse akan menjadi mahal dan tidak scalable
2. Hasil akan bisa berbeda dengan "pertanyaan" yang sama
3. Banyak Aktivitas yang akan mengulang

ETL Software: 
> 1. Azkaban = LinkedIn
2. Luigi   = Spotify
3. Airbow  = Airbnb
4. Pinball = Pinterest

Pertimbangan dalam memilih DW 
> 1. Konfigurasi, Configuration as Code. Memudahkan dalam mengkonfigurasi karena dalam berbentuk kode.
2. UI, Monitoring, Alert : Terutama karena data enginnering biasanya akan langsung batch proccesing.
3. Backfilling : Fasilitas untuk memproses data histori
