# 10.1 Operating System Interface

>` >>> import os`<br>
`>>> os.getcwd()`<br>
`'C:\\Users\\Gucci Genk\\AppData\\Local\\Programs\\Python\\Python37-32'`<br>
`>>> os.system('mkdir today')`<br>
`0`<br>

Disini menampilkan informasi letak dari program python yang dimilii, dan os.system itu mengecek apa ada penambahan dir hari ini.


# 10.2 File Wildcards
>` >>> import glob`<br>
`>>> glob.glob('*.py')`<br>
`[]`<br>

Mengimport func glob

# 10.3 Command Line Arguments
>` >>> import sys`<br>
`>>> print(sys.argv)`<br>
`['']`<br>

ini mengimport func sys, dimana akan menampilkan system apa saja yang sudah terinstall pada python

# 10.4 Error Output Redirection and Program Termination
>` >>> sys.stderr.write('Warning, log file not found\n')`<br>
`Warning, log file not found`<br>
`28`<br>

Ini akan memunculkan warningnya dan berapa panjang dari warning tersebut

# 10.5 String Pattern Matching
>` >>> import re` <br>
`>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')` <br>
`['foot', 'fell', 'fastest']` <br>
`>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')` <br>
`'cat in the hat'` <br>

mengimport func re dimana akan mengecek string-string yang ada

# 10.6 Mathematics
>` >>> import math`<br>
`>>> math.cos(math.pi/4)`<br>
`0.7071067811865476`<br>

mengimport math, fungsinya adalah mengimport logika matematika di python. seperti diatas menampilkan cos dari pi/4.

# 10.9 Data Compressio
>` >>> import zlib`<br>
`>>> s = b'witch which has which witches wrist watch'`<br>
`>>> len(s)`<br>
`41`<br>
`>>> t = zlib.compress(s)`<br>
`>>> len(t)`<br>
`37`<br>

mengimport func zlib, dimana sama menghitung panjang string, tetapi ketika menggunakan zlib panjang tersebut berkurang karena spasi <br>
atau whitespace tidak dihitung.

# 10.10 Performance Measurement
>` >>> from timeit import Timer`<br>
`>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()`<br>
`0.06280662799997572`<br>

Mengimport timer, ini menunjukan perhitungan waktu.

# 11.1 Output Formatting
>` >>> import reprlib`<br>
`>>> reprlib.repr(set('supercalifragilisticexpialidocious'))`<br>
`"{'a', 'c', 'd', 'e', 'f', 'g', ...}"`<br>

mengimport func reprlib, ini berfungsi mengecek kata apa saja yang terdapat pada string tersebut

# 11.2 Templating
>` >>> from string import Template`<br>
`>>> t = Template('${village}folk send $$10 to $cause.')`<br>
`>>> t.substitute(village='Nottingham', cause='the ditch fund')`<br>
`'Nottinghamfolk send $10 to the ditch fund.'`<br>

berfungsi sebagai template jadi tidak perlu untuk mengetikkan cukup menggunakan template yang sudah dibuat.

# 11.7 Tools for Working with List
>` >>> from array import array`<br>
`>>> a = array('H',[4000,10,700,22222])`<br>
`>>> sum(a)`<br>
`26932`<br>
`>>> a[1:3]`<br>
`array('H', [10, 700])`<br>

Func array, dimana menggunakan array dimensi didalamnya dan cara memanggil dari array tersebut.

# 11.8 Decimal Floating Point Arithmetic
>` >>> from decimal import *`<br>
`>>> round(Decimal('0.70') * Decimal('1.05'),2)`<br>
`Decimal('0.74')`<br>
`>>> round(.70 * 1.05, 2)`<br>
`0.73`<br>
`>>> Decimal('1.00') % Decimal('.10')`<br>
`Decimal('0.00')`<br>
`>>> 1.00 % 0.10`<br>
`0.09999999999999995`<br>
`>>> sum([Decimal('0.1')]*10) == Decimal('1.0')`<br>
`True`<br>

diatas merupakan aritmatika dari desimal pada python, cara penggunaan dan mengimport func Decimal

# 12.1 Virtual Environments and Packages
>` >>> import sys`<br>
`>>> sys.path`<br>
`['', 'C:\\Users\\Gucci Genk\\AppData\\Local\\Programs\\Python\\Python37-32\\python37.zip', 'C:\\Users\\Gucci Genk\\AppData\\Local\\Programs\\Python\\Python37-32\\DLLs', 'C:\\Users\\Gucci Genk\\AppData\\Local\\Programs\\Python\\Python37-32\\lib', 'C:\\Users\\Gucci Genk\\AppData\\Local\\Programs\\Python\\Python37-32', 'C:\\Users\\Gucci Genk\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\site-packages']`<br>

Mengecek env atau package apa saja yang sudah terinstall
