#!/usr/bin/env python3

import sys


with open(sys.argv[1], 'r') as f:
    data = list(map(lambda x: x.strip(), f.readlines()))


def find_needle(x, y, dx, dy, needle):
    for letter in needle:
        if x + dx < 0 or x + dx >= len(row):
            return False
        if y + dy < 0 or y + dy >= len(data):
            continue
        if data[y + dy][x + dx] != letter:
            return False
        x += dx
        y += dy
    return True


needle = "XMAS"

found = 0

letter = needle[0]
for y, row in enumerate(data):
    for x, cell in enumerate(row):
        if cell == letter:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    if find_needle(x, y, dx, dy, needle[1:]):
                        found += 1

print(found)