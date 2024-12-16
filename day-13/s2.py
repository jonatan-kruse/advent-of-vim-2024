import numpy as np

def parsemachine(string):
    lines = string.splitlines()
    a = [int(x.split("+")[1]) for x in lines[0].split(",")]
    b = [int(x.split("+")[1]) for x in lines[1].split(",")]
    p = [int(x.split("=")[1]) + 10000000000000 for x in lines[2].split(",")]
    return (a, b, p)

machines = list(map(parsemachine, open(0).read().split("\n\n")))
count = 0
for (a, b, p) in machines:
    basis = np.array([a, b]).T
    target = np.array(p)
    ass, bss = np.linalg.solve(basis, target)
    if abs(ass - round(ass)) < 0.001 and abs(bss - round(bss)) < 0.001 :
        count += ass * 3 + bss
print(int(count))
