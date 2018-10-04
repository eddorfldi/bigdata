# membuat sebuah class yang dimana didalam class tersebut terdapat beberapa object

>>> class Complex:
...     def __init__(self, realpart, imagpart):
...             self.r = realpart
...             self.i = imagpart
...

# contoh pemanggilan class Complex yang sudah dibuat diatas
>>> x = Complex(3.0,-4.5)
>>> x.r,x.i
(3.0, -4.5)
