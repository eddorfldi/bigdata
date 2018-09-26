# Perintah yang digunakan pada statment dictionaries

>>> tel = {'jack': 4098, 'sape': 4139}

# Menambah nilai pada variable tel
>>> tel['guido'] = 4127

>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}

# fungsi del disini sama seperti del statment, menghapus nilai array.
>>> del tel['sape']
>>> tel
{'jack': 4098, 'guido': 4127}

# membuat list dari variable tel
>>> list(tel)
['jack', 'guido']

# mensortir variable tel
>>> sorted(tel)
['guido', 'jack']

# contoh mengecek apakah nilai tersebut ada di dalam variable
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
