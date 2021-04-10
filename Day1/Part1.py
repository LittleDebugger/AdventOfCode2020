file = [int(l.strip()) for l in open("c:\\aoc\\2020\\Day1.txt")]

for a in range(0, len(file)):
    if file[a] > 2020:
        continue
    for b in range(a + 1, len(file)):
        if file[a] == file[b]:
            continue
        if file[a] + file[b] == 2020:
            print(file[a], file[b], file[a] * file[b])
            exit()
