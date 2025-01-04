size = 71 
read = 1024
G = dict([((x, y), 1) for x in range(size) for y in range(size)])
coords = [tuple(map(int, line.split(","))) for line in open(0).read().splitlines()]
for c in coords[:read]:
    G[c] = 0
end = (size-1,size-1)
v = set((0,0))
q = [(0,0,0)]
while q:
    (x, y, d) = q.pop(0)
    if (x, y) == end:
        print(d);
    for (dx, dy) in [(1,0),(0,1),(-1,0),(0,-1)]:
        n = (x+dx, y+dy) 
        if n not in v and n in G and G[n]:
            v.add(n)
            q.append((x+dx,y+dy,d+1))
            
