
file = open('input.txt')
inp = file.readlines()
file.close()

h = len(inp)
inp = [[x[:h][j] for j in range(h)] for x in inp]

dirs = array([[-1,0], [0,1], [1,0], [0,-1]])
d = 0
loc = array([45, 42])

while True:
    newLoc = loc + dirs[d]
    if newLoc[0] < 0 or newLoc[0] == h or newLoc[1] < 0 or newLoc[1] == h:
        inp[loc[0]][loc[1]] = 'X'
        break
    else:
        if inp[newLoc[0]][newLoc[1]] == '#':
            d = (d+1) % 4
        else:
            inp[loc[0]][loc[1]] = 'X'
            loc = newLoc

print(sum(i.count('X') for i in inp))


# part 2

h = len(inp)

count = 0
for i in range(h):
    for j in range(h):
        file = open('input.txt')
        inp = file.readlines()
        file.close()
        inp = [[x[:h][j] for j in range(h)] for x in inp]
        if inp[i][j] == '.':
            inp[i][j] = '#'
            d = 0
            loc = array([45, 42])
            steps = 0
            while True:
                steps += 1
                newLoc = loc + dirs[d]
                if newLoc[0] < 0 or newLoc[0] == h or newLoc[1] < 0 or newLoc[1] == h:
                    inp[loc[0]][loc[1]] = 'X'
                    break
                else:
                    if steps >= h*h: #lazy solution to find loop
                        count += 1
                        break
                    elif inp[newLoc[0]][newLoc[1]] == '#':
                        d = (d+1) % 4
                    else:
                        inp[loc[0]][loc[1]] = 'X'
                        loc = newLoc
print(count)