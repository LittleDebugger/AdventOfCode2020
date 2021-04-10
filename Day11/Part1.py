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

while i < 1000:
    i += 1
    t = 0
    for y in range(1, len(grid) - 1):
        for x in range(1, width - 1):
            if grid[y][x] == '#':
                t += 1
    print(t)
``
   for y in range(1, len(grid) - 1):
        for x in range(1, width - 1):
            count = 0
            if grid[y - 1][x - 1] == '#':
                count += 1
            if grid[y - 1][x] == '#':
                count += 1
            if grid[y - 1][x + 1] == '#':
                count += 1
            if grid[y][x - 1] == '#':
                count += 1
            if grid[y][x + 1] == '#':
                count += 1
            if grid[y + 1][x - 1] == '#':
                count += 1
            if grid[y + 1][x] == '#':
                count += 1
            if grid[y + 1][x + 1] == '#':
                count += 1

            if grid[y][x] == 'L':
                if count == 0:
                    copy[y][x] = '#'
            elif grid[y][x] == '#' and count >= 4:
                copy[y][x] = 'L'

    grid = []
    for l in copy:
        grid.append(l[:])
