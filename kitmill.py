#!/usr/bin/env python

from numpy import arange, angle
from math import cos, sin

accuracy = 0.05 #mm
zceil = 2.  #mm
zstep = 0.1 #mm
#zstep = 1.  #mm
xyspeed = 200. #mm/min
#xyspeed = 250. #mm/min
zspeed =   60. #mm/min

def move(x, y, _zceil = zceil):
    print "G0Z%.4f" % _zceil
    print "G0X%.4fY%.4fZ%.4f" % (x, y, _zceil)
    pass

def wait(): print "M6 T5"

def initialize(name):
    print "%"
    print "(SCRIPT NAME: %s)" % name
    print "(mili-meter, cut-mode, xy-plane)"
    print "G21G64G17"
    print "(TOOL/MILL,4.0000,0,8.0000,0.0)"
    print "M6 T5"
    pass

def finalize():
    print "(finish: up, move-zero, mill-stop, end)"
    move(0, 0)
    print "M5"
    print "M30"
    print "%"
    pass

def down(z):
    print "G1Z%.4fF%.1f" % (z,  zspeed)
    print "G1Z%.4fF%.1f" % (z, xyspeed)

def line(x, y):
    print "X%.4fY%.4f" % (x, y)
    pass

def circle_line(x, y, r, theta1, theta2): ## x,y,r[mm], theta[rad]
    print "(circle_line start)"
    delta_theta = angle(float(r) + accuracy*1j)
    if theta2 < theta1: delta_theta *= -1
    thetalist = arange(theta1, theta2, delta_theta).tolist()
    thetalist.append(theta2)
    for theta in thetalist:
        line(x + r * cos(theta), y + r * sin(theta))
        pass
    print "(circle_line end)"
    pass

def make_span(a, b):
    return min([a, b]), max([a, b])

def make_zlist(z1, z2):
    ret = arange(z1-zstep, z2, -zstep).tolist()
    ret.append(z2)
    return ret

def square_cut(_x1, _x2, _y1, _y2, _z1, _z2, _zceil = zceil):
    print "(square_cut start)"
    x1, x2 = make_span(_x1, _x2)
    y1, y2 = make_span(_y1, _y2)
    z2, z1 = make_span(_z1, _z2)
    move(x1, y1, _zceil)
    for z in make_zlist(z1, z2):
        down(z)
        line(x2, y1)
        line(x2, y2)
        line(x1, y2)
        line(x1, y1)
    print "(square_cut end)"
    pass

def square_cut_line(_x1, _x2, _y1, _y2, _z1, _z2, width, _zceil = zceil):
    print "(square_cut_line start)"
    x1, x2 = make_span(_x1, _x2)
    y1, y2 = make_span(_y1, _y2)
    z2, z1 = make_span(_z1, _z2)
    move(x1, y1, _zceil)
    for z in make_zlist(z1, z2):
        down(z)
        line(x2, y1)
        line(x2, y2)
        line(x1, y2)
        line(x1, y1)
        line(x1 + width, y1 + width)
        line(x1 + width, y2 - width)
        line(x2 - width, y2 - width)
        line(x2 - width, y1 + width)
        line(x1 + width, y1 + width)
        line(x1, y1)
        pass
    print "(square_cut_line end)"
    pass

def circle_cut(x, y, _r1, _r2, _theta1, _theta2, _z1, _z2, _zceil = zceil):
    print "(circle_cut start)"
    r1, r2 = make_span(_r1, _r2)
    theta1, theta2 = make_span(_theta1, _theta2)
    z2, z1 = make_span(_z1, _z2)
    def make_pos(r, theta): return x+r*cos(theta), y+r*sin(theta)
    x0, y0 = make_pos(r1, theta1)
    move(x0, y0, _zceil)
    for z in make_zlist(z1, z2):
        down(z)
        line(*make_pos(r2, theta1))
        circle_line(x, y, r2, theta1, theta2)
        line(*make_pos(r1, theta2))
        circle_line(x, y, r1, theta2, theta1)
        pass
    print "(circle_cut end)"
    pass
