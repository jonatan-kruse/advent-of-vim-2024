import sys

l1, l2 = map(list, zip(*[line.split() for line in sys.stdin]))
print(sum([int(n) * l2.count(n) for n in l1]))
