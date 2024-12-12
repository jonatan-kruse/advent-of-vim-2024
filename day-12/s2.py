G = dict([((row, col), plot) for row, line in enumerate(open(0).read().splitlines()) for col, plot in enumerate(line)])

added = set()
regions = {}

def add(plot, rs, v, G, coord, i):
    if coord in v or not coord in G or G[coord] != plot: 
        return
    rs.setdefault((plot, i), []).append(coord)
    v.add(coord)
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        x, y = coord
        add(plot, rs, v, G, (x+dx, y+dy), i)

for i, coord in enumerate(G.keys()):
    plot = G[coord]
    add(plot, regions, added, G, coord, i)
count = 0
for region in regions:
    plot, _ = region
    locations = regions[region]
    area = len(locations)
    perim = 0
    v = set()
    for x, y in locations:
        edges = []
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if not (x + dx, y + dy) in G or G[x + dx, y + dy] != plot:
                edges.append((dx, dy))
                if (dy, -dx) in edges: perim += 1
                if (-dy, dx) in edges: perim += 1           
                upright = (x + dx - dy, y + dy + dx)
                right = (x - dy, y + dx)
                if upright in G and G[upright] == plot and G[right] == plot: perim += 1
    count += area * perim
print(count)
