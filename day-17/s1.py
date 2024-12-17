inpu = open(0).read().split("\n\n")
regs = inpu[0].splitlines();
A = int(regs[0].split(":")[1])
B = int(regs[1].split(":")[1])
C = int(regs[2].split(":")[1])

pc = 0
ins = [int(x) for x in inpu[1].split(":")[1].split(",")]
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
        case 0: A //= 2**combo
        case 1: B ^= op
        case 2: B = combo % 8
        case 3: 
            if A != 0:
                pc = op
                continue
        case 4: B ^= C
        case 5: out.append(str(combo % 8))
        case 6: B = A // 2**combo
        case 7: C = A // 2**combo
    pc += 2
print(",".join(out))
