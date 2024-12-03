#!/usr/bin/env python3

import sys
import re

with open(sys.argv[1], 'r') as f:
    line = f.read()

matches = re.findall(r"((mul)|(do)|(don't))\(((\d+),(\d+))?\)", line)

sum = 0
enabled = True
for ins in matches:
    opcode = ins[0]
    arg1 = ins[5]
    arg2 = ins[6]
    if opcode == "don't":
        enabled = False
    if opcode == "do":
        enabled = True
    if opcode == "mul" and enabled:
        sum += int(arg1) * int(arg2)

print(sum)