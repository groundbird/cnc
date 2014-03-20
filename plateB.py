#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boring
import os
import sys
import datetime as dt
from numpy import matrix, sin, cos, pi, dot, array

def rotation(x, th):
    rot = matrix(((cos(th), sin(th)), (-sin(th), cos(th))))
    return dot(x, rot)

fname = 'plateB_%s.nc' % dt.datetime.now().strftime('%Y%m%d%H%M')

x0 = array([[-16.25, -40.],
           [-16.25, -50.],
           [0.,     -50.],
           [0.,     -40.],
           [16.25,  -40.],
           [16.25,  -50.]])

x    = x0.tolist()
x120 = rotation(x0, 2*pi/3).tolist()
x240 = rotation(x0, 4*pi/3).tolist()
x.extend(x120)
x.extend(x240)
list = []
for x_i in x:
    x_i.extend([5, 3.5])
    list.append(x_i)
list.extend([[0, 0, 5, 144]]) # 大円

sys.stdout = open(fname, 'w')
boring.init(fname)
for l in list: boring.boring(*l)
boring.final()
sys.stdout.close()
sys.stdout = sys.__stdout__
print open(fname, 'r').read()
os.system('mv %s ~/Dropbox/hikaru/kitmill' % fname)
