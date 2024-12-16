pos = []
#h, w = 7, 11
h, w = 103, 101
for line in open(0):
    px, py, vx, vy = list(map(int, line.replace("p=", "").replace("v=", "").replace(",", " ").split()))
    x = (px + 100 * vx) % w
    y = (py + 100 * vy) % h
    pos.append((x, y))
quadrants = [0, 0, 0, 0]
for px, py in pos:
    if px < w // 2:
        if py < h // 2:
            quadrants[0] += 1
        if py > h // 2:
            quadrants[1] += 1
    if px > w // 2:
        if py < h // 2:
            quadrants[2] += 1
        if py > h // 2:
            quadrants[3] += 1

res = 1
for n in quadrants:
    res *= n
print(res)
