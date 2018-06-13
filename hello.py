#! /anaconda2/bin/python
import sys
# sys.path.insert(0, '/home/akshaya/technical/tinkerbox/python-trials/foo')
import foo.libA as libA
import bar.libB as libB
import bar.barchild.libBB as libBB
import numpy 
from helloHelper import OutHello



print('Hello, world!')

A = numpy.array([1,2,3])
print(A)
B = OutHello()
C = libA.PrintText('Kookaburra')

art   = libB.Arithmatik()
D     = art.AddConst(A[1])
print(D)

b   = libBB.Dividing()
I   = b.DivConst(2*3.14)
print(I)