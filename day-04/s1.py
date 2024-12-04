m = [x.strip() for x in open(0)]
mt = []
for col in range(len(m[0])):
    mt.append([])
    for row in range(len(m)):
        mt[col].append(m[row][col])
num = 0
for row in range(len(m)):
    num += m[row].count("XMAS") + m[row].count("SAMX")
for row in range(len(mt)):
    string = ''.join(mt[row])
    num += string.count("XMAS") + string.count("SAMX")
for row in range(len(m)):
    for col in range(len(m[0])):
        if row - 3 >= 0 and col - 3 >= 0:
           l = ''.join([m[row - x][col - x] for x in range(4)])
           if l == "XMAS" or l == "SAMX":
               num += 1
        if row - 3 >= 0 and col + 3 < len(m[0]):
           l = ''.join([m[row - x][col + x] for x in range(4)])
           if l == "XMAS" or l == "SAMX":
               num += 1
print(num)
