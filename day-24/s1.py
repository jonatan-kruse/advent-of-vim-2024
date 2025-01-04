inpu = open(0).read().split("\n\n")
D = {}
for line in inpu[0].splitlines():
    wire, value = line.split(":")
    D[wire] = int(value)

def calculate(left, op, right):
    if op == "XOR": return left ^ right
    if op == "AND": return left & right
    if op == "OR": return left | right
    print("ERROR: no valid opperand")

Q = []
for line in inpu[1].splitlines():
    left, op, right, out = line.replace("->", "").split()
    Q.append((left, op, right, out))

while Q:
    left, op, right, out = Q.pop(0)
    if left in D and right in D:
        D[out] = calculate(D[left], op, D[right])
    else:
        Q.append((left, op, right, out))

zs = sorted([w for w in D if w.startswith("z")], reverse=True)
print(int("".join([str(D[w]) for w in zs]), 2))

