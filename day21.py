#referred to AOC reddit pages

#part 1

with open('day21.txt', 'rt') as file:
    day21_data=file.readlines()

monkeys_dict={}

for data in day21_data:
    monkeys_dict[data.split(':')[0]]=data.split(':')[1]

num_monkeys={}
non_num={}
for key,value in monkeys_dict.items():
    val_split=value.split()
    if len(val_split)==1:
        num_monkeys[key]=int(value)
    else:
        non_num[key]=value

def yell_calulation(monkey, non_num, num_monkeys):
    
    calc = non_num[monkey].strip().split()
    monkey1,op, monkey2 = calc[0],calc[1], calc[2] 
    
    if monkey2 not in num_monkeys:
        yell_calulation(monkey2, non_num, num_monkeys)
    if monkey1 not in num_monkeys:
        yell_calulation(monkey1, non_num, num_monkeys)
    
    if op=='+':
        num_monkeys[monkey] = num_monkeys[monkey1]+num_monkeys[monkey2]
    elif op=='-':
        num_monkeys[monkey] = num_monkeys[monkey1]-num_monkeys[monkey2]
    elif op=='*':
        num_monkeys[monkey] = num_monkeys[monkey1]*num_monkeys[monkey2]
    elif op=='/':
        num_monkeys[monkey] = num_monkeys[monkey1]/num_monkeys[monkey2]
        
    return num_monkeys[monkey]

print(int(yell_calulation('root',non_num, num_monkeys)))

#part 2
#https://docs.python.org/3/library/re.html
#https://z3prover.github.io/api/html/z3.html

import re
from z3 import *

part2list=[]
for line in day21_data:
    part2list.append(line.split(':'))

sol = Solver()
dic = {equ[0]: Int(equ[0]) for equ in part2list}

for p1, p2 in part2list:
    if p1 == "root":
        m1, _, m2 = p2.split()
        sol.add(dic[m1] == dic[m2])
        continue
    if p1 == "humn":
        continue
    
    if re.findall("\d+", p2):
        sol.add(dic[p1] == int(re.findall("\d+", p2)[0]))
    else:
        m1, op, m2 = p2.split()
        if op== "+":
            sol.add(dic[p1] == dic[m1] + dic[m2])
        elif op== "-":
            sol.add(dic[p1] == dic[m1] - dic[m2])
        elif op== "*":
            sol.add(dic[p1] == dic[m1] * dic[m2])
        elif op== "/":
            sol.add(dic[p1] == dic[m1] / dic[m2])
            sol.add(dic[m1] % dic[m2] == 0)

sol.check()
print(sol.model().eval(dic['humn']))


