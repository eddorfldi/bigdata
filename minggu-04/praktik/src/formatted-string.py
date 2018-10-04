# code dibawah merupakan cara memformat sebuah string menjadi sebuah array

>>> table = {'Sjoerd' : 4127, 'Jack' : 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...

# Diatas merupakan print diatas didalam for
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
