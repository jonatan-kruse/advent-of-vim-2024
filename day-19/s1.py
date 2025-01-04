inpu = open(0).read().split("\n\n")
ts = inpu[0].replace(" ", "").split(",")

def find(design):
    if design == "": return True
    for t in ts:
        if design.startswith(t):
            if find(design[len(t):]):
                return True
    return False

print(sum([find(design) for design in inpu[1].splitlines()]))
