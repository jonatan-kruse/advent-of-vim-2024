string = ""
for line in open(0):
    string += line
stage = ""
ans = 0;
num1 = ""
num2 = ""
for c in string:
    if stage == "" and c == "m":
        stage = "m"
        continue
    if stage == "m" and c == "u":
        stage = "u"
        continue
    if stage == "u" and c == "l":
        stage = "l"
        continue
    if stage == "l" and c == "(":
        stage = "num1"
        continue
    if stage == "num1" and c.isdigit() and len(num1) < 3:
        num1 += c
        continue
    if stage == "num1" and c == "," and len(num1) > 0:
        stage = "num2"
        continue
    if stage == "num2" and c.isdigit() and len(num2) < 3:
        num2 += c
        continue
    if stage == "num2" and c == ")" and len(num2) > 0:
        ans += int(num1) * int(num2)

    stage = ""
    num1 = ""
    num2 = ""
print(ans)

