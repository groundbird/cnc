#!/usr/bin/env python

from sys import stdin
from math import sqrt


F0 = 15. * 60      # mm/min
F1 = 250.          # mm/min
A = 100. * 60 * 60 # mm/min2

def cost(length, F): ## length [mm], F [mm/min], output [min]
    # ret = sqrt(length / A)
    # if ret * A < F:
    #     ret *= 2
    # else:
    #     rest = length - F * F / A
    #     ret = F / A * 2 + rest / F
    #     pass
    ret = length / F
    #print length, F, ret
    return ret

def parser(_s):
    s = _s.strip()
    if s[0] in ['%', '(', 'M']: return None
    ret = {}
    index = []
    for i, c in enumerate(s):
        if c in ["G", "X", "Y", "Z", "F"]: index.append(i)
        pass
    index.append(None)
    for i1, i2 in zip(index[0:-1], index[1:]):
        ret[s[i1]] = float(s[i1+1:i2])
        pass
    #print s, ret
    return ret


ln = 0
total_time = 0 # min
G = 1
F = F1
x, y, z = 0., 0., 0. # mm

for line in stdin:
    ln += 1
    if line[0:2] == 'M6': print "L%d: %.1f min" % (ln, total_time)
    comm = parser(line)
    if comm == None: continue
    if "G" in comm: 
        if comm["G"] == 0.:
            G = 0
            F = F0
        elif comm["G"] == 1.:
            G = 1
            if "F" in comm: F1 = comm["F"]
            F = F1
        else: continue
    x1, y1, z1 = x, y, z
    if "X" in comm: x1 = comm["X"]
    if "Y" in comm: y1 = comm["Y"]
    if "Z" in comm: z1 = comm["Z"]
    dx = abs(x1-x)
    dy = abs(y1-y)
    dz = abs(z1-z)
    x, y, z = x1, y1, z1
    if G == 0:
        length = max(dx, dy, dz)
    else:
        length = sqrt(dx**2 + dy**2 + dz**2)
        pass

    total_time += cost(length, F)
    pass

print "Total: %.1f min" % total_time
