import heapq
G = dict([((col, row), plot) for row, line in enumerate(open(0).read().splitlines()) for col, plot in enumerate(line)])

def bfs(G, start):
    dist = {start: 0}
    x, y = start
    pq = [(0, (x, y))]
    while pq:
        cd, (x, y) = heapq.heappop(pq)
        if cd > dist.setdefault((x, y), float('inf')): continue
        for dx, dy in [(1, 0),(-1, 0),(0, 1),(0, -1)]:
            if cd + 1 < dist.setdefault((x + dx, y + dy), float('inf')) and (x + dx, y +dy) in G:
                if G[x+dx, y+dy] != "#":
                    dist[(x + dx, y + dy)] = cd + 1
                    heapq.heappush(pq, (cd + 1, (x+dx, y+dy)))
    return dist

c = 20
diffs = [(x,y) for x in range(-cl - 1, cl + 1) for y in range(-cl - 1, cl + 1) if (1 < abs(x) + abs(y) <= cl)]
for x, y in G:
    if G[x, y] == "S":
        start = (x, y)
        G[x, y] = "."
    if G[x, y] == "E":
        end = (x, y)
        G[x, y] = "."
dist = bfs(G, start)
diste = bfs(G, end)
ds = []
for x, y in G:
    if G[x, y] == ".":
        for cex, cey in [(x + dx, y + dy) for dx, dy in diffs]:
            if (cex, cey) in G and G[cex, cey] == ".":
                dtcs = dist[x,y]
                cd = abs(x - cex) + abs(y - cey)
                dte = diste[cex, cey]
                ds.append((dtcs + cd + dte, (x,y), (cex, cey)))

m = dist[end]
print(sum([1 for (x, s, e) in ds if m - x >= 100]))
    
