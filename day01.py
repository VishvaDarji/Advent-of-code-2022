# Part a
f=open('day01.txt')
day1_data=f.readlines()
cal_values=[]
for cal in day1_data:
    calorie=0
    if cal.startswith('\n')==False:
        calorie=calorie+int(cal)
        cal_values.append(calorie)
    else:
        cal_values.append('\n')
calories=[]
cal_sum=[]
elf_count=1
for cal in cal_values: 
    if cal=='\n':
        cal_sum.append(sum(calories))
        elf_count+=1
        calories.clear()
    else:
        calories.append(int(cal)) 
print(sum(calories))

# Part b

top1=max(cal_sum)
cal_sum.remove(top1)

top2=max(cal_sum)
cal_sum.remove(top2)

top3=max(cal_sum)

sum_top3s=top1+top2+top3
print(sum_top3s)