# Berikut ini beberapa contoh exception yang ada di python

# contoh exception ketika mendapat nilai 0 atau zero
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

# contoh ketika mendapat sebuah variable yang tak terdefinisikan terlebih dahulu
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined

# contoh ketika terdapat string disaat melakukan perhitungan 
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
