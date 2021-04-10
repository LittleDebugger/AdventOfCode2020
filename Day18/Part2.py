orig = ''
file = [l.strip().replace(' ', '') for l in open("c:\\aoc\\2020\\Day18.txt")]

t = 0
for line in file:
    i = 0

    def getNum():
        nums = []
        ops = []

        global i
        while i < len(line) and line[i] != ')':
            if line[i] == '(':
                i += 1
                nums.append(getNum())
            elif line[i] in ['+', '*']:
                ops.append(line[i])
            else:
                nums.append(int(line[i]))
            i += 1

        if len(nums) != len(ops) + 1:
            print('BAD')
            exit(0)
        for c in ['+', '*']:
            while c in ops:
                for ii, o in enumerate(ops):
                    if o == c:
                        ops.pop(ii)
                        if c == '+':
                            nums[ii] = nums[ii] + nums[ii + 1]
                        else:
                            nums[ii] = nums[ii] * nums[ii + 1]

                        nums.pop(ii + 1)
                        continue
        return nums[0]

    num = getNum()
    t += num
print(t)
