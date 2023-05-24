#part 1
#https://docs.python.org/3/library/json.html
#referred to AOC reddit pages

import json
que=[]

with open('day13.txt') as file:
    day13_data = file.readlines()
    for index in range(len(pack)//3+1):
        que.append([json.loads(day13_data[index*3]), json.loads(day13_data[index*3+1])])

def order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left > right:
            return False
        return None
    elif isinstance(left, list) and isinstance(right, list):
        for index in range(len(left)):
            if index == len(right):
                return False
            ord = order(left[index], right[index])
            if ord != None:
                return ord
        if len(left) == len(right):
            return None
        return True
    if isinstance(right, int):
        return order(left, [right])
    else:
        return order([left], right)

full = 0

for index in range(len(que)):
    a = order(que[index][0], que[index][1])
    if a == True:
        #print(index+1, ':', a)
        full += (index +1)

print(full)

#part 2
#https://docs.python.org/3/library/functools.html
from functools import cmp_to_key

with open('day13.txt', 'r') as file:
    day13_data = file.read().split('\n\n')

a = lambda x:isinstance(x, int)
b = lambda x:isinstance(x, list)

def cmp(left, right):
    if a(left) and a(right): 
        if left < right: return -1
        return left > right
    if b(left) and b(right):
        for ii in range(min(len(left), len(right))):
            c = cmp(left[ii], right[ii])
            if c: return c
        return cmp(len(left), len(right))
    if a(left) and b(right):
        return cmp([left], right)
    if b(left) and a(right):
        return cmp(left, [right])
c = [] 
n = 0 

for ii, ss in enumerate(day13_data):
    left, right = [eval(x) for x in ss.split()]  
    if cmp(left, right) <= 0: n += ii + 1
    c.append(left); c.append(right)

c.append([[2]]); c.append([[6]])
c.sort(key = cmp_to_key(cmp))

print((c.index([[2]]) + 1) * (c.index([[6]]) + 1) )
