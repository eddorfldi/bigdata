# membuat model dengan nama scope_test kemudian membuat beberapa model lagi didalammnya
>>> def scope_test():
...     def do_local():
...             spam = "local spam"
...     def do_nonlocal():
...             nonlocal spam
...             spam = "nonlocal spam"
...     def do_global():
...             global spam
...             spam = "global spam"
...     spam = "test spam"
...     do_local()
...     print("After local assigment:", spam)
...     do_nonlocal()
...     print("After nonlocal assigment:", spam)
...     do_global()
...     print("After global assigment:", spam)
...

# kemudian coba print model tersebut
>>> scope_test()

# maka yang keluar seperti dibawah ini
After local assigment: test spam
After nonlocal assigment: nonlocal spam
After global assigment: nonlocal spam

# ini contoh memanggil sebuah variable spam yang berada di dalam module scope_test
>>> print("In global scope:" ,spam)
In global scope: global spam
