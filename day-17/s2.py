inpu = open(0).read().split("\n\n")

ins = [int(x) for x in inpu[1].split(":")[1].split(",")]
def run(A, ins):
    B = 0
    C = 0
    pc = 0
    out = []
    while pc < len(ins) - 1:
        i = ins[pc]
        op = ins[pc + 1]
        combo = op
        match op:
            case 4: combo = A
            case 5: combo = B
            case 6: combo = C
        match i:
            case 0: A >>= combo
            case 1: B ^= op
            case 2: B = combo % 8
            case 3: 
                if A != 0:
                    pc = op
                    continue
            case 4: B ^= C
            case 5: out.append(combo % 8)
            case 6: B = A >> combo
            case 7: C = A >> combo
        pc += 2
    return out

out = list(reversed(ins))
lasto = None
possibleA = [0]
os = []
for i in range(len(out)):
    o = out[i]
    os = ins[-(i + 1):]
    nexposA = []
    for A in possibleA:
        for j in range(1 << 6):
            a = (A << 3) + j
            if run(a, ins) == os: 
                nexposA.append(a)
    if len(nexposA) == 0: print("WARNING NO POSSIBLE SOLUTION")
    lasto = o
    possibleA = nexposA
print(min(possibleA + [float('inf')]))

