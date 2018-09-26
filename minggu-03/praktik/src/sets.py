# Contoh beberapa perintah dari statment sets di Python

>>> a = set('abracadabra')
>>> b = set('alacazam')

# Mengetahui dalam variable a terdapat huruf atau nilai apa saja yang terdapat
>>> a
{'r', 'd', 'b', 'c', 'a'}

# Fungsi ini seperti irisan pada perhitunga matematika
>>> a - b
{'b', 'r', 'd'}
>>> a | b
{'m', 'r', 'd', 'z', 'b', 'c', 'a', 'l'}
>>> a & b
{'c', 'a'}
>>> a ^ b
{'m', 'r', 'z', 'd', 'b', 'l'}
