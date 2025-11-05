from os import chdir
chdir('/Users/dennisnieman/Documents/python projects/aoc2024/12')

file = open('input.txt')
inp = file.readlines()
file.close()

h = len(inp)
seen = [h * [0] for x in range(h)]

def mapping(i, j):
    global inp, seen, perimeter, area
    seen[i][j] = 1
    area += 1
    for x, y in [[i-1, j], [i, j-1], [i+1, j], [i, j+1]]:
        if x >= 0 and x < h and y >= 0 and y < h:
            if inp[i][j] == inp[x][y] and not(seen[x][y]):
                mapping(x, y)
            elif not(inp[i][j] == inp[x][y]):
                perimeter += 1
        else:
            perimeter += 1

cost = 0

for i in range(h):
    for j in range(h):
        if not(seen[i][j]):
            perimeter = 0
            area = 0
            mapping(i, j)
            cost += perimeter * area

print(cost)


# part two

def makeMap(i, j):
    global inp, map, seen
    map[i][j] = 1
    seen[i][j] = 1
    for x, y in [[i-1, j], [i, j-1], [i+1, j], [i, j+1]]:
        if x >= 0 and x < h and y >= 0 and y < h:
            if inp[i][j] == inp[x][y] and not(seen[x][y]):
                makeMap(x, y)

def buildFence(map):
    global fence
    for i in range(h):
        for j in range(h):
            if map[i][j] == 1:
                if i == 0 or map[i-1][j] == 0:
                    fence[i][j][0] = 1
                if j == 0 or map[i][j-1] == 0:
                    fence[i][j][1] = 1
                if i == h-1 or map[i+1][j] == 0:
                    fence[i][j][2] = 1
                if j == h-1 or map[i][j+1] == 0:
                    fence[i][j][3] = 1

seen = [h * [0] for x in range(h)]
cost = 0

for i in range(h):
    for j in range(h):
        if not(seen[i][j]):
            map = [h * [0] for x in range(h)]
            makeMap(i, j)
            area = sum(sum(map[i][j] for j in range(h)) for i in range(h))

            fence = [[[0, 0, 0, 0] for x in range(h)] for y in range(h)]
            buildFence(map)
            noFences = 0
            for k in range(h):
                fences = [fence[k][l][0] for l in range(h)]
                switches = sum(not(fences[j+1]==fences[j]) for j in range(h-1))
                if switches % 2 == 0:
                    noFences += switches/2 + fences[0]
                else:
                    noFences += (switches+1)/2
                fences = [fence[l][k][1] for l in range(h)]
                switches = sum(not(fences[j+1]==fences[j]) for j in range(h-1))
                if switches % 2 == 0:
                    noFences += switches/2 + fences[0]
                else:
                    noFences += (switches+1)/2
                fences = [fence[k][l][2] for l in range(h)]
                switches = sum(not(fences[j+1]==fences[j]) for j in range(h-1))
                if switches % 2 == 0:
                    noFences += switches/2 + fences[0]
                else:
                    noFences += (switches+1)/2
                fences = [fence[l][k][3] for l in range(h)]
                switches = sum(not(fences[j+1]==fences[j]) for j in range(h-1))
                if switches % 2 == 0:
                    noFences += switches/2 + fences[0]
                else:
                    noFences += (switches+1)/2
            cost += area * noFences

print(cost)