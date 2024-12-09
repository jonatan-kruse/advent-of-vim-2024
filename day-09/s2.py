line = open(0).read().strip()
free = False
fid = 0
files = []
space = []
location = 0
for c in line:
    if (free):
        space.append((location, int(c)))
        location += int(c)
    else:
        files.append((location, int(c), fid))
        fid += 1
        location += int(c)
    free = not free

for i in reversed(range(len(files))):
    fs, fl, fid = files[i]
    for j in range(len(space)):
        es, el = space[j]
        if fl <= el and es < fs:
            space[j] = (es + fl, el -fl)
            files[i] = (es, fl, fid)
            break
# file (start, len, id)
# empyt (start, len)
count = 0
for fs, fl, fid in files:
    for a in range(fl):
        count += (fs + a) * fid

print(count)
