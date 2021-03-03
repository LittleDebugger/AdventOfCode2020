file = [int(l.strip()) for l in open("c:\\aoc\\2020\\Day9.txt")]

pre = []
t = 0

for l in file:
    if len(pre) < 25:
        pre.append(l)
    else:
        good = False
        for i, p in enumerate(pre):
            if good:
                break
            for ii, pp in enumerate(pre):
                if i == ii:
                    continue
                if good:
                    break
                if pp + p == l:
                    t += 1
                    good = True
        if not good:
            print(l)
            exit()
        pre.append(l)
        pre.pop(0)

print(t)
