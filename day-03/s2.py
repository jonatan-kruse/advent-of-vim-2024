string = ""
for line in open(0):
    string += line
stage = ""
stage2 = ""
shouldMul = True
ans = 0;
num1 = ""
num2 = ""
for c in string:
    if stage2 == "" and c == "d":
        stage2 = "d"
        stage = ""
        num1 = ""
        num2 = ""
        continue
    if stage2 == "d" and c == "o":
        stage2 = "o"
        stage = ""
        num1 = ""
        num2 = ""
        continue
    if stage2 == "o" and c == "(":
        stage2 = "do("
        stage = ""
        num1 = ""
        num2 = ""
        continue
    if stage2 == "do(" and c == ")":
        stage2 = ""
        stage = ""
        num1 = ""
        num2 = ""
        shouldMul = True
        continue
    if stage2 == "o" and c == "n":
        stage2 = "n"
        stage = ""
        num1 = ""
        num2 = ""
        continue
    if stage2 == "n" and c == "'":
        stage2 = "'"
        stage = ""
        num1 = ""
        num2 = ""
        continue
    if stage2 == "'" and c == "t":
        stage2 = "t"
        stage = ""
        num1 = ""
        num2 = ""
        continue
    if stage2 == "t" and c == "(":
        stage2 = "don't("
        stage = ""
        num1 = ""
        num2 = ""
        continue
    if stage2 == "don't(" and c == ")":
        stage2 = ""
        stage = ""
        num1 = ""
        num2 = ""
        shouldMul = False
        continue

    if stage == "" and c == "m":
        stage = "m"
        stage2 = ""
        continue
    if stage == "m" and c == "u":
        stage = "u"
        stage2 = ""
        continue
    if stage == "u" and c == "l":
        stage = "l"
        stage2 = ""
        continue
    if stage == "l" and c == "(":
        stage = "num1"
        stage2 = ""
        continue
    if stage == "num1" and c.isdigit() and len(num1) < 3:
        num1 += c
        stage2 = ""
        continue
    if stage == "num1" and c == "," and len(num1) > 0:
        stage = "num2"
        stage2 = ""
        continue
    if stage == "num2" and c.isdigit() and len(num2) < 3:
        num2 += c
        stage2 = ""
        continue
    if stage == "num2" and c == ")" and len(num2) > 0:
        stage2 = ""
        if shouldMul:
            ans += int(num1) * int(num2)

    stage = ""
    num1 = ""
    num2 = ""
print(ans)

