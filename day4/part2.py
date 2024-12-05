#!/usr/bin/env python3

import sys


with open(sys.argv[1], 'r') as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

found = 0

for y in range(1, len(data) - 1):
    for x in range(1, len(data[y]) - 1):
        if data[y][x] == 'A':
            if ((data[y-1][x-1] == 'M' and data[y+1][x+1] == 'S') or (data[y-1][x-1] == 'S' and data[y+1][x+1] == 'M')) and ((data[y+1][x-1] == 'M' and data[y-1][x+1] == 'S') or (data[y+1][x-1] == 'S' and data[y-1][x+1] == 'M')):
                found += 1

print(found)