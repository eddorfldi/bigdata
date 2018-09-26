# ini adalah cara membuat Nested List Comprehensions dalam python

# Pertama buat variable matrix dalam bentuk array 
>>> matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],]

# buat variable baru dengan nama transposed
>>> transposed = []
>>> for i in range(4):

# tambahkan append untuk menambah data baru, dan disini jenis dimensi array akan berbeda karena sudah di atur pada  for sebelumnya.
...     transposed.append([row[i] for row in matrix])
...

>>> transposed
# Hasil dari transposed setelah arraynya di ubah.
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
