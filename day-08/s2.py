G = open(0).read().splitlines();
w = len(G[0])
h = len(G)

print(h, w)
an = set()
for row in range(h):
    for col in range(w):
        char = G[row][col]
        if char == ".": continue
        for r in range(h):
            for c in range(w):
                if char != G[r][c] or row == r and col == c: continue
                dr = r - row
                dc = c - col
                ar = row + dr
                ac = col + dc 
                while  0 <= ar < h and 0 <= ac < h:
                   an.add((ar, ac))
                   ar += dr
                   ac += dc

print(len(an))
