inpu = open(0).read().split("\n\n")

G = dict([((col, row), plot) for row, line in enumerate(inpu[0].splitlines()) for col, plot in enumerate(line)])
robot = (0, 0)
for x, y in G:
    if G[x, y] == "@":
        robot = (x, y)
        G[x, y] = "."

for c in inpu[1].replace("\n", ""):
    rx, ry = robot
    dx, dy = 1, 0
    if c == "<": dx, dy = -1, 0
    if c == "^": dx, dy = 0, -1
    if c == ">": dx, dy = 1, 0
    if c == "v": dx, dy = 0, 1
    if G[rx + dx, ry + dy] == "#": continue 
    if G[rx + dx, ry + dy] == ".": 
        robot = (rx + dx, ry + dy)
        continue
    cx, cy = dx + rx, dy + ry
    while G[cx, cy] == "O":
        cx += dx
        cy += dy
    if G[cx, cy] == ".":
        G[cx, cy] = "O"
        G[rx + dx, ry + dy] = "."
        robot = (rx + dx, ry + dy)

count = 0
for x, y in G:
    if G[x, y] == "O":
        count += 100 * y + x
print(count)

