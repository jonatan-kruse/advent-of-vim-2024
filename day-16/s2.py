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
pred = {start: []}
while pq:
    cd, (x, y, f) = heapq.heappop(pq)
    if cd > dist.setdefault((x, y, f), float('inf')): continue
    dx = 0 if f in ["n", "s"] else 1 if f == "e" else -1
    dy = 0 if f in ["e", "w"] else 1 if f == "s" else -1
    d = cd + 1
    new = (x + dx, y + dy, f)
    if d <= dist.setdefault(new, float('inf')) and G[x+dx, y+dy] != "#":
        if d < dist[new]:
            dist[new] = d
            pred[new] = [(x, y, f)]
            heapq.heappush(pq, (d, new))
        elif d == dist[new]:
            pred[new].append((x, y, f))
    
    for n in rotate[f]:
        d = cd + 1000
        new = (x, y, n)
        if d <= dist.setdefault(new, float('inf')):
            if d < dist[new]:
                dist[new] = d
                pred[new] = [(x, y, f)]
                heapq.heappush(pq, (d, new))
            elif d == dist[new]:
                pred[new].append((x, y, f))
ends = []
for x, y in G:
    if G[x, y] == "E":
        ends = [(x, y, f) for f in rotate if (x, y, f) in dist]

def paths(preds, end_state, path=None):
    if path is None: path = [end_state]
    else:
        path = path + [end_state]
    
    if end_state not in preds or not preds[end_state]:
        return [path[::-1]]
    
    all_paths = []
    for pred in preds[end_state]:
        all_paths.extend(paths(preds, pred, path))
    return all_paths

all_paths = []
for end in ends:
    if dist[end] == min(dist[e] for e in ends):
        all_paths.extend(paths(pred, end))
coords = set()
for idx, path in enumerate(all_paths):
    cs = [(x, y) for x, y, _ in path]
    coords.update(cs)
print(len(coords))
