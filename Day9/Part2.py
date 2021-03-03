file = [int(l.strip()) for l in open("c:\\aoc\\2020\\Day9.txt")]

# answer to Part 1
goal = 90433990
t = 0
pre = []

for i in range(0, len(file)):
    for ii in range(0, 20):
        rt = 0
        for iii in range(i, i + ii):
            rt += file[iii]
        if rt > goal:
            break
        if rt == goal:
            goods = []
            for iii in range(i, i + ii):
                goods.append(file[iii])
            print(min(goods) + max(goods))
            exit()
