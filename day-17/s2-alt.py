inpu = open(0).read().split("\n\n")
ins = [int(x) for x in inpu[1].split(":")[1].split(",")]

def find(target, A):
    if len(target) == 0: return A
    for i in range(8):
        a = A << 3 | i
        if ((a % 8 ^ 1) ^ (a >> (a % 8 ^ 1)) ^ 6) % 8 == target[-1]: 
            ans = find(target[:-1], a)
            if ans == None: continue
            return ans

print(find(ins, 0))
