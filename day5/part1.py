#!/usr/bin/env python3

import sys

rules = []
pages = []

with open(sys.argv[1], 'r') as f:
    while line := f.readline().strip():
        rules.append(tuple(map(int, line.split('|'))))
    while line := f.readline().strip():
        pages.append(tuple(map(int, line.split(','))))

print(rules)
print(pages)


def is_valid(page):
    for l,r in rules:
        try:
            li = page.index(l)
            ri = page.index(r)
            if li > ri:
                return False
        except ValueError:
            # skip this rule
            pass
    return True
        

valid_pages = list(filter(is_valid, pages))
print(valid_pages)

print(sum([page[len(page) // 2] for page in valid_pages]))
