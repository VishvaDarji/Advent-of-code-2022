#part a
import re

with open('day05.txt', 'rt') as file:
    day5_data=file.readlines()
instructions=[]
stacks=[]
for data in day5_data:
    if data.startswith('move'):
        instructions.append(data.split('\n')[0])
    else:
        stacks.append(data)
stacks.remove('\n')
num_instructions=[]
for line in instructions:
    split_line=line.split()
    split_line.remove('move')
    split_line.remove('from')
    split_line.remove('to')
    num_instructions.append(split_line)

stacks=stacks[::-1]
pattern = re.compile(r"[A-Z]")

stacks_len = len(stacks[0].split())
stack_width = 4
new_stacks = [[i+1] for i in range(stacks_len)] 

for line in stacks[1:]:    
    for n_stacks in range(stacks_len):
        match = pattern.search(line[n_stacks * stack_width:(n_stacks+1) * stack_width])
        if match:
            new_stacks[n_stacks].append(match.group())

from copy import deepcopy
stacks1 = deepcopy(new_stacks) 

for i in range(len(num_instructions)):
    if int(num_instructions[i][1]) in new_stacks[0]:
        for j in range(int(num_instructions[i][0])):
            item=new_stacks[0].pop()
            if int(num_instructions[i][2]) in new_stacks[0]:
                new_stacks[0].append(item)
            elif int(num_instructions[i][2]) in new_stacks[1]:
                new_stacks[1].append(item)
            elif int(num_instructions[i][2]) in new_stacks[2]:
                new_stacks[2].append(item)
            elif int(num_instructions[i][2]) in new_stacks[3]:
                new_stacks[3].append(item)
            elif int(num_instructions[i][2]) in new_stacks[4]:
                new_stacks[4].append(item)
            elif int(num_instructions[i][2]) in new_stacks[5]:
                new_stacks[5].append(item)
            elif int(num_instructions[i][2]) in new_stacks[6]:
                new_stacks[6].append(item)
            elif int(num_instructions[i][2]) in new_stacks[7]:
                new_stacks[7].append(item)
            elif int(num_instructions[i][2]) in new_stacks[8]:
                new_stacks[8].append(item)

    elif int(num_instructions[i][1]) in new_stacks[1]:
        for j in range(int(num_instructions[i][0])):
            item=new_stacks[1].pop()
            if int(num_instructions[i][2]) in new_stacks[0]:
                new_stacks[0].append(item)
            elif int(num_instructions[i][2]) in new_stacks[1]:
                new_stacks[1].append(item)
            elif int(num_instructions[i][2]) in new_stacks[2]:
                new_stacks[2].append(item)
            elif int(num_instructions[i][2]) in new_stacks[3]:
                new_stacks[3].append(item)
            elif int(num_instructions[i][2]) in new_stacks[4]:
                new_stacks[4].append(item)
            elif int(num_instructions[i][2]) in new_stacks[5]:
                new_stacks[5].append(item)
            elif int(num_instructions[i][2]) in new_stacks[6]:
                new_stacks[6].append(item)
            elif int(num_instructions[i][2]) in new_stacks[7]:
                new_stacks[7].append(item)
            elif int(num_instructions[i][2]) in new_stacks[8]:
                new_stacks[8].append(item)
    elif int(num_instructions[i][1]) in new_stacks[2]:
        for j in range(int(num_instructions[i][0])):
            item=new_stacks[2].pop()
            if int(num_instructions[i][2]) in new_stacks[0]:
                new_stacks[0].append(item)
            elif int(num_instructions[i][2]) in new_stacks[1]:
                new_stacks[1].append(item)
            elif int(num_instructions[i][2]) in new_stacks[2]:
                new_stacks[2].append(item)
            elif int(num_instructions[i][2]) in new_stacks[3]:
                new_stacks[3].append(item)
            elif int(num_instructions[i][2]) in new_stacks[4]:
                new_stacks[4].append(item)
            elif int(num_instructions[i][2]) in new_stacks[5]:
                new_stacks[5].append(item)
            elif int(num_instructions[i][2]) in new_stacks[6]:
                new_stacks[6].append(item)
            elif int(num_instructions[i][2]) in new_stacks[7]:
                new_stacks[7].append(item)
            elif int(num_instructions[i][2]) in new_stacks[8]:
                new_stacks[8].append(item)
    elif int(num_instructions[i][1]) in new_stacks[3]:
        for j in range(int(num_instructions[i][0])):
            item=new_stacks[3].pop()
            if int(num_instructions[i][2]) in new_stacks[0]:
                new_stacks[0].append(item)
            elif int(num_instructions[i][2]) in new_stacks[1]:
                new_stacks[1].append(item)
            elif int(num_instructions[i][2]) in new_stacks[2]:
                new_stacks[2].append(item)
            elif int(num_instructions[i][2]) in new_stacks[3]:
                new_stacks[3].append(item)
            elif int(num_instructions[i][2]) in new_stacks[4]:
                new_stacks[4].append(item)
            elif int(num_instructions[i][2]) in new_stacks[5]:
                new_stacks[5].append(item)
            elif int(num_instructions[i][2]) in new_stacks[6]:
                new_stacks[6].append(item)
            elif int(num_instructions[i][2]) in new_stacks[7]:
                new_stacks[7].append(item)
            elif int(num_instructions[i][2]) in new_stacks[8]:
                new_stacks[8].append(item)
    elif int(num_instructions[i][1]) in new_stacks[4]:
        for j in range(int(num_instructions[i][0])):
            item=new_stacks[4].pop()
            if int(num_instructions[i][2]) in new_stacks[0]:
                new_stacks[0].append(item)
            elif int(num_instructions[i][2]) in new_stacks[1]:
                new_stacks[1].append(item)
            elif int(num_instructions[i][2]) in new_stacks[2]:
                new_stacks[2].append(item)
            elif int(num_instructions[i][2]) in new_stacks[3]:
                new_stacks[3].append(item)
            elif int(num_instructions[i][2]) in new_stacks[4]:
                new_stacks[4].append(item)
            elif int(num_instructions[i][2]) in new_stacks[5]:
                new_stacks[5].append(item)
            elif int(num_instructions[i][2]) in new_stacks[6]:
                new_stacks[6].append(item)
            elif int(num_instructions[i][2]) in new_stacks[7]:
                new_stacks[7].append(item)
            elif int(num_instructions[i][2]) in new_stacks[8]:
                new_stacks[8].append(item)
    elif int(num_instructions[i][1]) in new_stacks[5]:
        for j in range(int(num_instructions[i][0])):
            item=new_stacks[5].pop()
            if int(num_instructions[i][2]) in new_stacks[0]:
                new_stacks[0].append(item)
            elif int(num_instructions[i][2]) in new_stacks[1]:
                new_stacks[1].append(item)
            elif int(num_instructions[i][2]) in new_stacks[2]:
                new_stacks[2].append(item)
            elif int(num_instructions[i][2]) in new_stacks[3]:
                new_stacks[3].append(item)
            elif int(num_instructions[i][2]) in new_stacks[4]:
                new_stacks[4].append(item)
            elif int(num_instructions[i][2]) in new_stacks[5]:
                new_stacks[5].append(item)
            elif int(num_instructions[i][2]) in new_stacks[6]:
                new_stacks[6].append(item)
            elif int(num_instructions[i][2]) in new_stacks[7]:
                new_stacks[7].append(item)
            elif int(num_instructions[i][2]) in new_stacks[8]:
                new_stacks[8].append(item)
    elif int(num_instructions[i][1]) in new_stacks[6]:
        for j in range(int(num_instructions[i][0])):
            item=new_stacks[6].pop()
            if int(num_instructions[i][2]) in new_stacks[0]:
                new_stacks[0].append(item)
            elif int(num_instructions[i][2]) in new_stacks[1]:
                new_stacks[1].append(item)
            elif int(num_instructions[i][2]) in new_stacks[2]:
                new_stacks[2].append(item)
            elif int(num_instructions[i][2]) in new_stacks[3]:
                new_stacks[3].append(item)
            elif int(num_instructions[i][2]) in new_stacks[4]:
                new_stacks[4].append(item)
            elif int(num_instructions[i][2]) in new_stacks[5]:
                new_stacks[5].append(item)
            elif int(num_instructions[i][2]) in new_stacks[6]:
                new_stacks[6].append(item)
            elif int(num_instructions[i][2]) in new_stacks[7]:
                new_stacks[7].append(item)
            elif int(num_instructions[i][2]) in new_stacks[8]:
                new_stacks[8].append(item)
    elif int(num_instructions[i][1]) in new_stacks[7]:
        for j in range(int(num_instructions[i][0])):
            item=new_stacks[7].pop()
            if int(num_instructions[i][2]) in new_stacks[0]:
                new_stacks[0].append(item)
            elif int(num_instructions[i][2]) in new_stacks[1]:
                new_stacks[1].append(item)
            elif int(num_instructions[i][2]) in new_stacks[2]:
                new_stacks[2].append(item)
            elif int(num_instructions[i][2]) in new_stacks[3]:
                new_stacks[3].append(item)
            elif int(num_instructions[i][2]) in new_stacks[4]:
                new_stacks[4].append(item)
            elif int(num_instructions[i][2]) in new_stacks[5]:
                new_stacks[5].append(item)
            elif int(num_instructions[i][2]) in new_stacks[6]:
                new_stacks[6].append(item)
            elif int(num_instructions[i][2]) in new_stacks[7]:
                new_stacks[7].append(item)
            elif int(num_instructions[i][2]) in new_stacks[8]:
                new_stacks[8].append(item)
    elif int(num_instructions[i][1]) in new_stacks[8]:
        for j in range(int(num_instructions[i][0])):
            item=new_stacks[8].pop()
            if int(num_instructions[i][2]) in new_stacks[0]:
                new_stacks[0].append(item)
            elif int(num_instructions[i][2]) in new_stacks[1]:
                new_stacks[1].append(item)
            elif int(num_instructions[i][2]) in new_stacks[2]:
                new_stacks[2].append(item)
            elif int(num_instructions[i][2]) in new_stacks[3]:
                new_stacks[3].append(item)
            elif int(num_instructions[i][2]) in new_stacks[4]:
                new_stacks[4].append(item)
            elif int(num_instructions[i][2]) in new_stacks[5]:
                new_stacks[5].append(item)
            elif int(num_instructions[i][2]) in new_stacks[6]:
                new_stacks[6].append(item)
            elif int(num_instructions[i][2]) in new_stacks[7]:
                new_stacks[7].append(item)
            elif int(num_instructions[i][2]) in new_stacks[8]:
                new_stacks[8].append(item)

