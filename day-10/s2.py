G = [[int(x) for x in line] for line in open(0).read().splitlines()]

ths = [(c, r) for r, row in enumerate(G) for c, val in enumerate(row) if val == 0]

def step(c, r, h, G):
    if h == 9: return 1
    w = len(G[0])
    t = len(G)
    steps = []
    for dc, dr in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nc = c + dc
        nr = r + dr
        nh = h + 1
        if 0 <= nc < w and 0 <= nr < t and G[nr][nc] == nh:
            steps.append(step(nc, nr, nh, G))

    return sum(steps)

count = 0
for c, r in ths:
    count += step(c, r, 0, G) 

print(count)
