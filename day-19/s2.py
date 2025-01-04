from functools import cache

inpu = open(0).read().split("\n\n")
ts = inpu[0].replace(" ", "").split(",")

@cache
def find(design):
    if design == "": return 1
    c = 0
    for t in ts:
        if design.startswith(t):
            c += find(design[len(t):])
    return c

print(sum([find(design) for design in inpu[1].splitlines()]))
