#referred to AOC reddit page
#part 1
with open("day18.txt") as file:
    day18_data = file.readlines()
data=[]
for line in day18_data:
    n1=line.strip().split(',')[0]
    n2=line.strip().split(',')[1]
    n3=line.strip().split(',')[2]
    data.append((int(n1),int(n2),int(n3)))
    
# part 1
neighbours=[(1, 0, 0), 
            (-1, 0, 0), 
            (0, 1, 0), 
            (0, -1, 0), 
            (0, 0, 1), 
            (0, 0, -1)]

def part1(cube):
    part1_list=[tuple(sum(x) for x in zip(cube, d)) for d in neighbours]
    return part1_list

surface_area = 0
for cube in data:
    for n in part1(cube):
        if n not in data:
            surface_area += 1

print(surface_area)
