m = [x.strip() for x in open(0)]
num = 0
for row in range(len(m)):
    for col in range(len(m[0])):
        if row - 1 >= 0 and col - 1 >= 0 and row + 1 < len(m) and col + 1 < len(m[0]):
           l1 = ''.join([m[row - x][col - x] for x in range(-1, 2)])
           l2 = ''.join([m[row - x][col + x] for x in range(-1, 2)])
           if (l1 == "MAS" or l1 == "SAM") and (l2 == "MAS" or l2 == "SAM"):
               num += 1
print(num)
