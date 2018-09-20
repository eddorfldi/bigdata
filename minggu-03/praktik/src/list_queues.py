# Ini kodingan untuk list of queues

# Import deque dari kelas collections 
>>> from collections import deque

>>> queue = deque(["Eric","John","Michael"])

# append digunakan untuk menambah data
>>> queue.append("Terry")

>>> queue.popleft()
# Hasil setelah di queue.popleft() mengeluarkan nilai paling ujung kiri atau nilai yang pertama kali masuk.
# 'Eric'

>>> queue
# Hasil queue setelah di queue.popleft()
# deque(['John', 'Michael', 'Terry'])
