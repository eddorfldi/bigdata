## 5.1.1. Using Lists as Stacks
> ` stack = [3,4,5]`<br>
` stack.append(6)`<br>
` stack.append(7)`<br>
` stack`<br>
`[3, 4, 5, 6, 7]`<br>
` stack.pop()`<br>
`7`<br>
` stack`<br>
`[3, 4, 5, 6]`<br>

Sebuah method list yang digunaakan untuk membuat tumpukan list. <br>
Nilai yang terakhir di tambah adalah nilai yang pertama kali akan dikeluarkan.<br>
untuk penggunaan stack, stack = [3,4,5], dan menambah nilai bisa dengan append, <br>
stack.append(6). maka hasilnya stack = [3,4,5,6].<br>
mengeluarkan nilai dapat menggunakan stack.pop(). maka stack = [3,4,5]

## 5.1.2. Using Lists as Queues
> ` from collections import deque`<br>
` queue = deque(["Eric","John","Michael"])`<br>
` queue.append("Terry")`<br>
` queue.popleft()`<br>
` 'Eric'`<br>
` queue`<br>
`deque(['John', 'Michael', 'Terry'])`<br>

Fungsi dari queue, element atau nilai pertama masuk adalah nilai yang pertama juga keluar<br>
Penggunaan Queues ini harus mengimport sebuah file bernama deque dari collections.<br>
hampir sama dengan Stack, queue punya perintah append untuk menambah, dan popleft menguluarkan nilai
dari kiri.

## 5.1.3. List Comprehensions
> ` combs = []`<br>
` for x in [1,2,3]:`<br>
`     for y in [3,1,4]:`<br>
`             if x != y:`<br>
`                     combs.append((x,y))`<br>
`...`<br>
` combs`<br>
`[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]`<br>

Contoh list dengan penggunaan for dan if statements di satu list yang sama.<br>
Ini akan membuat sebuah list yang baru dengan format x,y seperti diatas. <br>

## 5.1.4. Nested List Comprehensions
> ` matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],]`<br>
` transposed = []`<br>
` for i in range(4):`<br>
`     transposed.append([row[i] for row in matrix])`<br>
`...`<br>
` transposed`<br>
`[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]`<br>

Penggunaan diatas, pertama buat dulu variable dengan nama matrix, <br>
kemudian pakai transposed statement, transposed statement akan membuat nilai array yang beru <br>
sesuai dengan range atau nilai yang dimasukkan contoh seperti di atas. <br>

## 5.2. Del Statement
> ` a = [-1,1,66.25,333,333,1234.5]`<br>
` del a[0]`<br>
` a`<br>
`[1, 66.25, 333, 333, 1234.5]`<br>
` del a[2:4]`<br>
` a`<br>
`[1, 66.25, 1234.5]`<br>
` del a[:]`<br>
` a`<br>
`[]`<br>

Del statement ini berfungsi sebagai menghapus nilai pada array yang sudah dibuat. <br>
berbeda dengan pop(), pop() memilih nilai mana yang akan dihapus, seperti pop() yang last-in first-out <br>
ataupun popLeft() yang first-in first-out. <br>

## 5.3. Tuples and Sequences
> ` t = 12345, 54321, 'hello!'`<br>
` t[0]`<br>
`12345`<br>
` t`<br>
`(12345, 54321, 'hello!')`<br>
` u = t, (1,2,3,4,5)`<br>
` u`<br>
`((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))`<br>
` t[0] = 88888`<br>
`Traceback (most recent call last):`<br>
`  File "<stdin>", line 1, in <module>`<br>
`TypeError: 'tuple' object does not support item assignment`<br>
` v = ([1,2,3],[3,2,1])`<br>
` v`<br>
`([1, 2, 3], [3, 2, 1])`<br>

Fungsi 'tuple' merupakan statement untuk menyimpan data-data. Tetapi isi 'tuple' tidak bisa dihapus.<br>

## 5.4. Sets
> ` a = set('abracadabra')`<br>
` b = set('alacazam')`<br>
` a`<br>
`{'r', 'd', 'b', 'c', 'a'}`<br>
` a - b`<br>
`{'b', 'r', 'd'}`<br>
` a | b`<br>
`{'m', 'r', 'd', 'z', 'b', 'c', 'a', 'l'}`<br>
` a & b`<br>
`{'c', 'a'}`<br>
` a ^ b`<br>
`{'m', 'r', 'z', 'd', 'b', 'l'}`<br>

Fungsi sets seperti fungsi irisan pada matematika,<br>
seperti contoh 'a - b', berarti irisan a yang tidak ada di b. <br>
atau 'a | b' nilai irisan a berada juga di b atau keduanya. <br>

## 5.5. Dictionaries
> ` tel = {'jack': 4098, 'sape': 4139}`<br>
` tel['guido'] = 4127`<br>
` tel`<br>
`{'jack': 4098, 'sape': 4139, 'guido': 4127}`<br>
` del tel['sape']`<br>
` tel`<br>
`{'jack': 4098, 'guido': 4127}`<br>
` list(tel)`<br>
`['jack', 'guido']`<br>
` sorted(tel)`<br>
`['guido', 'jack']`<br>
` 'guido' in tel`<br>
`True`<br>
` 'jack' not in tel`<br>
`False`<br>

Fungsi Dictionaries adalah mengelompokkan beberapa array menjadi satu array yang terdiri, <br>
dari beberapa array yang sudah dikumpulkan. <br>
ada fungsi 'del' dimana sudah dijelaskan berfungsi untuk menghapus sebuah array. <br>

## 5.6. Looping Techniques
> ` knight = {'gallahad': 'the pure','robin':'thebrave'}`<br>
` for k, v in knight.items():`<br>
`     print(k,v)`<br>
`...`<br>
`gallahad the pure`<br>
`robin thebrave`<br>

Loop ini menjelaskan perulangan yang sesuai dengan nilai yang sama, contoh for k,v <br>
berarti 'gallahad' mempunyai nilai pasangan berulangnya adalah 'the pure'.<br>
Dan, nilai itu akan di ulangkan sampai value dari variable knight, habis atau tidak tersisa nilai lagi untuk ditmapilkan. <br>

## 5.7. More on Conditions
> ` string1, string2, string3 = '','Trondheim','Hammer Dance'`<br>
` not_null = string1 or string2 or string3`<br>
` not_null`<br>
`'Trondheim'`<br>

More no Conditions adalah konsep atau sebuah fungsi untuk mendapatkan nilai menggunakan <br>
boolean operators seperti 'and' dan 'or' dan di panggil dengan 'short-circuit' operasi.<br>
ini untuk memilih nilai mana yang harus di ambi, jika a dan c bernilai true dan b false, <bR>
maka nilai tersebut aka mengambil nilai b.

##5.8. Comparing Sequences and Other Types
> ` (1,2,3) < (1,2,4)`<br>
`True`<br>
` 'abc'<'c'<'pascal'<'Python'`<br>
`False`<br>
` (1,2,3) == (1.0,2.0,3.0)`<br>
`True`<br>

Fungsi ini menentukan antara kedua nilai, mana yang bersifat true dan false. <br>
