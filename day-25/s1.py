blocks = open(0).read().split("\n\n")
keys = []
locks = []
for block in blocks:
    matrix = [list(group) for group in zip(*block.splitlines())]
    values = [x.count("#") - 1 for x in matrix]
    if matrix[0][0] == "#":
        locks.append(values)
    else:
        keys.append(values)

count = 0
for key in keys:
    for lock in locks:
        if all([x + y < 6 for x, y in zip(lock, key)]):
            count += 1
print(count)
