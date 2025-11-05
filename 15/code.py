from os import chdir
chdir('/Users/dennisnieman/Documents/python projects/aoc2024/15')

file = open('input.txt')
inp = file.readlines()
file.close()

from numpy import array

h = 50
map = [[inp[i][j] for j in range(h)] for i in range(h)]
robot = array([24, 24])

for i in inp[h+1:]:
    for d in i[:70]:
        dir = array([[-1,0], [0,-1], [1,0], [0,1]])[['^', '<', 'v', '>'].index(d)]
        next = robot + dir
        if map[next[0]][next[1]] == '.':
            map[robot[0]][robot[1]] = '.'
            robot = next
            map[robot[0]][robot[1]] = '@'
        else:
            while map[next[0]][next[1]] == 'O':
                next += dir
            if map[next[0]][next[1]] == '.':
                map[robot[0]][robot[1]] = '.'
                robot = robot + dir
                map[robot[0]][robot[1]] = '@'
                map[next[0]][next[1]] = 'O'

out = 0
for i in range(len(map)):
    for j in range(len(map)):
        out += (map[i][j] == 'O') * (j + 100*i)
print(out)


# part two

map = [['.' for j in range(2*h)] for i in range(h)]
for i in range(h):
    for j in range(h):
        if inp[i][j] == '#':
            map[i][2*j] = '#'
            map[i][2*j+1] = '#'
        elif inp[i][j] == '@':
            map[i][2*j] = '@'
            robot = array([i, 2*j])
        elif inp[i][j] == 'O':
            map[i][2*j] = '['
            map[i][2*j+1] = ']'

for i in inp[h+1:]:
    for d in i[:1000]:
        dir = array([[-1,0], [0,-1], [1,0], [0,1]])[['^', '<', 'v', '>'].index(d)]
        if not(dir[0]):
            next = robot + dir
            while map[next[0]][next[1]] in ['[', ']']:
                next += 2 * dir
            if map[next[0]][next[1]] == '.':
                while not(all(next == robot)):
                    map[next[0]][next[1]], map[next[0]][next[1]-dir[1]] = map[next[0]][next[1]-dir[1]], map[next[0]][next[1]]
                    next -= dir
                robot = robot + dir
        else:
            nextList = [robot + dir]
            boxList = []
            wallFlag = 0
            while len(nextList) > 0 and wallFlag == 0:
                boxes = []
                for next in nextList:
                    if map[next[0]][next[1]] == '[':
                        boxes.append(array([next[0],next[1]]))
                    elif map[next[0]][next[1]] == ']':
                        boxes.append(array([next[0],next[1]-1]))
                    elif map[next[0]][next[1]] == '#':
                        wallFlag = 1
                nextList = [b + dir for b in boxes] + [b + dir + array([0,1]) for b in boxes]
                boxList = boxList + boxes
            if not(wallFlag):
                for b in boxList:
                    map[b[0]][b[1]] = '.'
                    map[b[0]][b[1]+1] = '.'
                for b in boxList:
                    map[b[0]+dir[0]][b[1]] = '['
                    map[b[0]+dir[0]][b[1]+1] = ']'
                
                map[robot[0]][robot[1]] = '.'
                robot = robot + dir
                map[robot[0]][robot[1]] = '@'

out = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        out += (map[i][j] == '[') * (j + 100*i)
print(out)
