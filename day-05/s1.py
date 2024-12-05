rules, updates = open(0).read().split("\n\n")
rtups = [x.split("|") for x in rules.splitlines()]
rdict = {}
for x, y in rtups:
    if x in rdict:
        rdict[x].append(y)
    else:
        rdict[x] = [y]
ans = 0;
for line in updates.splitlines():
    numbers = line.split(",")
    success = True
    for i in range(len(numbers)):
        num = numbers[i]
        if num in rdict and any([x in numbers[:i] for x in rdict[num]]):
            success = False
            break

    if success:
        ans += int(numbers[len(numbers) // 2])
print(ans)
