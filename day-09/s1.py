line = open(0).read().strip()
free = False
fid = 0
disk = []
for c in line:
    if (free):
        disk += [-1] * int(c)
    else:
        disk += [fid] * int(c)
        fid += 1
    free = not free
lastb = len(disk) - 1
for i in range(len(disk)):
    # print((i / len(disk)) * 100)
    if disk[i] != -1: continue
    for j in range(lastb, i, -1):
        if disk[j] == -1: continue
        disk[i] = disk[j]
        disk[j] = -1
        lastb = j
        break
count = 0
for a in range(len(disk)):
    if disk[a] != -1:
        count += a * disk[a]
print(count)
