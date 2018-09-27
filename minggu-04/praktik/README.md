# 6. Modules

Pertama buat file fibo.py di folder Python seperti contoh D:\python<br>
di dalam file fibo.py , copy kan code berikut ini:

> `def fib(n):    # write Fibonacci series up to n` <br>
`    a, b = 0, 1` <br>
`    while a < n:` <br>
`        print(a, end=' ')` <br>
`        a, b = b, a+b` <br>
`    print()` <br>
`##` <br>
`def fib2(n):   # return Fibonacci series up to n
`    result = []` <br>
`    a, b = 0, 1` <br>
`    while a < n:` <br>
`        result.append(a)` <br>
`        a, b = b, a+b` <br>
`    return result` <br>

Setelah itu save di D:\python.<br>
Kemudian di Python 3.7.exe jalankan code seperti di bawah: <br>

> `import sys`<br>
`sys.path.append(r'D:\python')`<br>
`import fibo`<br>

maka fibo selesai di import. Kemudian coba fibo tersebut dengan code dibawah : <br>

> `fibo.fib(1000)`<br>

Maka hasilnya seperti di samping : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987


# 6.1 More on Modules

> `import fibo as fib`<br> 
`fib.fib(500)`<br>

Maka hasilnya : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
 
Maksud dari 'as' adalah inisialisasi nama file untuk mempersingkat code. <br>


# 6.2 Standard Modules

> ` import sys`<br>
` sys.ps1`<br>
`'>>> '`<br>
` sys.ps1 = 'C>'`<br>
`C>print('Yeah!')`<br>
`Yeah!`<br>
`C>`<br>

Membuat sebuah perintah menuju directory C. <br>


# 6.3 The dir() Function

> ` a = [1,2,3,4,5]`<br>
` fib = fibo.fib`<br>
` dir()`<br>
`['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'fib', 'fibo', 'sys']`<br>

Fungsi dir adalah fungsi mem-builtin apa saja yang sudah di built. <br>

# 6.4
