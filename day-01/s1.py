import sys

l1, l2 = map(list, zip(*[line.split() for line in sys.stdin]))
l1.sort()
l2.sort()
print(sum([abs(int(a) - int(b)) for [a, b] in zip(l1, l2)]))
