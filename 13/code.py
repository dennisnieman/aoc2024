file = open('input.txt')
inp = file.readlines()
file.close()

from numpy.linalg import solve

i = 0
spend = 0
while i < len(inp):
    ax = int(inp[i][12:14])
    ay = int(inp[i][18:20])
    bx = int(inp[i+1][12:14])
    by = int(inp[i+1][18:20])
    x = int(inp[i+2][9:inp[i+2].find(',')])
    y = int(inp[i+2][(inp[i+2].find('Y=')+2):])

    j = solve([[ax,bx],[ay,by]], [x,y])
    if abs(j[0] - round(j[0])) + abs(j[1] - round(j[1])) < 1e-4:
        spend += 3*j[0] + j[1]

    i += 4

print(spend)



# part two

i = 0
spend = 0
while i < len(inp):
    ax = int(inp[i][12:14])
    ay = int(inp[i][18:20])
    bx = int(inp[i+1][12:14])
    by = int(inp[i+1][18:20])
    x = int(inp[i+2][9:inp[i+2].find(',')])
    y = int(inp[i+2][(inp[i+2].find('Y=')+2):])

    j = solve([[ax,bx],[ay,by]], [1e13 + x, 1e13 + y])
    if abs(j[0] - round(j[0])) + abs(j[1] - round(j[1])) < 1e-4:
        spend += 3*j[0] + j[1]
        
    i += 4

print(spend)

