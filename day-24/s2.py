inpu = open(0).read().split("\n\n")
F = {}
for line in inpu[0].splitlines():
    wire, value = line.split(":")

for line in inpu[1].splitlines():
    l, op, r, out = line.replace("->", "").split()
    l, r = sorted([l, r])
    F[out] = (l, op, r)
def mw(c, n):
    return c + str(n).rjust(2, "0")

def v_z(wire, num):
    print("vz", wire, num)
    l, op, r = F[wire]
    if op != "XOR": return False
    if num == 0:  return [l, r] == ["x00", "y00"]
    return (v_xor(l, num) and v_carry(r, num)) or (v_xor(r, num) and v_carry(l, num))
    
def v_xor(wire, num):
    print("vx", wire, num)
    l, op, r = F[wire]
    if op != "XOR": return False
    return [l, r] == [mw("x", num), mw("y", num)]

def v_carry(wire, num):
    print("vc", wire, num)
    l, op, r = F[wire]
    if num == 1:
       return op == "AND" and [l, r] == ["x00", "y00"]
    if op != "OR": return False
    return (v_d_carry(l, num - 1) and v_r_carry(r, num - 1)) or (v_d_carry(r, num - 1) and v_r_carry(l, num - 1))

def v_d_carry(wire, num):
    print("vd", wire, num)
    l, op, r = F[wire]
    return [l, r] == [mw("x", num), mw("y", num)] and op == "AND"

def v_r_carry(wire, num):
    print("vr", wire, num)
    l, op, r = F[wire]
    if op != "AND": return False
    return (v_xor(l, num) and v_carry(r, num)) or (v_xor(r, num) and v_carry(l, num))
    
def verify(num):
    return v_z(mw("z", num), num)

i = 0
while True:
    if not verify(i): break
    i += 1

print()
print(verify(i))
print("failed to verify: ", mw("z", i))
# hwk <--> z06
# tnt <--> qmd
# z31 <--> hpc
# z37 <--> cgr
