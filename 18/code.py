file = open('input.txt')
inp = file.readlines()
file.close()

size = 71

map = [[0 for j in range(size)] for k in range(size)]

for i in range(2868):
    x, y = [int(u) for u in inp[i].split(',')]
    map[x][y] = 1

here = [[0, 0]]
map[0][0]= 2

steps = 0
while not([70, 70] in here):
    # print(steps, here)
    steps += 1
    next = []
    for h in here:
        for step in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            iNext = h[0] + step[0]
            jNext = h[1] + step[1]
            if iNext > -1 and jNext > -1 and iNext < 71 and jNext < 71 and map[iNext][jNext] == 0:
                next.append([iNext, jNext])
                map[iNext][jNext] = 2
    here = next
print(steps)


# part two

flag = 0

for j in range(1024, len(inp)):
    map = [[0 for a in range(size)] for b in range(size)]

    for i in range(j):
        x, y = [int(u) for u in inp[i].split(',')]
        map[x][y] = 1

    here = [[0, 0]]
    map[0][0]= 2

    steps = 0
    while not([70, 70] in here):
        # print(steps, here)
        steps += 1
        next = []
        for h in here:
            for step in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                iNext = h[0] + step[0]
                jNext = h[1] + step[1]
                if iNext > -1 and jNext > -1 and iNext < 71 and jNext < 71 and map[iNext][jNext] == 0:
                    next.append([iNext, jNext])
                    map[iNext][jNext] = 2
        here = next
        if len(next) == 0:
            print(inp[j-1])
            flag = 1
            break
    
    if flag:
        break

