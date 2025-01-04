edges = []

for line in open(0).read().splitlines():
    e1, e2 = sorted(line.split("-"))
    edges.append((e1, e2))

edges.sort()
count = 0
for i in range(len(edges) - 1):
    v1, v2 = edges[i]
    for j in range(i + 1, len(edges)):
        u1, u2 = edges[j]
        if u1 != v1: break
        if (v1.startswith("t") or v2.startswith("t") or u2.startswith("t")) and (v2, u2) in edges:
            count += 1
print(count)
