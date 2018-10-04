# Sama dengan sebelumnya, buat class dan didalamnya ada module.
>>> class Reverse:
...     def __init__(self, data):
...             self.data = data
...             self.index = len(data)
...     def __iter__(self):
...             return self
...     def __next__(self):
...             if self.index == 0:
...                     raise StopIteration
...             self.index = self.index - 1
...             return self.data[self.index]
...

# kemudian panggil class tersebut dan didalamnya bawa variable spam
>>> rev = Reverse('spam')
>>> iter(rev)

# terbaca sebagai sebuah object 
<__main__.Reverse object at 0x00957910>

# kemudian for kan dari variable rev
>>> for char in rev:
...     print(char)
...

# ini hasilnya 

m
a
p
s
