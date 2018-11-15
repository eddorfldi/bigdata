- DE mengambil data agar DW (Data Warehouse) terisi.

- Tugas dari DE (Data Engineering) adalah merangcang, membangun dan memaintance DW.

- Kebutuhan metrix = kebutuhan pengukuran.

- Data backfilling yaitu data history.

- Data modelling = membuat production (DB yang digunakan untuk keperluan realdata) database bisa digunakan oleh OLAP (On Line Analytics Processing)

- Problem yaitu ada normalisasi dan de-normalisasi

- Airbnb memmbuat star schema . Teknik ini sudah lama ada, tetapi dibuat dengan nama baru oleh airbnb. Fact and Dimention tables, 
      Teknik ini biasanya digunakan para developer dengan istilah transcation tables, parameter tables dan temporary table.
      
- Tugas dari DE merupakan memikirkan bagaimana semua data yang ada mudah di-query dan digunakan untuk sebagai perhitungannya.

- Data Partitioning merupakan data tidak disimpan dalam suatu bagian khusus, tetapi dipotong-potong

- Apache Airflow merupakan konsep ETL yang kompleks, dimana apache airflow menyediakan framework untuk mengelola ETL. Di representasikan dalam bentuk 
    DAG (Direct Acyclic Graph)
 
- DE mendefinisikan DAG yang dependensi antar task

- ETL Best Practice = 1. Partisi Table Data
                      2. Load Data secara incremental
                      3. Enforce idempotency = tidak bisa mengubah data untuk data history
                      4. Parameter workflow
                      5. Early opendata Check
                      6. Alerts and Monitoring System
                     
