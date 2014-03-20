#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boring
import os
import sys
import datetime as dt

# fname = 'turiguA_ana2_%s.nc' % dt.datetime.now().strftime('%Y%m%d%H%M')
# list = [[20, 10, 3, 2.5],
#         [30, 10, 3, 2.5]]
fname = 'turiguA_ana4_%s.nc' % dt.datetime.now().strftime('%Y%m%d%H%M')
list = [[8.75,   5, 3, 2.5],
        [8.75,  15, 3, 2.5],
        [41.25,  5, 3, 2.5],
        [41.25, 15, 3, 2.5]]
# fname = 'turiguB_ana2_%s.nc' % dt.datetime.now().strftime('%Y%m%d%H%M')
# list = [[17.5, 10, 5, 2.5],
#         [27.5, 10, 5, 2.5]]
# fname = 'turiguB_ana4_%s.nc' % dt.datetime.now().strftime('%Y%m%d%H%M')
# list = [[6, 5, 3, 2.5],
#         [6, 15, 3, 2.5],
#         [39, 5, 3, 2.5],
#         [39, 15, 3, 2.5]]
sys.stdout = open(fname, 'w')
boring.init(fname)
for l in list: boring.boring(*l)
boring.final()
sys.stdout.close()
sys.stdout = sys.__stdout__
print open(fname, 'r').read()
os.system('mv %s ~/Dropbox/hikaru/kitmill' % fname)
