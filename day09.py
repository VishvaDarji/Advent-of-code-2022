#Part 1
#reffered to AOC reddit pages

with open("day09.txt") as file:
    day9_data = file.readlines()

instructions=[]
for line in day9_data:
    instructions.append((line.strip().split()[0],int(line.strip().split()[1])))

hr = hc = tr = tc = 0
positions_moved = set()

for direction,n_steps in instructions:
    
    for step in range(n_steps):
        if direction=='U':
            hr += 1
        elif direction== 'D':
            hr -= 1
        elif direction== 'R':
            hc += 1
        elif direction== 'L':
            hc -= 1

        if (hr - tr == -1 and hc - tc < -1) or (hr - tr < -1 and hc - tc == -1):
            tr -= 1
            tc -= 1
        elif (hr - tr == 1 and hc - tc > 1) or (hr - tr > 1 and hc - tc == 1):
            tr += 1
            tc += 1
        elif (hr - tr == 1 and hc - tc < -1) or (hr - tr > 1 and hc - tc == -1):
            tr += 1
            tc -= 1
        elif (hr - tr == -1 and hc - tc > 1) or (hr - tr < -1 and hc - tc == 1):
            tr -= 1
            tc += 1
        elif hc - tc < -1:
            tc -= 1
        elif hr - tr < -1:
            tr -= 1
        elif hr - tr > 1:
            tr += 1
        elif hc - tc > 1:
            tc += 1

        positions_moved.add((tr,tc))

print(len(positions_moved))
