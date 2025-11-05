from os import chdir
chdir('/Users/dennisnieman/Documents/python projects/aoc2024/7')

file = open('input.txt')
inp = file.readlines()
file.close()



def insOp(testVal, nrs, curVal):
    # inserts operators + and * between items in nrs and checks if end result equals testVal
    if len(nrs) == 0:
        return (testVal == curVal)
    else:
        return insOp(testVal, nrs[1:], curVal+nrs[0]) or insOp(testVal, nrs[1:], curVal*nrs[0])

count = 0
for i in inp:
    l = i.find(':')
    testValue = int(i[:l])
    numbers = [int(x) for x in i.split()[1:]]
    if insOp(testValue, numbers[1:], numbers[0]):
        count += testValue
print(count)


# part two

def insOp(testVal, nrs, curVal):
    # inserts operators +, *, || between items in nrs and checks if end result equals testVal
    if len(nrs) == 0:
        return (testVal == curVal)
    else:
        return (insOp(testVal, nrs[1:], curVal+nrs[0]) or
                insOp(testVal, nrs[1:], curVal*nrs[0]) or
                insOp(testVal, nrs[1:], int(str(curVal)+str(nrs[0]))))

count = 0
for i in inp:
    l = i.find(':')
    testValue = int(i[:l])
    numbers = [int(x) for x in i.split()[1:]]
    if insOp(testValue, numbers[1:], numbers[0]):
        count += testValue
print(count)
