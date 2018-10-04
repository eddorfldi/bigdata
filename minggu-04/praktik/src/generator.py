# buat sebuah module reverse dan buat pehitungan range

>>> def reverse(data):
...     for index in range(len(data)-1,-1,-1):
...             yield data[index]
...

# setelah itu forkan nilai reverse tersebut
>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g
