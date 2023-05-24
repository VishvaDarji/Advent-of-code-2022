#part 1
# referred to AOC reddit page

with open('day10.txt', 'rt') as file:
    day10_data=file.readlines()

X_register=1
cycle_num=0
during=0
after=0
string=""
signal_strength=[]
for instruction in day10_data:
    if instruction.startswith('noop'):
        cycle_num+=1
        X_register+=0 #no change
        
        if cycle_num==20:
            signal_strength.append(X_register*20)
        elif cycle_num==60:
            signal_strength.append(X_register*60)
        elif cycle_num==100:
            signal_strength.append(X_register*100)
        elif cycle_num==140:
            signal_strength.append(X_register*140)
        elif cycle_num==180:
            signal_strength.append(X_register*180)
        elif cycle_num==220:
            signal_strength.append(X_register*220)
        
    elif instruction.startswith('addx'):
        cycle_num+=1
        
        during+=X_register
        if cycle_num==20:
            signal_strength.append(X_register*20)
        elif cycle_num==60:
            signal_strength.append(X_register*60)
        elif cycle_num==100:
            signal_strength.append(X_register*100)
        elif cycle_num==140:
            signal_strength.append(X_register*140)
        elif cycle_num==180:
            signal_strength.append(X_register*180)
        elif cycle_num==220:
            signal_strength.append(X_register*220)
       
        cycle_num+=1
        
        if cycle_num==20:
            signal_strength.append(X_register*20)
        elif cycle_num==60:
            signal_strength.append(X_register*60)
        elif cycle_num==100:
            signal_strength.append(X_register*100)
        elif cycle_num==140:
            signal_strength.append(X_register*140)
        elif cycle_num==180:
            signal_strength.append(X_register*180)
        elif cycle_num==220:
            signal_strength.append(X_register*220)
        
        X_register+=int(instruction.split()[1])
        after+=X_register

print(sum(signal_strength))

#part 2

x_register = 1
lit_pixels = []
cycle_num = 0

for line in day10_data:
    cycle_num += 1
    if cycle_num in range(x_register,x_register+3):
        lit_pixels.append(cycle_num - 1)
    if cycle_num == 40:
        for idx in range(40):
            if idx in lit_pixels:
                print("#", end="") 
            else:
                print(".", end="")
        print()
        lit_pixels.clear()
        cycle_num = 0
    
    if line.startswith("addx"):
        cycle_num += 1
        if cycle_num in range(x_register,x_register+3):
            lit_pixels.append(cycle_num - 1)
        if cycle_num == 40:
            for idx in range(40):
                if idx in lit_pixels:
                    print("#", end="") 
                else:
                    print(".", end="")
            print()
            lit_pixels.clear()
            cycle_num = 0
        x_register += int(line.split()[1])
