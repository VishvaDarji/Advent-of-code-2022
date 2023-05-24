#part a
file=open('day04.txt')
day4_data=file.readlines()
elf1=[]
elf2=[]

Complete_Overlaps=[]
for pairs in day4_data:
    elf1.append(pairs.split(',')[0])
    elf2.append(pairs.split(',')[1])
Complete_Overlaps=0
no_overlap=0
some_overlap=0

for e1_item, e2_item in zip(elf1,elf2):
    e1_start_end=e1_item.split('-')
    e2_start_end=e2_item.split('-')
    if int(e1_start_end[0]) in range(int(e2_start_end[0]),int(e2_start_end[1])+1) and int(e1_start_end[1]) in range(int(e2_start_end[0]),int(e2_start_end[1])+1):
        Complete_Overlaps+=1
    elif int(e2_start_end[0]) in range(int(e1_start_end[0]), int(e1_start_end[1])+1) and int(e2_start_end[1]) in range(int(e1_start_end[0]), int(e1_start_end[1])+1):
        Complete_Overlaps+=1
        
    elif int(e2_start_end[0]) not in range(int(e1_start_end[0]), int(e1_start_end[1])+1) and int(e2_start_end[1]) not in range(int(e1_start_end[0]), int(e1_start_end[1])+1):
        no_overlap+=1
    elif int(e1_start_end[0]) not in range(int(e2_start_end[0]),int(e2_start_end[1])+1) and int(e1_start_end[1]) not in range(int(e2_start_end[0]),int(e2_start_end[1])+1):
        no_overlap+=1    
    else:
        some_overlap+=1

print(Complete_Overlaps)

#Part B
print(Complete_Overlaps+ some_overlap)