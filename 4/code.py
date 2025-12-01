
file = open('input.txt')
inp = file.readlines()
file.close()



count = 0

# east
count += sum(i.count('XMAS') for i in inp)

# west
count += sum(i[::-1].count('XMAS') for i in inp)

# south
inpt = np.array([list(i[:140]) for i in inp]).T
count += sum(''.join(i).count('XMAS') for i in inpt)

# north
count += sum(''.join(i[::-1]).count('XMAS') for i in inpt)

# south east
h = len(inp)
stringList = [''.join([inp[i][i] for i in range(h)])]
for u in range(1, h):
    stringList.append(''.join(inp[i][i+u] for i in range(h-u)))
    stringList.append(''.join(inp[i+u][i] for i in range(h-u)))
count += sum(i.count('XMAS') for i in stringList)

# north west
count += sum(i[::-1].count('XMAS') for i in stringList)

# north east
h = len(inp)
stringList = [''.join([inp[h-1-i][i] for i in range(h)])]
for u in range(1, h):
    stringList.append(''.join(inp[h-1-i-u][i] for i in range(h-u)))
    stringList.append(''.join(inp[h-1-i][i+u] for i in range(h-u)))
count += sum(i.count('XMAS') for i in stringList)

# south west
count += sum(i[::-1].count('XMAS') for i in stringList)
print(count)




# part 2

count = 0

for i in range(1, h-1):
    for j in range(1, h-1):
        x = 0
        if inp[i][j] == 'A':
            if inp[i-1][j-1]+inp[i+1][j+1] in ['MS', 'SM']:
                if inp[i+1][j-1]+inp[i-1][j+1] in ['MS', 'SM']:
                    count += 1
print(count)