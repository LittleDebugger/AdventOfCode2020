file = [l.strip() for l in open("c:\\aoc\\2020\\Day18.txt")]

stack = []
stack.append([1, 'mul'])

total = 0


def opToTop(ss):
    global stack
    num = int(ss)
    if stack[-1][1] == 'add':
        stack[-1][0] += num
        stack[-1][1] = ''
    elif stack[-1][1] == 'mul':
        stack[-1][0] *= num
        stack[-1][1] = ''
    else:
        print('NOOO')
        exit()


for line in file:

    open = False
    stack = []
    stack.append([1, 'mul'])
    splits = line.split()

    close = 0
    for s in splits:

        if s == '*':
            stack[-1][1] = 'mul'
            continue
        elif s == '+':
            stack[-1][1] = 'add'
            continue
        elif s.startswith('('):
            while s.startswith('('):
                s = s[1:]
                stack.append([1, 'mul'])
        elif s.endswith(')'):
            while s.endswith(')'):
                s = s[0:-1]
                close += 1
                pass

        opToTop(s)

        for i in range(0, close):
            top = stack[-1]
            stack.remove(top)
            opToTop(top[0])
        close = 0

    total += stack[0][0]

    if len(stack) > 1:
        print(stack)
        print('fail!')
        exit()

print(total)
