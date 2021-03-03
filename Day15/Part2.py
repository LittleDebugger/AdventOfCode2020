from collections import defaultdict as dd

file = [l.strip() for l in open("c:\\aoc\\2020\\Day15.txt")]

nums = [int(m) for m in file[0].split(',')]
posOfLast = dd(lambda: - 1)

spoken = nums[:]
i = 0
for a in nums[:-1]:
    posOfLast[a] = i
    i += 1

next = nums[-1]
while i < 30000000:
    previous = next
    prevPos = posOfLast[next]
    if prevPos >= 0:
        next = i - prevPos
    else:
        next = 0
    posOfLast[previous] = i
    i += 1
print(previous)
