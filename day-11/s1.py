stones = list(map(int, open(0).read().split())  )
for j in range(25):
    for i in range(len(stones)):
        stone = stones[i]
        if stone == 0:
            stones[i] = 1
        elif len(str(stone)) % 2 == 0:
            s1 = int(str(stone)[:len(str(stone)) // 2])
            s2 = int(str(stone)[len(str(stone)) // 2:])
            stones[i] = s1
            stones.append(s2)
        else:
            stones[i] = stone * 2024

print(len(stones))

