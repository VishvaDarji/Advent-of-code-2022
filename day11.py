#part1
#https://docs.python.org/3/library/operator.html
#referred to AOC reddit pages

import operator

r = 20
m = 8
th = 3
que = []
ops = { '+' : operator.add, '*' : operator.mul }
touch = [0] * m
def Pro(num, op):
    left = num if op[0] == 'old' else int(op[0])
    right = num if op[2] == 'old' else int(op[2])
    return ops[op[1]](left, right) // th


with open('day11.txt') as file:
    for i in range(m):
        num = int(file.readline().split()[1][0])
        items = [int(y) for y in [x.split(', ') for x in file.readline().strip().split(':')][1]]
        op = file.readline().split()[3:]
        d = int(file.readline().split()[3])
        t = int(file.readline().split()[5])
        f = int(file.readline().split()[5])
        div = [d,t,f]
        m = [items, op, div]
        que.append([items, op, div])
        file.readline()

for round in range(r):
    for index in range(len(que)):
        m = que[index]
        for item in m[0]:
            touch[index] +=1
            val = Pro(item, m[1])
            if val % m[2][0] == 0:
                que[m[2][1]][0].append(val)
            else:
                que[m[2][2]][0].append(val)
        m[0].clear()

touch = sorted(touch, reverse = True)

print(touch[0] * touch[1])

import operator
r = 10000
m = 8
th = 1
que = []
ops = { '+' : operator.add, '*' : operator.mul }
touch = [0] * m

def Pro(num, op):
    left = num if op[0] == 'old' else int(op[0])
    right = num if op[2] == 'old' else int(op[2])
    return ops[op[1]](left, right) // th

with open('day11.txt') as file:
    for i in range(m):
        num = int(file.readline().split()[1][0])
        items = [int(y) for y in [x.split(', ') for x in file.readline().strip().split(':')][1]]
        op = file.readline().split()[3:]
        d = int(file.readline().split()[3])
        t = int(file.readline().split()[5])
        f = int(file.readline().split()[5])
        div = [d,t,f]
        m = [items, op, div]
        que.append([items, op, div])
        file.readline()

modulus = 1
for m in que:
    modulus *= m[2][0]
for round in range(r):
    for index in range(len(que)):
        m = que[index]
        for item in m[0]:
            touch[index] +=1
            val = Pro(item, m[1])
            if val % m[2][0] == 0:
                que[m[2][1]][0].append(val % modulus)
            else:
                que[m[2][2]][0].append(val % modulus)
        m[0].clear()
touch = sorted(touch, reverse = True)
print(touch[0] * touch[1])
