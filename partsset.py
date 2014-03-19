#!/usr/bin/env python

from kitmill import *
from numpy import pi, sqrt

initialize("partsset.py")

## waku1
print "(waku1)"
square_cut_line(-3, 73, -3, 43, 0, -15, 1)

## left-area
## z: 0 -> -10
#wait() #34.9min
print "(z: 0 -> -10)"
square_cut(0, 3, 0, 40, 0, -10)
square_cut(6, 8, 0, 40, 0, -10)

square_cut(10, 13, 0, 13, 0, -10)
square_cut(16, 19, 0, 13, 0, -10)
square_cut(22, 23, 0, 13, 0, -10)

square_cut(10, 17.5, 12, 13, 0, -10)

square_cut(19.5, 23, 12, 28, 0, -10)

## z: -10 -> -15
#wait() #49.4min
print "(z: -10 -> -15)"
square_cut(0, 3, 15, 40, -10, -15)
square_cut(6, 8, 15, 40, -10, -15)

square_cut(0, 23,  7,  9, -10, -17)
square_cut(0, 23, 11, 13, -10, -17)

square_cut(22, 23, 0, 15, -10, -19.9)

square_cut(19.5, 23, 15, 28, -10, -19.9)

circle_cut(18, 3, 4, 5, pi*0.0, pi*0.5, -10, -17)
circle_cut( 2, 3, 4, 5, pi*0.5, pi*1.0, -10, -17)

circle_cut( 2, 2, 4, 5, pi*1.0, pi*1.5, -10, -19.9)
circle_cut(18, 2, 4, 5, pi*1.5, pi*2.0, -10, -19.9)

square_cut(-3, -2, 0, 17.5, -15, -17)

## z: -15 -> -17
#wait() #68.4min
print "(z: -15 -> -17)"

square_cut(0, 8, 37.5, 40.5, -15, -15)
for z in arange(-15-accuracy, -17-accuracy, -accuracy):
    delta = sqrt(2.**2 - (17.+z)**2) # 0 -> 2
    square_cut(0, 8, 37.5 + delta, 40.5, z, z, z)
    pass
square_cut(0, 8, 39.5, 40.5, -17, -19.9, -16)

#wait() #73.0min
square_cut(0, 8, 14.5, 17.5, -15, -15)
for z in arange(-15-accuracy, -17-accuracy, -accuracy):
    delta = sqrt(2.**2 - (17.+z)**2) # 0 -> 2
    square_cut(0, 8, 14.5, 17.5 - delta, z, z, z)
    pass
square_cut(0, 8, 14.5, 15.5, -17, -19.9, -16)

## z: -17 -> -19
#wait() #77.7min
print "(z: -17 -> -19)"

move(-3, 10)
for z in arange(-17., -19, -accuracy):
    delta = sqrt(2.**2 - (19.+z)**2) # 0 -> 2
    phi = angle(-(2+delta) + sqrt(4.**2 - (2.+delta)**2)*1j)
    down(z)
    line(-3, 3)
    circle_line(2, 3, 4, pi, phi)
    line(-delta, 10)
    line(-3, 10)
    pass

#wait() #81.6min
move(23, 10)
for z in arange(-17., -19, -accuracy):
    delta = sqrt(2.**2 - (19.+z)**2) # 0 -> 2
    phi = angle((2+delta) + sqrt(4.**2 - (2.+delta)**2)*1j)
    down(z)
    line(20+delta, 10)
    circle_line(18, 3, 4, phi, 0)
    line(23, 3)
    line(23, 10)
    pass

## z: -17 -> -20
#wait() #85.5min
print "(z: -17 -> -20)"
square_cut(0, 20, 12, 13, -17, -19.9)

## z: 0 -> -20
#wait() #86.4min
print "(z: 0 -> -20)"
square_cut(23,   40.5, 27, 28, 0, -19.9)
square_cut(37,   40.5, 12, 28, 0, -19.9)
square_cut(40.5, 58,   12, 13, 0, -19.9)
square_cut(57,   58,   13, 40, 0, -19.9)
square_cut(58,   70,   27, 28, 0, -19.9)

## hekomi
print "(hekomi)"
square_cut(24.5, 25.5, -0.5,  0.5, 0, -19.9)
square_cut(69.5, 70.5, -0.5,  0.5, 0, -19.9)
square_cut(69.5, 70.5, 24.5, 25.5, 0, -19.9)
square_cut(24.5, 25.5, 24.5, 25.5, 0, -19.9)
square_cut(52, 55, 14.5, 15.5, 0, -19.9)
square_cut(52, 55, 39.5, 40.5, 0, -19.9)

## waku2
#wait() #104.3min
square_cut_line(-3, 73, -3, 43, -15, -19.9, 1)

finalize() #114.5min
