# Contoh kodingan untuk List Comprehensions

# buat variable combs dengan isian valuenya adalah array  
>>> combs = []

# buat perulangan
>>> for x in [1,2,3]:

# untuk di Python sendiri jika mau meneruskan sebuah method tidak boleh sejajar dengan methodnya, jadi tekan tab untuk membuatnya sedikit lebih dalam
...     for y in [3,1,4]:
...             if x != y:

# tambahan append untuk menambah nilai array yang ada di for
...                     combs.append((x,y))
...

# untuk cek hasil, ketik combs lagi
>>> combs
# hasil dari variable combs
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
