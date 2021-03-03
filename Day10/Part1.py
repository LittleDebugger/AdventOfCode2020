file = [int(l.strip()) for l in open("c:\\aoc\\2020\\Day10.txt")]
file.sort()

c = 0
ones = 0
threes = 1
for a in file:
    if a == c + 1:
        ones += 1
    elif a == c + 3:
        threes += 1
    c = a
print(ones * threes)