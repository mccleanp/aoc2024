#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    stones = f.read().split()

print(stones)

def evolve(stones):
    new_stones = []
    for stone in stones:
        if stone == '0':
            new_stones.append('1')
        elif len(stone) % 2 == 0:
            new_stones.append(stone[:len(stone)//2])
            new_stones.append(str(int(stone[len(stone)//2:])))
        else:
            new_stones.append(str(int(stone)*2024))
    return new_stones

for i in range(25):
    stones = evolve(stones)

print(len(stones))