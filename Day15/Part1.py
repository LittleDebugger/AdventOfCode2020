file = [l.strip() for l in open("c:\\aoc\\2020\\Day15.txt")]

nums = [int(m) for m in file[0].split(',')]
spoken = nums[:]

while len(spoken) < 2020:
    next = 0
    for ii in range(len(spoken) - 2, -1, -1):
        if spoken[ii] == spoken[-1]:
            next = len(spoken) - ii -1
            break

    spoken.append(next)
print(spoken[-1])
