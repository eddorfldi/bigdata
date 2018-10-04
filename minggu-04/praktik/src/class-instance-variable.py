# Pertama buat class terlebih dahulu, dimana dalam class tersebut terdapat beberapa module yang akan digunakan

>>> class Dog:
...     def __init__(self,name):
...             self.name = name
...             self.tricks = []
...     def add_trick(self,trick):
...             self.tricks.append(trick)
...

# buat sebuah variable terlebih dahulu
>>> d = Dog('Fido')
>>> e = Dog('Horsea')

# kemudian tambahkan sebuah action pada setiap variable
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')

# berikut ini adalah hasil dari action pada setiap variable
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
