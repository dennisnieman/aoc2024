file = open('input.txt')
inp = file.readlines()
file.close()

nFiles = round((len(inp[0])+1)/2)
sizes = [int(inp[0][2*i]) for i in range(nFiles)]
spaces = [int(inp[0][2*i+1]) for i in range(nFiles-1)]

totalSpace = sum(sizes)

disk = sizes[0] * [0] # visual representation of disk
i = 0 # index of gap being filled
file = nFiles-1 # file currently being MOVED
fileSize = sizes[file] # its remaining size
spaceSize = spaces[i] # size of gap

while len(disk) < totalSpace:
    if fileSize >= spaceSize:
        disk += spaceSize * [file]
        fileSize -= spaceSize
        i = i + 1
        disk += sizes[i] * [i]
        spaceSize = spaces[i]
    else: #fileSize < spaceSize
        disk += fileSize * [file]
        spaceSize -= fileSize
        file = file - 1
        fileSize = sizes[file]

print(sum([i * disk[i] for i in range(totalSpace)]))


# part two

sizes = [int(inp[0][2*i]) for i in range(nFiles)]
spaces = [int(inp[0][2*i+1]) for i in range(nFiles-1)]

disk = sizes[0] * [0]
for i in range(nFiles-1):
    disk += spaces[i] * ['.'] + sizes[i+1] * [i+1]

for file in reversed(range(nFiles)):
    oldPos = disk.index(file)
    i = disk.index('.')
    while (i < oldPos):
        if all(disk[i+j] == '.' for j in range(sizes[file])):
            for j in range(sizes[file]):
                disk[i+j] = file
                disk[oldPos+j] = '.'
            break
        else:
            i += 1

for i in range(len(disk)):
    if disk[i] == '.': disk[i] = 0
print(sum([i * disk[i] for i in range(len(disk))]))


