#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    stones = f.read().split()

print(stones)

cache = {}

def evolve_count(stone, generations):
    if generations == 0:
        return 1

    if not stone in cache:
        cache[stone] = {}
    
    if not generations in cache[stone]:
        if stone == '0':
            cache[stone][generations] = evolve_count(str(1), generations-1)
        elif len(stone) % 2 == 0:
            mid = len(stone)//2
            left = stone[:mid]
            right = str(int(stone[mid:]))
            cache[stone][generations] = evolve_count(left, generations-1) + evolve_count(right, generations-1)
        else:
            cache[stone][generations] = evolve_count(str(int(stone)*2024), generations-1)
    return cache[stone][generations]


print(sum([evolve_count(stone, 75) for stone in stones]))