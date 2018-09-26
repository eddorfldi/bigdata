# dibawah ini adalah source code untuk del statement

>>> a = [-1,1,66.25,333,333,1234.5]

# perintah del stat array 0
>>> del a[0]

>>> a
[1, 66.25, 333, 333, 1234.5]

# perintah del stat  2:4 artinya hapus dari array 2 sampai sebelum 4 
>>> del a[2:4]

>>> a
[1, 66.25, 1234.5]

# perintah del stat untuk semua nilai pada satu array
>>> del a[:]
>>> a
[]
