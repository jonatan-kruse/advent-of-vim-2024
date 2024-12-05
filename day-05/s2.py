import itertools

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
    for i in range(len(numbers)):
        num = numbers[i]
        if num in rdict and any([x in numbers[:i] for x in rdict[num]]):
            nums = []
            numsleft = numbers
            for j in range(len(numbers)):
                forbidden = sum([rdict.get(x, []) for x in numsleft], [])
                allowed = [x for x in numsleft if not x in forbidden]
                nums.append(allowed[0])
                numsleft.remove(allowed[0])
            ans += int(nums[len(nums) // 2])
            break
print(ans)
