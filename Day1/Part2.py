file = [int(l.strip()) for l in open("c:\\aoc\\2020\\Day1.txt")]
print(file[0])

for a in range(0, len(file)):
    if file[a] > 2020:
        continue
    for b in range(a + 1, len(file)):
        if file[a] == file[b]:
            continue
        for c in range(b + 1, len(file)):
            if file[a] == file[c]:
                continue
            if file[a] + file[b] + file[c] == 2020:
                print(file[a], file[b], + file[c], file[a] * file[b] * + file[c])
                exit()