# dibawah ini merupakan fungsi dari penggunaam raise dan finally ketika user salah memasukkan sesuatu pada saat pengetikan code

>>> try :
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
