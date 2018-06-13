#! /anaconda2/bin/python
import sys
sys.path.insert(0, '/home/akshaya/technical/tinkerbox/python-trials/')
# from helloHelper import OutHello

import foo.libA as libA
import libB
import barchild.libBB as libBB
# import bar.libB as libB
import numpy 


G   = libA.PrintText('Tarqib')

# a   = libB.Arithmatik()
a   = libB.Arithmatik()
H   = a.AddConst(5)
print(H)

b   = libBB.Dividing()
I   = b.DivConst(2*3.14)
print(I)