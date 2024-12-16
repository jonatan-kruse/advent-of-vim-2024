from functools import cache
def parsemachine(string):
    lines = string.splitlines()
    a = tuple([int(x.split("+")[1]) for x in lines[0].split(",")])
    b = tuple([int(x.split("+")[1]) for x in lines[1].split(",")])
    p = tuple([int(x.split("=")[1]) for x in lines[2].split(",")])
    return (a, b, p)

@cache
def findprize(a, b, left, cost):
    ax, ay = a
    bx, by = b
    px, py = left
    if px == 0 and py == 0:
        return cost
    if (ax > px or ay > py) and (bx > px or by > py):
        return None
    bcost = findprize(a, b, (px - bx, py - by), cost + 1)
    if (bcost != None): return bcost
    else: return findprize(a, b, (px - ax, py - ay), cost + 3)

machines = list(map(parsemachine, open(0).read().split("\n\n")))
count = 0
for (a, b, p) in machines:
    cost = findprize(a, b, p, 0)
    if cost != None: count += cost
print(count)
