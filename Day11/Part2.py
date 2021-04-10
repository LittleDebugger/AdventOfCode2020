file = [l.strip() for l in open("c:\\aoc\\2020\\Day11.txt")]

grid = ["." * (len(file[0]) + 2)]

for l in file:
    line = ['.']
    for c in l:
        line.append(c)
    line.append('.')
    grid.append(line)
grid.append("." * (len(file[0]) + 2))


width = len(grid[1])
height = len(grid)

i = 0

copy = []
for l in grid:
    copy.append(l[:])

while i < 100:
    i += 1
    t = 0
    for y in range(1, len(grid) - 1):
        for x in range(1, width - 1):
            if grid[y][x] == '#':
                t += 1
    print(t)

    def isTaken(xl, yl, xx, yy):
        while True:
            xl += xx
            yl += yy
            if xl < 0 or xl >= width or yl < 0 or yl >= height:
                return 0
            if grid[yl][xl] == '.':
                continue
            return 1 if grid[yl][xl] == '#' else 0

    for y in range(1, len(grid) - 1):
        for x in range(1, width - 1):
            count = 0
            count += isTaken(x, y, -1, -1)
            count += isTaken(x, y, 0, -1)
            count += isTaken(x, y, 1, -1)
            count += isTaken(x, y, -1, 0)
            count += isTaken(x, y, 1, 0)
            count += isTaken(x, y, -1, 1)
            count += isTaken(x, y, 0, 1)
            count += isTaken(x, y, 1, 1)

            if grid[y][x] == 'L':
                if count == 0:
                    copy[y][x] = '#'
            elif grid[y][x] == '#' and count >= 5:
                copy[y][x] = 'L'

    grid = []
    for l in copy:
        grid.append(l[:])
