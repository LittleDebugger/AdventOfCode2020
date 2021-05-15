from collections import defaultdict as dd

file = [l.strip() for l in open("c:\\aoc\\2020\\Day6.txt")]
print(file[0])

t = 0
counts = dd(lambda: 0)

for l in file:
    if not l:
        t += len(counts)
        counts = dd(lambda: 0)
    else:
        for c in l:
            counts[c] = counts[c] + 1

print(t)
