#!/usr/bin/env python3

import sys
import re

with open(sys.argv[1], 'r') as f:
    line = f.read()

matches = re.findall(r'mul\((\d+),(\d+)\)', line)

result = sum(map(lambda x: int(x[0]) * int(x[1]), matches))

print(result)