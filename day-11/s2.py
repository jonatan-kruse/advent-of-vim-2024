stones = [int(s) for s in open(0).read().split()]
cache = {}

def numstones(s, i, c):
    if i == 0: return 1
    if (s, i) in c: return c[s,i]
    if s == 0:
        nv = numstones(1, i - 1, c)
        c[s,i] = nv
        return nv
    elif len(str(s)) % 2 == 0:
        s1 = int(str(s)[:len(str(s)) // 2])
        s2 = int(str(s)[len(str(s)) // 2:])
        nv1 = numstones(s1, i - 1, c)
        nv2 = numstones(s2, i - 1, c)
        c[s,i] = nv1 + nv2
        return nv1 + nv2
    else:
        nv = numstones(s * 2024, i - 1, c)
        c[s,i] = nv
        return nv
    
print(sum([numstones(s, 75, cache) for s in stones]))

