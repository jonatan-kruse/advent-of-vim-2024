import heapq
G = dict([((col, row), plot) for row, line in enumerate(open(0).read().splitlines()) for col, plot in enumerate(line)])

def bfs(G, pos, start):
    dist = {start: 0}
    x, y = start
    pq = [(0, (x, y), False)]
    while pq:
        cd, (x, y), c = heapq.heappop(pq)
        if G[x,y] == "E": return cd
        if cd > dist.setdefault((x, y), float('inf')): continue
        d = cd + 1
        for dx, dy in [(1, 0),(-1, 0),(0, 1),(0, -1)]:
            if d < dist.setdefault((x + dx, y + dy), float('inf')) and (x + dx, y +dy) in G:
                if (x + dx, y + dy) == pos:
                    dist[(x + dx, y + dy)] = d
                    heapq.heappush(pq, (d, (x+dx, y+dy), True))
                elif G[x+dx, y+dy] != "#":
                    dist[(x + dx, y + dy)] = d
                    heapq.heappush(pq, (d, (x+dx, y+dy), False))

for x, y in G:
    if G[x, y] == "S":
        start = (x, y)
        G[x, y] = "."
ds = []
for pos in G:
    if G[pos] == "#":
        ds.append(bfs(G, pos, start))
m = max(ds)

print(sum([1 for x in ds if m - x >= 100]))
    
