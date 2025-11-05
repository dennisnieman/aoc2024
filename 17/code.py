from os import chdir
chdir('/Users/dennisnieman/Documents/python projects/aoc2024/17')

file = open('input.txt')
inp = file.readlines()
file.close()




registers = [int(inp[j][12:]) for j in range(3)]

program = [int(x) for x in inp[4][9:].split(',')]

combo = lambda n: (n<4) * n + (n>3) * registers[n-4]

out = [] 
i = 0
while (i < len(program)):
    opcode = program[i]
    operand = program[i+1]

    if opcode == 0:
        registers[0] = int(registers[0] / 2**combo(operand))
    elif opcode == 1:
        registers[1] = operand ^ registers[1]
    elif opcode == 2:
        registers[1] = combo(operand) % 8
    elif opcode == 3 and registers[0] != 0:
        i = operand - 2
    elif opcode == 4:
        registers[1] = registers[1] ^ registers[2]
    elif opcode == 5:
        out.append(combo(operand) % 8)
    elif opcode == 6:
        registers[1] = int(registers[0] / 2**combo(operand))
    elif opcode == 7:
        registers[2] = int(registers[0] / 2**combo(operand))

    i += 2

print(','.join(str(j) for j in out))


# part two

def f(j):
    registers = [j, 0, 0]
    program = [int(x) for x in inp[4][9:].split(',')]

    combo = lambda n: (n<4) * n + (n>3) * registers[n-4]

    out = [] 
    i = 0
    while (i < len(program)):
        opcode = program[i]
        operand = program[i+1]

        if opcode == 0:
            registers[0] = int(registers[0] / 2**combo(operand))
        elif opcode == 1:
            registers[1] = operand ^ registers[1]
        elif opcode == 2:
            registers[1] = combo(operand) % 8
        elif opcode == 3 and registers[0] != 0:
            i = operand - 2
        elif opcode == 4:
            registers[1] = registers[1] ^ registers[2]
        elif opcode == 5:
            out.append(combo(operand) % 8)
        elif opcode == 6:
            registers[1] = int(registers[0] / 2**combo(operand))
        elif opcode == 7:
            registers[2] = int(registers[0] / 2**combo(operand))

        i += 2
    return(out)

# [5, 6, 0, 0, 6, 4, 4, 6]
baseEight = [[5]]
for a in reversed(range(15)):
    new = []
    for x in baseEight:
        baseTen = sum(x[j] * 8 ** (15-j) for j in range(len(x)))
        for b in range(8):
            if f(baseTen + b * 8**a)[a] == program[a]:
                new.append(x + [b])
    baseEight = new

x = sorted(baseEight)[0]
baseTen = sum(x[j] * 8 ** (15-j) for j in range(len(x)))
