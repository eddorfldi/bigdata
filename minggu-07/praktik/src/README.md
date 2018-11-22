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
>>> type(df['A'])
<class 'pandas.core.series.Series'>
>>> df - df['A']
            2000-01-01 00:00:00  2000-01-02 00:00:00  2000-01-03 00:00:00  2000-01-04 00:00:00 ...  2000-01-08 00:00:00   A   B   C
2000-01-01                  NaN                  NaN                  NaN                  NaN ...                  NaN NaN NaN NaN
2000-01-02                  NaN                  NaN                  NaN                  NaN ...                  NaN NaN NaN NaN
2000-01-03                  NaN                  NaN                  NaN                  NaN ...                  NaN NaN NaN NaN
2000-01-04                  NaN                  NaN                  NaN                  NaN ...                  NaN NaN NaN NaN
2000-01-05                  NaN                  NaN                  NaN                  NaN ...                  NaN NaN NaN NaN
2000-01-06                  NaN                  NaN                  NaN                  NaN ...                  NaN NaN NaN NaN
2000-01-07                  NaN                  NaN                  NaN                  NaN ...                  NaN NaN NaN NaN
2000-01-08                  NaN                  NaN                  NaN                  NaN ...                  NaN NaN NaN NaN

[8 rows x 11 columns]

# Transposing
>>> df[:5].T
   2000-01-01  2000-01-02  2000-01-03  2000-01-04  2000-01-05
A   -1.527096    1.069324   -0.552742    1.568252   -0.611872
B    0.744563    0.706189   -0.557935    0.713562   -0.628124
C   -0.512684   -2.445008   -0.620193   -1.590126   -0.372767

# DataFrame interoperability with NumPy functions
>>> np.exp(df)
                   A         B         C
2000-01-01  0.217165  2.105522  0.598886
2000-01-02  2.913410  2.026255  0.086725
2000-01-03  0.575370  0.572390  0.537841
2000-01-04  4.798255  2.041249  0.203900
2000-01-05  0.542335  0.533592  0.688826
2000-01-06  1.037482  3.084910  3.616295
2000-01-07  0.384891  4.552109  1.252450
2000-01-08  4.619176  1.323539  0.298348
>>> np.asarray(df)
array([[-1.52709585,  0.74456337, -0.51268371],
       [ 1.06932436,  0.70618938, -2.44500784],
       [-0.55274247, -0.55793459, -0.62019263],
       [ 1.56825225,  0.71356177, -1.590126  ],
       [-0.61187165, -0.62812362, -0.37276703],
       [ 0.0367969 ,  1.12652255,  1.28544993],
       [-0.95479491,  1.51559057,  0.22510201],
       [ 1.53021623,  0.28030939, -1.20949524]])
       
# Console display
>>> pd.set_option('display.width', 40)
>>> pd.DataFrame(np.random.randn(3, 12))
         0         1         2         3         4         5         6         7         8         9         10        11
0  0.941595 -0.281574  0.402722  1.052652  1.577692  1.770626 -1.788340 -0.951465  1.099783  1.394173  0.742940  0.418658
1  0.261975 -0.737266  0.232209  2.055588  1.678714 -1.293341  0.379221  0.139958  0.355462  0.894095  0.503120  0.945206
2  1.178554 -0.125867 -1.683584 -0.068520 -2.509512 -0.664375  0.577029  0.634695 -0.596757  1.026476 -0.764995 -0.037509

# DataFrame column attribute access and IPython completion
>>> df = pd.DataFrame({'foo1' : np.random.randn(5),
...     'foo2' : np.random.randn(5)})
>>> df
       foo1      foo2
0 -0.085709  0.567698
1  1.428085  0.082535
2 -0.439620  0.822733
3  0.010360  0.362885
4  1.686646  0.529790
>>>
>>> df.foo1
0   -0.085709
1    1.428085
2   -0.439620
3    0.010360
4    1.686646
Name: foo1, dtype: float64

# From 3D ndarray with optional axis labels
>>> wp = pd.Panel(np.random.randn(2, 5, 4), items=['Item1', 'Item2'],
...     major_axis=pd.date_range('1/1/2000', periods=5),
...     minor_axis=['A', 'B', 'C', 'D'])
>>> wp
<class 'pandas.core.panel.Panel'>
Dimensions: 2 (items) x 5 (major_axis) x 4 (minor_axis)
Items axis: Item1 to Item2
Major_axis axis: 2000-01-01 00:00:00 to 2000-01-05 00:00:00
Minor_axis axis: A to D

# From dict of DataFrame objects
>>> data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
...     'Item2' : pd.DataFrame(np.random.randn(4, 2))}
>>> pd.Panel(data)
<class 'pandas.core.panel.Panel'>
Dimensions: 2 (items) x 4 (major_axis) x 3 (minor_axis)
Items axis: Item1 to Item2
Major_axis axis: 0 to 3
Minor_axis axis: 0 to 2

# From DataFrame using to_panel method
