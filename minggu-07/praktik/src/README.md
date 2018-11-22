# Intro to Data Structures

> `>>> import numpy as np` <br>
`>>> import pandas as pd`<br>

# Series with ndarray
>>> s = pd.Series(np.random.randn(5), index=['a','b','c','d','e'])
>>> s
a    1.120249
b   -0.145511
c    0.730411
d    0.161393
e   -0.795025
dtype: float64

# Series with dict
>>> d = {'b' : 1, 'a' : 0, 'c' : 2}
>>> pd.Series(d)
b    1
a    0
c    2
dtype: int64

>>> d = {'a' : 0., 'b' : 1., 'c' :2.}
>>> pd.Series(d)
a    0.0
b    1.0
c    2.0
dtype: float64
>>> pd.Series(d, index=['b','c','d','a'])
b    1.0
c    2.0
d    NaN
a    0.0
dtype: float64


# Series with scalar value
>>> pd.Series(5., index=['a','b','c','d','e'])
a    5.0
b    5.0
c    5.0
d    5.0
e    5.0
dtype: float64

# Series is ndarray-like
>>> s[0]
1.120249026777211
>>> s[:3]
a    1.120249
b   -0.145511
c    0.730411
dtype: float64
>>> s[s > s.median()]
a    1.120249
c    0.730411
dtype: float64

# Series is dict-like
>>> s['a']
1.120249026777211
>>> s['e']=12.
>>> s
a     1.120249
b    -0.145511
c     0.730411
d     0.161393
e    12.000000
dtype: float64

# Vectorized operations and label alignment with Series
>>> s + s
a     2.240498
b    -0.291023
c     1.460823
d     0.322785
e    24.000000
dtype: float64
>>> s * 2
a     2.240498
b    -0.291023
c     1.460823
d     0.322785
e    24.000000
dtype: float64
>>> s[1:]+s[:-1]
a         NaN
b   -0.291023
c    1.460823
d    0.322785
e         NaN
dtype: float64

# Name attribute
>>> s = pd.Series(np.random.randn(5), name='something')
>>> s
0   -0.034886
1   -0.314753
2    0.704430
3   -1.113588
4   -1.670781
Name: something, dtype: float64
>>> s.name
'something'

# From dict of Series or dict
>>> d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
...     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
>>> df = pd.DataFrame(d)
>>> df
   one  two
a  1.0  1.0
b  2.0  2.0
c  3.0  3.0
d  NaN  4.0
>>> pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])
   two three
d  4.0   NaN
b  2.0   NaN
a  1.0   NaN

# From dict of ndarrays / lists
>>> d = {'one' : [1., 2., 3., 4.],
...     'two' : [4., 3., 2., 1.]}
>>> pd.DataFrame(d)
   one  two
0  1.0  4.0
1  2.0  3.0
2  3.0  2.0
3  4.0  1.0
>>> pd.DataFrame(d, index=['a','b','c','d'])
   one  two
a  1.0  4.0
b  2.0  3.0
c  3.0  2.0
d  4.0  1.0

# From structured or record array
>>> data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])
>>> data[:] = [(1,2.,'Hello'), (2,3.,"World")]
>>> pd.DataFrame(data)
   A    B         C
0  1  2.0  b'Hello'
1  2  3.0  b'World'
>>> pd.DataFrame(data, index=['first', 'second'])
        A    B         C
first   1  2.0  b'Hello'
second  2  3.0  b'World'
>>> pd.DataFrame(data, columns=['C', 'A', 'B'])
          C  A    B
0  b'Hello'  1  2.0
1  b'World'  2  3.0

# From a list of dicts
>>> data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
>>> pd.DataFrame(data2)
   a   b     c
0  1   2   NaN
1  5  10  20.0
>>> pd.DataFrame(data2, index=['first', 'second'])
        a   b     c
first   1   2   NaN
second  5  10  20.0
>>> pd.DataFrame(data2, columns=['a', 'b'])
   a   b
0  1   2
1  5  10

# From a dict of tuples
>>> pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
...             ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
...             ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
...             ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
...             ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})
       a              b
       b    a    c    a     b
A B  1.0  4.0  5.0  8.0  10.0
  C  2.0  3.0  6.0  7.0   NaN
  D  NaN  NaN  NaN  NaN   9.0
  
# Alternate Constructors
>>> pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]),
...                             orient='index', columns=['one', 'two', 'three'])
   one  two  three
A    1    2      3
B    4    5      6

>>> data
array([(1, 2., b'Hello'), (2, 3., b'World')],
      dtype=[('A', '<i4'), ('B', '<f4'), ('C', 'S10')])
>>> pd.DataFrame.from_records(data, index='C')
          A    B
C
b'Hello'  1  2.0
b'World'  2  3.0

# Column selection, addition, deletion
>>> df.insert(1, 'bar', df['one'])
>>> df
   one  bar  two
a  1.0  1.0  1.0
b  2.0  2.0  2.0
c  3.0  3.0  3.0
d  NaN  NaN  4.0

# Data alignment and arithmetic
>>> df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
>>> df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])
>>>
>>> df + df2
          A         B         C   D
0  1.468236  1.113292 -2.653881 NaN
1  0.028142 -0.044725 -2.418750 NaN
2  0.759206 -1.132532 -2.488735 NaN
3 -1.486699 -0.518653 -0.093701 NaN
4 -0.510985  0.694744  3.146783 NaN
5  1.231910  0.945245 -0.676860 NaN
6 -0.654820  0.256159  0.072677 NaN
7       NaN       NaN       NaN NaN
8       NaN       NaN       NaN NaN
9       NaN       NaN       NaN NaN


