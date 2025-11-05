from os import chdir
chdir('/Users/dennisnieman/Documents/python projects/aoc2024/8')

from numpy import array

file = open('input.txt')
inp = file.readlines()
file.close()


antennaNames = list(set(x for x in ''.join(inp) if not(x=='.' or x=='\n')))

h = len(inp)
antinodeMap = [[0 for j in range(h)] for i in range(h)]

for aN in antennaNames:
    coordList = []
    for i in range(h):
        loc = 0
        for j in range(inp[i].count(aN)):
            loc = inp[i].find(aN, loc)
            coordList.append(array([i, loc]))

    for x in range(len(coordList)):
        for y in range(x+1, len(coordList)):
            cX = coordList[x]
            cY = coordList[y]
            diff = cX - cY

            coords = cX + diff
            if all(coords >= 0) and all(coords < h):
                antinodeMap[coords[0]][coords[1]] = 1

            coords = cY - diff
            if all(coords >= 0) and all(coords < h):
                antinodeMap[coords[0]][coords[1]] = 1

print(sum(sum(x) for x in antinodeMap))



# part two

antinodeMap = [[0 for j in range(h)] for i in range(h)]

for aN in antennaNames:
    coordList = []
    for i in range(h):
        loc = 0
        for j in range(inp[i].count(aN)):
            loc = inp[i].find(aN, loc)
            coordList.append(array([i, loc]))

    for x in range(len(coordList)):
        for y in range(x+1, len(coordList)):
            cX = coordList[x]
            cY = coordList[y]
            diff = cX - cY

            k = 0
            coords = cX + k*diff
            while all(coords >= 0) and all(coords < h):
                antinodeMap[coords[0]][coords[1]] = 1
                k += 1
                coords = cX + k*diff
            
            k = 0
            coords = cY - k*diff
            while all(coords >= 0) and all(coords < h):
                antinodeMap[coords[0]][coords[1]] = 1
                k += 1
                coords = cY - k*diff

print(sum(sum(x) for x in antinodeMap))