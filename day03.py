#part a
import string

file=open('day03.txt')
day3_data=file.readlines()

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)

lowercase_priority={letter:num for letter, num in zip(lowercase,range(1,27)) }
uppercase_priority={letter:num for letter, num in zip(uppercase,range(27,53)) }

rucksack_scores=[]      
for rucksack in day3_data:
    if rucksack.endswith('\n')!=True:
        commons=set(rucksack[0:len(rucksack)//2]) & set(rucksack[len(rucksack)//2:len(rucksack)])
        for item in commons:
            if item in uppercase:
                rucksack_scores.append(uppercase_priority[item])
            elif item in lowercase:
                rucksack_scores.append(lowercase_priority[item])

    else:
        commons1=set(rucksack[0:(len(rucksack)-1)//2]) & set(rucksack[(len(rucksack)-1)//2:len(rucksack)])
        for item in commons1:
            if item in uppercase:
                rucksack_scores.append(uppercase_priority[item])
            elif item in lowercase:
                rucksack_scores.append(lowercase_priority[item])

print(sum(rucksack_scores))

#part b

grouped_rucksacks = [day3_data[n:n+3] for n in range(0, len(day3_data), 3)]

grp_scores=[]
for grp in grouped_rucksacks:
    commons=set(grp[0]) & set(grp[1]) & set(grp[2])
    for item in commons:
        if item in uppercase:
            grp_scores.append(uppercase_priority[item])
        elif item in lowercase:
            grp_scores.append(lowercase_priority[item])
print(sum(grp_scores))
