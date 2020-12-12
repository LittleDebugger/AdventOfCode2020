file = [l.strip() for l in open("c:\\aoc\\2020\\Day3.txt")]

y = 0
x = 0
t = 0

while y < len(file):
    if file[y][x % len(file[y])] == '#':
        t += 1
    x += 3
    y += 1
print(t)



