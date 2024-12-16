inpu = open(0).read().split("\n\n")
fixed = inpu[0].replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
G = dict([((col, row), plot) for row, line in enumerate(fixed.splitlines()) for col, plot in enumerate(line)])
robot = (0, 0)
for x, y in G:
    if G[x, y] == "@":
        robot = (x, y)
        G[x, y] = "."

otherx = {"[": 1, "]": -1}
def check(G, boxes, x, y, dy):
    boxes.append(((x, y), G[x,y]))
    G[x,y] = "."
    if G[x, y+dy] == "#": return False
    if G[x, y+dy] == ".": return True
    return check(G, boxes, x + otherx[G[x,y+dy]], y+dy, dy) and check(G, boxes, x, y+dy, dy) 

for c in inpu[1].replace("\n", ""):
    # for row in range(len(fixed.splitlines())):
        # for col in range(len(fixed.splitlines()[0])):
            # if (col, row) == robot: print("@", end="")
            # else: print(G[col,row], end = "") 
        # print()
    # print(c)
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
    if dy == 0:
        cx, cy = dx + rx, dy + ry
        boxes = []
        while G[cx, cy] in ["[", "]"]:
            boxes.append(((cx, cy), G[cx, cy]))
            G[cx, cy] = "."
            cx += dx
            cy += dy
        if G[cx, cy] == ".":
            for ((x, y), l) in boxes:
                G[x + dx, y + dy] = l
            robot = (rx + dx, ry + dy)
        else:
            for ((x, y), l) in boxes:
                G[x, y] = l
    else:
        boxes = []
        if check(G, boxes, rx + otherx[G[rx,ry+dy]], ry+dy, dy) and check(G, boxes, rx, ry+dy, dy):
            for ((x, y), l) in boxes:
                G[x + dx, y + dy] = l
            robot = (rx + dx, ry + dy)
        else:
            for ((x, y), l) in boxes:
                G[x, y] = l

count = 0
for x, y in G:
    if G[x, y] == "[":
        count += 100 * y + x
print(count)