for s in new_stacks:
    print(s[-1],end="")

#part b

stack_dict={}
for i in range(len(stacks1)):
    for j in range(len(stacks1[i])):
        stack_dict[stacks1[i][0]]=stacks1[i][1:]

for i in range(len(num_instructions)):
    if int(num_instructions[i][1]) in new_stacks[0]:
        pop_list=[]
        for j in range(int(num_instructions[i][0])):
            pop_list.append(stack_dict[1].pop())
        pop_list.reverse()
        if int(num_instructions[i][2]) in new_stacks[0]:
            stack_dict.update({1:stack_dict[1]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[1]:
            stack_dict.update({2:stack_dict[2]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[2]:
            stack_dict.update({3:stack_dict[3]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[3]:
            stack_dict.update({4:stack_dict[4]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[4]:
            stack_dict.update({5:stack_dict[5]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[5]:
            stack_dict.update({6:stack_dict[6]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[6]:
            stack_dict.update({7:stack_dict[7]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[7]:
            stack_dict.update({8:stack_dict[8]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[8]:
            stack_dict.update({9:stack_dict[9]+pop_list})
        pop_list.clear()

    elif int(num_instructions[i][1]) in new_stacks[1]:
        pop_list=[]
        for j in range(int(num_instructions[i][0])):
            pop_list.append(stack_dict[2].pop())
        pop_list.reverse()
        if int(num_instructions[i][2]) in new_stacks[0]:
            stack_dict.update({1:stack_dict[1]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[1]:
            stack_dict.update({2:stack_dict[2]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[2]:
            stack_dict.update({3:stack_dict[3]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[3]:
            stack_dict.update({4:stack_dict[4]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[4]:
            stack_dict.update({5:stack_dict[5]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[5]:
            stack_dict.update({6:stack_dict[6]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[6]:
            stack_dict.update({7:stack_dict[7]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[7]:
            stack_dict.update({8:stack_dict[8]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[8]:
            stack_dict.update({9:stack_dict[9]+pop_list})
        pop_list.clear()
        
    elif int(num_instructions[i][1]) in new_stacks[2]:
        pop_list=[]
        for j in range(int(num_instructions[i][0])):
            pop_list.append(stack_dict[3].pop())
        pop_list.reverse()
        if int(num_instructions[i][2]) in new_stacks[0]:
            stack_dict.update({1:stack_dict[1]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[1]:
            stack_dict.update({2:stack_dict[2]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[2]:
            stack_dict.update({3:stack_dict[3]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[3]:
            stack_dict.update({4:stack_dict[4]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[4]:
            stack_dict.update({5:stack_dict[5]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[5]:
            stack_dict.update({6:stack_dict[6]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[6]:
            stack_dict.update({7:stack_dict[7]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[7]:
            stack_dict.update({8:stack_dict[8]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[8]:
            stack_dict.update({9:stack_dict[9]+pop_list})
        pop_list.clear()
        
    elif int(num_instructions[i][1]) in new_stacks[3]:
        pop_list=[]
        for j in range(int(num_instructions[i][0])):
            pop_list.append(stack_dict[4].pop())
        pop_list.reverse()
        if int(num_instructions[i][2]) in new_stacks[0]:
            stack_dict.update({1:stack_dict[1]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[1]:
            stack_dict.update({2:stack_dict[2]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[2]:
            stack_dict.update({3:stack_dict[3]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[3]:
            stack_dict.update({4:stack_dict[4]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[4]:
            stack_dict.update({5:stack_dict[5]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[5]:
            stack_dict.update({6:stack_dict[6]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[6]:
            stack_dict.update({7:stack_dict[7]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[7]:
            stack_dict.update({8:stack_dict[8]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[8]:
            stack_dict.update({9:stack_dict[9]+pop_list})
        pop_list.clear()
        
    elif int(num_instructions[i][1]) in new_stacks[4]:
        pop_list=[]
        for j in range(int(num_instructions[i][0])):
            pop_list.append(stack_dict[5].pop())
        pop_list.reverse()
        if int(num_instructions[i][2]) in new_stacks[0]:
            stack_dict.update({1:stack_dict[1]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[1]:
            stack_dict.update({2:stack_dict[2]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[2]:
            stack_dict.update({3:stack_dict[3]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[3]:
            stack_dict.update({4:stack_dict[4]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[4]:
            stack_dict.update({5:stack_dict[5]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[5]:
            stack_dict.update({6:stack_dict[6]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[6]:
            stack_dict.update({7:stack_dict[7]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[7]:
            stack_dict.update({8:stack_dict[8]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[8]:
            stack_dict.update({9:stack_dict[9]+pop_list})
        pop_list.clear()
        
    elif int(num_instructions[i][1]) in new_stacks[5]:
        pop_list=[]
        for j in range(int(num_instructions[i][0])):
            pop_list.append(stack_dict[6].pop())
        pop_list.reverse()
        if int(num_instructions[i][2]) in new_stacks[0]:
            stack_dict.update({1:stack_dict[1]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[1]:
            stack_dict.update({2:stack_dict[2]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[2]:
            stack_dict.update({3:stack_dict[3]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[3]:
            stack_dict.update({4:stack_dict[4]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[4]:
            stack_dict.update({5:stack_dict[5]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[5]:
            stack_dict.update({6:stack_dict[6]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[6]:
            stack_dict.update({7:stack_dict[7]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[7]:
            stack_dict.update({8:stack_dict[8]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[8]:
            stack_dict.update({9:stack_dict[9]+pop_list})
        pop_list.clear()
        
    elif int(num_instructions[i][1]) in new_stacks[6]:
        pop_list=[]
        for j in range(int(num_instructions[i][0])):
            pop_list.append(stack_dict[7].pop())
        pop_list.reverse()
        if int(num_instructions[i][2]) in new_stacks[0]:
            stack_dict.update({1:stack_dict[1]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[1]:
            stack_dict.update({2:stack_dict[2]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[2]:
            stack_dict.update({3:stack_dict[3]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[3]:
            stack_dict.update({4:stack_dict[4]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[4]:
            stack_dict.update({5:stack_dict[5]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[5]:
            stack_dict.update({6:stack_dict[6]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[6]:
            stack_dict.update({7:stack_dict[7]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[7]:
            stack_dict.update({8:stack_dict[8]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[8]:
            stack_dict.update({9:stack_dict[9]+pop_list})
        pop_list.clear()
        
    elif int(num_instructions[i][1]) in new_stacks[7]:
        pop_list=[]
        for j in range(int(num_instructions[i][0])):
            pop_list.append(stack_dict[8].pop())
        pop_list.reverse()
        if int(num_instructions[i][2]) in new_stacks[0]:
            stack_dict.update({1:stack_dict[1]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[1]:
            stack_dict.update({2:stack_dict[2]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[2]:
            stack_dict.update({3:stack_dict[3]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[3]:
            stack_dict.update({4:stack_dict[4]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[4]:
            stack_dict.update({5:stack_dict[5]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[5]:
            stack_dict.update({6:stack_dict[6]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[6]:
            stack_dict.update({7:stack_dict[7]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[7]:
            stack_dict.update({8:stack_dict[8]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[8]:
            stack_dict.update({9:stack_dict[9]+pop_list})
        pop_list.clear()
        
    elif int(num_instructions[i][1]) in new_stacks[8]:
        pop_list=[]
        for j in range(int(num_instructions[i][0])):
            pop_list.append(stack_dict[9].pop())
        pop_list.reverse()
        if int(num_instructions[i][2]) in new_stacks[0]:
            stack_dict.update({1:stack_dict[1]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[1]:
            stack_dict.update({2:stack_dict[2]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[2]:
            stack_dict.update({3:stack_dict[3]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[3]:
            stack_dict.update({4:stack_dict[4]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[4]:
            stack_dict.update({5:stack_dict[5]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[5]:
            stack_dict.update({6:stack_dict[6]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[6]:
            stack_dict.update({7:stack_dict[7]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[7]:
            stack_dict.update({8:stack_dict[8]+pop_list})
        elif int(num_instructions[i][2]) in new_stacks[8]:
            stack_dict.update({9:stack_dict[9]+pop_list})
        pop_list.clear()
        
for values in stack_dict.values():
    print(values[-1],end="")

