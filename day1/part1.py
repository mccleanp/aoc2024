#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    lines = map(lambda line: tuple(map(int, line.split())), f.readlines())
    left, right = map(sorted, zip(*lines))

sum = 0;
for l, r in zip(left, right):
    dist = abs(l - r)
    sum += dist

print(sum)