m = open(0).read().splitlines()
num = 0
for row in range(1, len(m) - 1):
    for col in range(1, len(m[0]) - 1):
           l1 = ''.join([m[row - x][col - x] for x in range(-1, 2)])
           l2 = ''.join([m[row - x][col + x] for x in range(-1, 2)])
           if l1 in ["MAS", "SAM"] and l2 in ["MAS", "SAM"]:
               num += 1
print(num)
