#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np

def boring(x, y, z, r):
    """
    x, y: 穴の中心
    z:    穴の深さ
    r:    穴の直径
    """
    n = 32                # 頂点の数
    f = 200.              # 切削速度
    f_z = 60.             # 下降速度
    step = 0.05           # 1回の切込み量
    b_phi = 2.            # 刃先
    r_eff = r/2 - b_phi/2 # 実効半径
    print 'G0Z2.0000'
    print 'G0X%.4fY%.4f' % (x+r_eff, y)
    for dz in -np.arange(step, z+step, step):
        print '(down)'
        print 'G1Z%.4fF%.4f' % (dz, f_z)
        print 'G1Z%.4fF%.4f' % (dz, f)
        for k in range(n+1):
            x_k = x + r_eff*np.cos(2*np.pi*k/n)
            y_k = y + r_eff*np.sin(2*np.pi*k/n)
            print 'X%.4fY%.4f' % (x_k, y_k)

def init(fname):
    print '%'
    print '(FILENAME: %s)' % fname
    print '(mili-meter, cut-mode, xy-plane)'
    print 'G21G64G17'
    print 'M6 T5'

def final():
    print '(finish: up, move-zero, mill-stop, end)'
    print 'G0Z2.0000'
    print 'M5'
    print 'M30'
    print '%'
        
if __name__ == '__main__':
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    z = float(sys.argv[3])
    r = float(sys.argv[4])
    fname = 'boring.nc'
    sys.stdout = open(fname, 'w')
    init(fname)
    boring(x, y, z, r)
    final()
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print open(fname, 'r').read()
