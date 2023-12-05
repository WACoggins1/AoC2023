import re

"""
the input looks kinda like this: 
Card 1: 41 72 83 | 72 41 17
First half is winning numbers, second half is your numbers
first matching pair sumWin = 1. For each additional pair, sumWin += 2*(sumWin)

Card 1 has two matching numbers, so you win one copy of each of the next 2 cards. (generalized up to n)
"""

def score(line):
    m = re.match(r"Card\s+(\d+):\s+(.*?)\s\|\s+(.*?)$", line)
    winners = set(int(n) for n in m.group(2).strip().split())
    nums = set(int(n) for n in m.group(3).strip().split())
    return winners.intersection(nums)

p1 = 0
lines = open('Day4.txt').read().strip().splitlines()
p2 = [1]*len(lines)

for n, line in enumerate(lines):
    matches = score(line)
    p1 += int(2**(len(matches) - 1))

    for i in range(len(matches)):
        p2[n + i + 1] += p2[n]

print(f"Part 1: {p1}")
print(f"Part 2: {sum(p2)}")
