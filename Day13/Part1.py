line = 1008169
line2 = '29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,653,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,17,x,x,x,x,x,23,x,x,x,x,x,x,x,823,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19'

nums = []
b = line2.split(',')
for a in b:
    try:
        nums.append(int(a))
    except:
        pass

bus = 0
min = 100000

for a in nums:
    if a - (line % a) < min:
        min = (a - (line % a) % a)
        bus = a
print(min * bus)
