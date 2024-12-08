lines = open(0).read().splitlines()

def check(t, v, l):
    if t == v: return True
    if len(l) == 0: return False
    return check(t, v * l[0], l[1:]) or check(t, v + l[0], l[1:])

count = 0
for line in lines:
    num, nums = line.split(":")
    nums = list(map(int, nums.split()))
    num = int(num)
    if check(num, nums[0], nums[1:]): count += num

print(count)
