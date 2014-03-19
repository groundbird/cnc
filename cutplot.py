#!/usr/bin/env python

from sys import stdin, stderr, argv
from math import sqrt
from getopt import getopt


try:
    gopt = None
    optlist, args = getopt(argv[1:], 'g:')
    for opt in optlist:
        if   opt[0] == '-g': gopt = float(opt[1])
        else: raise
        pass
except:
    print >>stderr, """
Usage: cutplot.py (-g [1 or 2])
"""
    exit(1)
    pass


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


x, y, z = 0., 0., 0. # mm

for line in stdin:
    comm = parser(line)
    if comm == None: continue
    if "G" in comm: 
        if comm["G"] == 0.:
            G = 0
        elif comm["G"] == 1.:
            G = 1
        else: continue
    if "X" in comm: x = comm["X"]
    if "Y" in comm: y = comm["Y"]
    if "Z" in comm: z = comm["Z"]

    if gopt != None:
        if gopt != G: print
        pass
    print x, y, z
    pass
