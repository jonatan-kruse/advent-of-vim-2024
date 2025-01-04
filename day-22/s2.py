monkeys = []
for line in open(0):
    s = int(line)
    monkey = []
    stp = {}
    for i in range(2000):
        ls = s
        m = s * 64
        s ^= m
        s %= 16777216
        m = s // 32
        s ^= m
        s %= 16777216
        m = s * 2048
        s ^= m
        s %= 16777216
        old = int(str(ls)[-1])
        new = int(str(s)[-1])
        monkey.append((new, new - old))
    for i in range(2000 - 4):
        _, d1 = monkey[i]
        _, d2 = monkey[i + 1]
        _, d3 = monkey[i + 2]
        p, d4 = monkey[i + 3]
        if (d1, d2, d3, d4) in stp: continue
        stp[d1, d2, d3, d4] = p
    monkeys.append(stp)
opt = 0
seqs = {key for d in monkeys for key in d}
for d1, d2, d3, d4 in seqs:
    count = 0
    for monkey in monkeys:
        count += monkey.get((d1, d2, d3, d4), 0)
    opt = max(count, opt)
print(opt)
