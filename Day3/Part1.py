file = [l.strip() for l in open("c:\\aoc\\2020\\Day3.txt")]

y = 0
x = 0
t = 0

while y < len(file):
    x += 3
    y += 1
    try:
        if file[y][x % len(file[y])] == '#':
            t += 1
    except:
        pass

print(t)



