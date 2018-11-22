# PERMULAIAN UNTUK PENGGUNAAN DATA STUKTUR

  Secara singkat, keseluruhan non-comperhensif dari fundamental data struktur di pandas dapat dimulai. <br>
  Dimulai dengan tipe, index dan label. Untuk memulai harus mengimport NuPy dan masukkan pandas di namespace.<br>
  
>`  In [1] : Import numpy as py `<br>
 `  In [2] : Import pandas as pd `<br>
 
 Disini dapat diketahui dara alignment adalah dasarnya. Link antara label dan data tidak bisa dipisahkan. Ini memberi permulaan tentang
 data struktur lalu mempertimbangkan fungsi kategori dan method pemisah.
 
 * Series
  Merupakan 1 dimensi label array yang menampug semua tipe data(Interger, string, float, nomor, objek python dll).
  Method dasar membuat series dapat dipanggil dengan contoh :
  
 >` >>> s = pd.Series(data, index=indesx) `
 
  Diatas terdapat "data" yang punya banyak arti seperti dict python, ndarray dan scalar value.
  
  - Untuk ndarray, index harus memiliki nilai yang sama dengan data. Jika tidak ada index, maka akan terbentuk value seperti dibawah
>` [0, ...., len(data-1)] `

  - Untuk dict, jika menggunakan python dengan versi lebih rendah dari 3.6 atau versi pandas yang lebih rendah 0.23
  maka penggunaan dict keysnya
 >` (i.e['a','b','c'] rether than ['b','a','c'])`
 
 - Untuk scalra value, index harus disediakan. nilai akan terus diulang dan meyesuiakan panjang dari index.
 
 * Series is ndarray-like, berintadak seperti ndarray pada umumnya dan bisa menggunakan argument dari fungsi numPy. Namun, operasi ini akan 
 memotog dari index tersebut.
 
 * Series is dict-like, akan memperbaiki ukuran dict yang didapat dan akan memasukkan value tersebut kedalam index.
 
 * Operan Vectorized dan Alignment label bersama Series. 
    Saat menggunakan secara bersama, array numPy akan melakukan perulangan terus menerus dilakukan secara value-by-value dan tidak seperti
    pada umumnya. Ini biasanya bekerja efektif atau benar dengan Series di Pandas. Perbedaan antara Series dan Ndrarray adalah operasi perbedaan 
    yang otomatis data based di label. Hasil dari operasi antara unaligned Series adalah terdapat union penyelesaian sebuah index.
      
  
