#!/usr/bin/env python

from sys import argv, stderr

## setting
w = 1.       # cut_width = 1mm
zstep = 0.05 # step = 0.05mm
#zstep = 1. # step = 0.05mm
zceil = 2.0  # z = 2.0 when high-speed moving

## read argument
try:
    if len(argv) != 6: raise
    x0 = float(argv[1])
    x1 = float(argv[2])
    y0 = float(argv[3])
    y1 = float(argv[4])
    depth = float(argv[5])
    if x1 < x0:
        print >>stderr, "Error: x1 < x0"
        raise
    if y1 < y0:
        print >>stderr, "Error: y1 < y0"
        raise
except:
    print >>stderr, """Usage: plane.py [x0] [x1] [y0] [y1] [depth]
  Cutting Area: xrange = [ x0 - r : x1 + r ] or more
                yrange = [ y0 - r : y1 + r ] or more
                 (r = radius_of_mill)"""
    exit(1)
    pass

## initialize
xw = x1 - x0
yw = y1 - y0
c = min([xw, yw]) / 2
cx0 = x0 + c
cx1 = x1 - c
cy0 = y0 + c
cy1 = y1 - c
z = 0.
print """%
(FILENAME: plane.nc)
(mili-meter, cut-mode, xy-plane)
G21G64G17
(TOOL/MILL,4.0000,0,8.0000,0.0)
M6 T5"""

## loop
while z < depth:
    print "(new plane)"
    print "G0Z%.4f" % (zceil-z)
    print "G0X%.4fY%.4fZ%.4f" % (cx1, cy1, zceil-z)
    z += zstep
    if z > depth: z = depth
    print "(down)"
    print "G1Z%.4fF60.0"  % -z
    print "G1Z%.4fF250.0" % -z
    print "(center)"
    print "X%.4fY%.4f" % (cx0, cy0)

    t = 0
    while t < c:
        print "(new square)"
        t += w
        print "X%.4fY%.4f" % (cx0-t, cy0-t)
        print "X%.4f" % (cx1+t)
        print "Y%.4f" % (cy1+t)
        print "X%.4f" % (cx0-t)
        print "Y%.4f" % (cy0-t)
        pass
    pass

## finalize
print "(finish: up, move-zero, mill-stop, end)"
print "G0Z%.4f" % zceil
print "G0X%.4fY%.4fZ%.4f" % (0., 0., zceil)
print """M5
M30
%"""
