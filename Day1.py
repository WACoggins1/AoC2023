day1 = open("AdventDay1_2023.txt").read().splitlines()

numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6',
            'seven': '7', 'eight': '8', 'nine': '9'}

def append(line, d, k ,v):
    if k in line:
        d.append((line.find(k), v))
        if line.count(k) > 1:
            d.append((line.rfind(k), v))

num = []
num2 = []

for line in day1:
    d = []
    d2 = []
    for k, v in numbers.items():
        append(line, d, v, v)
        append(line, d2, k, v)

    if d:
        num.append(int(min(d)[1] + max(d)[1]))
    if d or d2:
        num2.append(int(min(d + d2)[1] + max(d + d2)[1]))

print(day1)

print(num)
print(num2)
print(sum(num), sum(num2))
