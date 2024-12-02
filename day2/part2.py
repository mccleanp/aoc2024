#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    lines = list(map(lambda line: list(map(int, line.split())), f.readlines()))

def is_safe(report):
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    direction = differences[0] > 0
    for diff in differences:
        if diff == 0:
            return False
        if (diff > 0) is not direction:
            return False
        if abs(diff) > 3:
            return False
    return True

safe = 0

for report in lines:
    if is_safe(report):
        safe += 1
    else:
        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            if is_safe(modified_report):
                safe += 1
                break

print(safe) 