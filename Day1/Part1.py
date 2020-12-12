from itertools import combinations
print([i[0] * i[1] for i in combinations([int(l.strip()) for l in open("c:\\aoc\\2020\\Day1.txt")], 3) if i[0] + i[1] == 2020][0])