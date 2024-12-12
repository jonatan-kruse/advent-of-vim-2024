from functools import cache

@cache
def numstones(s, i):
    if i == 0: return 1
    if s == 0:
        return numstones(1, i - 1)
    elif len(str(s)) % 2 == 0:
        s1 = int(str(s)[:len(str(s)) // 2])
        s2 = int(str(s)[len(str(s)) // 2:])
        return numstones(s1, i - 1) + numstones(s2, i - 1)
    else:
        return numstones(s * 2024, i - 1)
    
stones = [int(s) for s in open(0).read().split()]
print(sum([numstones(s, 1000) for s in stones]))

