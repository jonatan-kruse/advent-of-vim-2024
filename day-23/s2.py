from functools import cache

adj = {}
for line in open(0).read().splitlines():
    v1, v2 = line.split("-")
    adj.setdefault(v1, set()).add(v2)
    adj.setdefault(v2, set()).add(v1)

@cache
def find(seen, v):
    opt = seen
    for u in adj[v]:
        if u in seen: 
            continue
        if all(x in adj[u] for x in seen):
            new_seen = tuple(sorted(seen + (u,)))
            new = find(new_seen, u)
            if len(new) > len(opt):
                opt = new
    return opt

opt = ()
for v in adj:
    seen = (v,)
    new = find(seen, v)
    if len(new) > len(opt):
        opt = new

print(",".join(sorted(list(opt))))
