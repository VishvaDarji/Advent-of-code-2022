#part a
with open('day06.txt', 'rt') as file:
    day6_data=file.readlines()
idx_part1=[]

for i in range(len(day6_data)):
    for j in range(len(day6_data[i])):
        if len(day6_data[i][j:j+4])==len(set(day6_data[i][j:j+4])):
            idx_part1.append(j)
            #print(day6_data[i][j:j+4])
            break
        elif len(day6_data[i][j:j+14])==len(set(day6_data[i][j:j+14])):
            idx_part2.append(j)
            break
idx_part1=[val+4 for val in idx_part1]
print(idx_part1)

#part b
idx_part2=[]
for i in range(len(day6_data)):
    for j in range(len(day6_data[i])):
        if len(day6_data[i][j:j+14])==len(set(day6_data[i][j:j+14])):
            idx_part2.append(j)
            break
idx_part2=[val+14 for val in idx_part2]
idx_part2