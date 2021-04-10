keys = [14222596, 4057428]

n = 1
subject = 7

i = 0

public = dict()

while True:
    i += 1
    n *= subject
    n = n % 20201227
    if n in keys:
        if n not in public:
            public[n] = i
        if len(public) == 2:
            break


def go(subject, i):
    n = 1
    for i in range(0, i):
        n *= subject
        n = n % 20201227
    return n


print(go(keys[1], public[keys[0]]))
