import heapq
G = dict([((col, row), plot) for row, line in enumerate(open(0).read().splitlines()) for col, plot in enumerate(line)])
start = (0, 0)
for x, y in G:
    if G[x, y] == "S":
        start = (x, y, "e")
        G[x, y] = "."
dist = {start: 0}
pq = [(0, start)]
rotate = {"s": ["e", "w"], "e": ["n", "s"], "n": ["e", "w"], "w": ["n", "s"]}
while pq:
    cd, (x, y, f) = heapq.heappop(pq)
    if cd > dist.setdefault((x, y, f), float('inf')): continue
    dx = 0 if f in ["n", "s"] else 1 if f == "e" else -1
    dy = 0 if f in ["e", "w"] else 1 if f == "s" else -1
    d = cd + 1
    if d < dist.setdefault((x + dx, y + dy, f), float('inf')) and G[x+dx, y+dy] != "#":
        dist[(x + dx, y + dy, f)] = d
        heapq.heappush(pq, (d, (x+dx, y+dy, f)))
    
    for n in rotate[f]:
        d = cd + 1000
        if d < dist.setdefault((x,y,n), float('inf')):
            dist[(x, y, n)] = d
            heapq.heappush(pq, (d, (x, y, n)))
for x, y in G:
    if G[x, y] == "E":
        print(min([dist[(x, y, f)] for f in rotate]))
    
