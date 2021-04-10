from collections import defaultdict
from collections import Counter
line2 = '29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,653,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,17,x,x,x,x,x,23,x,x,x,x,x,x,x,823,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19'

nums = []
b = line2.split(',')
c = 0
busMax = (0, 0)
for a in b:
    try:
        t = [int(a), c]
        nums.append(t)
        if t[0] > busMax[0]:
            busMax = t
    except:
        pass
    c += 1

size = 1
for num in nums:
    size *= num[0]
t = 0
for n in nums[1:]:
    c = size // n[0]
    for b in range(1, c):
        if (c * b) % n[0] == 1:
            t += (c * b) * (n[0] - n[1])
            t = t % size
            break
print(t)
