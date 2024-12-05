#!/usr/bin/env python3

import sys

rules = []
pages = []

with open(sys.argv[1], 'r') as f:
    while line := f.readline().strip():
        rules.append(tuple(map(int, line.split('|'))))
    while line := f.readline().strip():
        pages.append(list(map(int, line.split(','))))

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
        

invalid_pages = filter(lambda x: not is_valid(x), pages)


def swap(page, i, j):
    temp = page[i]
    page[i] = page[j]
    page[j] = temp


def fix_page(page):
    for l,r in rules:
        try:
            li = page.index(l)
            ri = page.index(r)
            if li > ri:
                swap(page, li, ri)
                return fix_page(page)
        except ValueError:
            # skip this rule
            pass
    return page

fixed_pages = [fix_page(page) for page in invalid_pages]

print(sum([page[len(page) // 2] for page in fixed_pages]))
