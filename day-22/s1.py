count = 0
for line in open(0):
    s = int(line)
    for i in range(2000):
        m = s * 64
        s ^= m
        s %= 16777216
        m = s // 32
        s ^= m
        s %= 16777216
        m = s * 2048
        s ^= m
        s %= 16777216
    count += s
print(count)
