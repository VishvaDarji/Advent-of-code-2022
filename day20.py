#referred to AOC reddit pages
#part 1
with open('day20.txt', 'rt') as file:
    day20_data=file.readlines()

coords=[]
for num in day20_data:
    coords.append(int(num))

tup_coords = []
for i,x in enumerate(coords):
    tup_coords.append((i,x))
    
for i, num in enumerate(coords):
    coord = (i,num)
    now_at = tup_coords.index(coord)
    if num == 0:
        continue        
        
    del tup_coords[now_at]

    new_posi = now_at + num
    new_posi %= len(tup_coords)
    if new_posi < 0:
        new_posi += len(tup_coords)
    tup_coords.insert(new_posi,coord)

encryp_zero_pos = coords.index(0)
zero_number = (encryp_zero_pos,0)
zero_pos = tup_coords.index(zero_number)

pos1 = zero_pos + 1000
pos1 %= len(tup_coords)
i1, n1 = tup_coords[pos1]

pos2 = zero_pos + 2000
pos2 %= len(tup_coords)
i2, n2 = tup_coords[pos2]

pos3 = zero_pos + 3000
pos3 %= len(tup_coords)
i3, n3 = tup_coords[pos3]

#sum of 3 coordinates
print(n1+n2+n3)

#part 2
with open('day20.txt', 'rt') as file:
    day20_data=file.readlines()
coords=[int(num) for num in day20_data]

decryp_key=811589153
coords = [x * decryp_key for x in coords]

tup_coords = [(i,x) for i,x in enumerate(coords)]

for x in range(10):#10 times of mixing
    for i, num in enumerate(coords):
        coord = (i,num)
        now_at = tup_coords.index(coord)
        if num == 0:
            continue        

        del tup_coords[now_at]

        new_posi = now_at + num
        new_posi %= len(tup_coords)
        if new_posi < 0:
            new_posi += len(tup_coords)
        tup_coords.insert(new_posi,coord)
zero=coords.index(0)
zero_number = (zero,0)
zero_pos = tup_coords.index(zero_number)

pos1 = zero_pos + 1000
pos1 %= len(tup_coords)
i1, n1 = tup_coords[pos1]

pos2 = zero_pos + 2000
pos2 %= len(tup_coords)
i2, n2 = tup_coords[pos2]

pos3 = zero_pos + 3000
pos3 %= len(tup_coords)
i3, n3 = tup_coords[pos3]

#sum of 3 coordinates
print(n1+n2+n3)
