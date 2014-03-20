#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boring
import os
import sys
import datetime as dt

fname = 'plateA_%s.nc' % dt.datetime.now().strftime('%Y%m%d%H%M')
list = [[-5,     -61.25, 5, 3.5],
        [-5,     -45,    5, 3.5],
        [-5,     -28.75, 5, 3.5],
        [5,      -61.25, 5, 3.5],
        [5,      -45,    5, 3.5],
        [5,      -28.75, 5, 3.5],
        [22.4,   18.71,  5, 3.5],
        [36.47,  26.83,  5, 3.5],
        [50.54,  34.96,  5, 3.5],
        [27.4,   10.04,  5, 3.5],
        [41.47,  18.17,  5, 3.5],
        [55.54,  26.29,  5, 3.5],
        [-22.4,  18.71,  5, 3.5],
        [-36.47, 26.83,  5, 3.5],
        [-50.54, 34.96,  5, 3.5],
        [-27.4,  10.04,  5, 3.5],
        [-41.47, 18.17,  5, 3.5],
        [-55.54, 26.29,  5, 3.5],
        [0,      0,      5, 144]] # 大円
sys.stdout = open(fname, 'w')
boring.init(fname)
for l in list: boring.boring(*l)
boring.final()
sys.stdout.close()
sys.stdout = sys.__stdout__
print open(fname, 'r').read()
os.system('mv %s ~/Dropbox/hikaru/kitmill' % fname)
