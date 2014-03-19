#!/usr/bin/env python

from sys import argv, stderr, stdin

## setting
r = 2.       # mill: phi = 2r = 4mm
m = 0.99995  # margin = 1mm
zstep = 0.05 # step = 0.05mm
zceil = 2.0  # z = 2.0 when high-speed moving

## read argument
command_list = []
try:
    if len(argv) == 2:
        if argv[1] == "-i":
            command_lines = stdin
        else:
            command_lines = open(argv[1])
            pass
    elif len(argv) == 6:
        command_lines = ["%s %s %s %s %s\n" % tuple(argv[1:6])]
    else: raise
    for line in command_lines:
        if line[0] == '#': continue
        wds = line.split()
        if len(wds) != 5: raise
        x0 = float(wds[0])
        x1 = float(wds[1])
        y0 = float(wds[2])
        y1 = float(wds[3])
        depth = float(wds[4])
        nakanuki = False
        if x1 < x0 + 2 * r + m:
            print >>stderr, line,
            print >>stderr, "x1 - x0 is too small."
            raise
        if y1 < y0 + 2 * r + m:
            print >>stderr, line,
            print >>stderr, "y1 - y0 is too small."
            raise
        if x1 - x0 > 4 * r and y1 - y0 > 4 * r: nakanuki = True
        command_list.append([x0, x1, y0, y1, depth, nakanuki])
        pass
    if len(command_list) == 0: raise
except:
    print >>stderr, """
Usage: square.py [x0] [x1] [y0] [y1] [depth]
         or
       square.py [filename]
         or
       square.py -i < [filename]

         == in file ==
         [x0] [x1] [y0] [y1] [depth]
         [x0] [x1] [y0] [y1] [depth]
         ...

  Cutting Area: xrange = [ x0 : x1 ]
                yrange = [ y0 : y1 ]
                 (Corners are not cut.)"""
    exit(1)
    pass


## initialize
print """%
(FILENAME: square.nc)
(mili-meter, cut-mode, xy-plane)
G21G64G17
(TOOL/MILL,4.0000,0,8.0000,0.0)
M6 T5"""


## loop
for x0, x1, y0, y1, depth, nakanuki in command_list:
    z = 0.
    print "G0Z%.4f" % zceil
    print "(set:  %.4f  %.4f  %.4f  %.4f  %.4f)" % (x0, x1, y0, y1, depth)
    print "G0X%.4fY%.4fZ%.4f" % (x0+r, y0+r, zceil)
    while z < depth:
        z += zstep
        if z > depth: z = depth
        print "(down)"
        print "G1Z-%.4fF60.0"  % z
        print "G1Z-%.4fF250.0" % z

        print "(outer)"
        print "X%.4f" % (x1-r)
        print "Y%.4f" % (y1-r)
        print "X%.4f" % (x0+r)
        print "Y%.4f" % (y0+r)

        if not nakanuki: continue

        print "(inner)"
        print "X%.4fY%.4f" % (x0+r+m, y0+r+m)
        print "Y%.4f" % (y1-r-m)
        print "X%.4f" % (x1-r-m)
        print "Y%.4f" % (y0+r+m)
        print "X%.4f" % (x0+r+m)
        print "X%.4fY%.4f" % (x0+r, y0+r)

        pass
    pass

## finalize
print "(finish: up, move-zero, mill-stop, end)"
print "G0Z%.4f" % zceil
print "G0X%.4fY%.4fZ%.4f" % (0., 0., zceil)
print """M5
M30
%"""
