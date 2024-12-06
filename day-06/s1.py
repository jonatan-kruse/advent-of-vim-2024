m = list(map(list, open(0).read().splitlines()))
pos = (0, 0)
w = len(m[0])
h = len(m)
d = (0, -1)
v = set()

for y in range(h):
    for x in range(w):
        if m[y][x] == "^":
            pos = (x, y)

def change_d(dd):
    if dd == (0, 1):
        return (-1, 0)
    if dd == (1, 0):
        return (0, 1)
    if dd == (0, -1):
        return (1, 0)
    if dd == (-1, 0):
        return (0, -1)

while True: 
    v.add(pos)
    new_pos = (pos[0] + d[0], pos[1] + d[1])
    if not (0 <= new_pos[0] < w) or not (0 <= new_pos[1] < h): break 
    if m[new_pos[1]][new_pos[0]] == "#":
        d = change_d(d)
        continue
    pos = new_pos

print(len(v))
