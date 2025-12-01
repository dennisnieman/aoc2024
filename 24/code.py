with open('input.txt') as file:
   inp = file.read().splitlines() 

gap = min([u for u, x in enumerate(inp) if x == ''])
values = dict([i.split(': ') for i in inp[:gap]])
gates = [g.split(' ') for g in inp[gap+1:]]

while len(gates) > 0:
   for g in gates:
      if g[0] in values and g[2] in values:
         x, y = int(values[g[0]]), int(values[g[2]])
         if g[1] == 'AND':
            values[g[4]] = str(x and y)
         elif g[1] == 'OR':
            values[g[4]] = str(x or y) 
         elif g[1] == 'XOR':
            values[g[4]] = str(x ^ y)
         gates.remove(g)

sValues = sorted(values)
zCount = int(sValues[-1][1:])+1
print(int(''.join(reversed([values[x] for x in sValues[-zCount:]])), 2))

# part 2

numbers = ['0' + str(j) for j in range(10)] + [str(j) for j in range(10,46)]

gates = [g.split(' ') for g in inp[gap+1:]]
hist = {}

def machine(inx, iny, out):
   global hist
   if out[0] == 'x':
      return int(inx[-1-int(out[1:])])
   elif out[0] == 'y':
      return int(iny[-1-int(out[1:])])
   elif out in hist:
      return int(hist[out])
   else:
      i = [u for u, gate in enumerate(gates) if gate[4] == out][0]
      gate = gates[i]
      if gate[1] == 'AND':
         m = (machine(inx, iny, gate[0]) and machine(inx, iny, gate[2]))
         hist[out] = m
         return m
      elif gate[1] == 'OR':
         m = (machine(inx, iny, gate[0]) or machine(inx, iny, gate[2]))
         hist[out] = m
         return m
      elif gate[1] == 'XOR':
         m = (machine(inx, iny, gate[0]) ^ machine(inx, iny, gate[2]))
         hist[out] = m
         return m


gates = [g.split(' ') for g in inp[gap+1:]]

i = [u for u, gate in enumerate(gates) if gate[4] == 'z06'][0]
j = [u for u, gate in enumerate(gates) if gate[4] == 'hwk'][0]

gates[i][4], gates[j][4] = gates[j][4], gates[i][4]

i = [u for u, gate in enumerate(gates) if gate[4] == 'qmd'][0]
j = [u for u, gate in enumerate(gates) if gate[4] == 'tnt'][0]

gates[i][4], gates[j][4] = gates[j][4], gates[i][4]

i = [u for u, gate in enumerate(gates) if gate[4] == 'hpc'][0]
j = [u for u, gate in enumerate(gates) if gate[4] == 'z31'][0]

gates[i][4], gates[j][4] = gates[j][4], gates[i][4]

i = [u for u, gate in enumerate(gates) if gate[4] == 'cgr'][0]
j = [u for u, gate in enumerate(gates) if gate[4] == 'z37'][0]

gates[i][4], gates[j][4] = gates[j][4], gates[i][4]

# cgr,hpc,hwk,qmd,tnt,z06,z31,z37