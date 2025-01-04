from functools import cache

codes = open(0).read().splitlines()
KP = {
    "7": (0, 0), "8": (1, 0), "9": (2, 0),
    "4": (0, 1), "5": (1, 1), "6": (2, 1),
    "1": (0, 2), "2": (1, 2), "3": (2, 2),
    "0": (1, 3), "A": (2, 3),
}

RP = {
    "U": (1, 0), "A": (2, 0),
    "L": (0, 1), "D": (1, 1), "R": (2, 1),
}

# alla e kombination av två riktnigar  R1 * len, R2 * len
# testa kombinationerna R1 * len och R2 * len t.ex DDU och UDD

@cache
def find(c, lastc, isRP = False):
    G = KP
    if isRP: G = RP
    rx, ry = G[lastc]
    tx, ty = G[c]
    dx = tx - rx
    dy = ty - ry
    pos = []
    if (rx + dx, ry) in G.values():
        out = ""
        if dx < 0: out += "L" * -dx
        if dx > 0: out += "R" * dx
        if dy > 0: out += "D" * dy
        if dy < 0: out += "U" * -dy
        out += "A"
        pos.append(out)
    if (rx, ry + dy) in G.values():
        out = ""
        if dy > 0: out += "D" * dy
        if dy < 0: out += "U" * -dy
        if dx > 0: out += "R" * dx
        if dx < 0: out += "L" * -dx
        out += "A"
        pos.append(out)
    return pos
    
@cache
def shortestRP(lastc, c, n):
    nexts = find(c, lastc, True)
    if n == 0: return len(nexts[0])
    cs = []
    for pos in nexts:
        lastc = "A"
        c = 0
        for i in range(len(pos)):
            if i > 0: lastc = pos[i-1]
            c += shortestRP(lastc, pos[i], n - 1)
        cs.append(c)
    return min(cs)

def shortestKP(I, n):
    lastc = "A"
    cs = []
    strings = [""]
    for c in I:
        pos = find(c, lastc)
        newstrings = []
        for string in strings:
            for p in pos:
                newstrings.append(string + p)
        strings = newstrings
        lastc = c
    for pos in set(strings):
        lastc = "A"
        c = 0
        for i in range(len(pos)):
            if i > 0: lastc = pos[i-1]
            c += shortestRP(lastc, pos[i], n - 1)
        cs.append(c)
    return min(cs)

count = 0
for line in codes:
    S = shortestKP(line, 25)
    N = int(line.lstrip("0").replace("A", ""))
    count += S * N
print(count)
    
