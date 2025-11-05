from os import chdir
chdir('/Users/dennisnieman/Documents/python projects/aoc2024/10')

file = open('input.txt')
inp = file.readlines()
file.close()

w = len(inp)

out = 0

def climb(h, i, j, hist):
    global out
    hist[i][j] = 0
    if h == 9:
        out += 1
    else:
        if i>0 and inp[i-1][j] == str(h+1) and hist[i-1][j]:
            climb(h+1, i-1, j, hist)
        if i<w-1 and inp[i+1][j] == str(h+1) and hist[i+1][j]:
            climb(h+1, i+1, j, hist)
        if j>0 and inp[i][j-1] == str(h+1) and hist[i][j-1]:
            climb(h+1, i, j-1, hist)
        if j<w-1 and inp[i][j+1] == str(h+1) and hist[i][j+1]:
            climb(h+1, i, j+1, hist)

for i in range(w):
    for j in range(w):
        if inp[i][j] == '0':
            climb(0, i, j, [w * [1] for x in range(w)])

print(out)


# part two

out = 0

def climb2(h, i, j):
    global out
    if h == 9:
        out += 1
    else:
        if i>0 and inp[i-1][j] == str(h+1):
            climb2(h+1, i-1, j)
        if i<w-1 and inp[i+1][j] == str(h+1):
            climb2(h+1, i+1, j)
        if j>0 and inp[i][j-1] == str(h+1):
            climb2(h+1, i, j-1)
        if j<w-1 and inp[i][j+1] == str(h+1):
            climb2(h+1, i, j+1)

for i in range(w):
    for j in range(w):
        if inp[i][j] == '0':
            climb2(0, i, j)

print(out)

