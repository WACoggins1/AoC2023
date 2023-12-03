import itertools
import math
import re
from collections import defaultdict

with open("Day3.txt") as f:
    ls = f.read().strip().split('\n')

box = list(itertools.product((-1, 0, 1), (-1, 0, 1)))
board = {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[0]))} #parsed as array

patterns = {x for x in board if board[x] != "." and not board[x].isdigit()}

partSum = 0
partSymbol = defaultdict(list)

#update counters and check for symbols adjacent to each entry
for i,l in enumerate(ls):
    for match in re.finditer(r"\d+", l):
        n = int(match.group(0))
        boundary = {
            (i + di, j + dj)
            for di, dj in box
            for j in range(match.start(), match.end())
        }

        if patterns & boundary:
            partSum += n

        for symbol in patterns & boundary:
            partSymbol[symbol].append(n)
#Part 1
print(partSum)

#Part 2
print(sum(math.prod(v) for v in partSymbol.values() if len(v) == 2))

