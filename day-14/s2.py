#h, w = 7, 11
h, w = 103, 101
lines = open(0).read().splitlines()
smallest = (0, 1000000000000000000)
for i in range(0, 10000):
    pos = []
    for line in lines:
        px, py, vx, vy = list(map(int, line.replace("p=", "").replace("v=", "").replace(",", " ").split()))
        x = (px + i * vx) % w
        y = (py + i * vy) % h
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
    if res < smallest[1]:
        smallest = (i, res)

print(smallest)
