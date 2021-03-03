file = [int(l.strip()) for l in open("c:\\aoc\\2020\\Day10.txt")]
file.append(0)
file.sort()

t = 1
previous = 0

landsAfterThree = []
for a in range(1, len(file)):
    if file[a] == file[a - 1] + 3:
        landsAfterThree.append((previous, a))
        previous = a
if landsAfterThree[-1][1] != len(file):
    landsAfterThree.append((previous, len(file)))

for l in landsAfterThree:
    num = (file[l[1] - 1] - file[l[0]])
    if num < 2:
        pass
    elif num == 2:
        t *= 2
    elif num == 3:
        t *= 4
    elif num == 4:
        t *= 7
print(t)
