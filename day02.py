#part a
file=open('day02.txt')
day2_data=file.readlines()
opponent={'A':'Rock','B':'Paper','C':'Scissors'}
you={'X':'Rock','Y':'Paper','Z':'Scissors'}
roundwise_point=[]
selected_shape={'Rock':1,'Paper':2,'Scissors':3}
round_outcome={'Lost':0,'Draw':3,'Win':6}

for each_round in day2_data:
    game_data=each_round.split()
    if opponent[game_data[0]]==you[game_data[1]]:
        if you[game_data[1]]=='Rock':
            roundwise_point.append(selected_shape['Rock']+round_outcome['Draw'])
        elif you[game_data[1]]=='Paper':
            roundwise_point.append(selected_shape['Paper']+round_outcome['Draw'])
        elif you[game_data[1]]=='Scissors':
            roundwise_point.append(selected_shape['Scissors']+round_outcome['Draw'])
    elif opponent[game_data[0]]=='Rock' and you[game_data[1]]=='Paper':
        roundwise_point.append(selected_shape['Paper']+round_outcome['Win'])
    elif opponent[game_data[0]]=='Paper' and you[game_data[1]]=='Rock':
        roundwise_point.append(selected_shape['Rock']+round_outcome['Lost'])
    elif opponent[game_data[0]]=='Rock' and you[game_data[1]]=='Scissors':
        roundwise_point.append(selected_shape['Scissors']+round_outcome['Lost'])
    elif opponent[game_data[0]]=='Scissors' and you[game_data[1]]=='Rock':
        roundwise_point.append(selected_shape['Rock']+round_outcome['Win'])
    elif opponent[game_data[0]]=='Scissors' and you[game_data[1]]=='Paper':
        roundwise_point.append(selected_shape['Paper']+round_outcome['Lost'])
    elif opponent[game_data[0]]=='Paper' and you[game_data[1]]=='Scissors':
        roundwise_point.append(selected_shape['Scissors']+round_outcome['Win'])
    
print(sum(roundwise_point))

#part b
second_col={'X':'Lose','Y':'Draw','Z':'Win'}
part2_roundwise=[]
for each_round in day2_data:
    game_data=each_round.split()
    if second_col[game_data[1]]=='Lose':
        if opponent[game_data[0]]=='Rock':
            part2_roundwise.append(selected_shape['Scissors']+round_outcome['Lost'])
        elif opponent[game_data[0]]=='Paper':
            part2_roundwise.append(selected_shape['Rock']+round_outcome['Lost'])
        elif opponent[game_data[0]]=='Scissors':
            part2_roundwise.append(selected_shape['Paper']+round_outcome['Lost'])
            
    elif second_col[game_data[1]]=='Draw':
        if opponent[game_data[0]]=='Rock':
            part2_roundwise.append(selected_shape['Rock']+round_outcome['Draw'])
        elif opponent[game_data[0]]=='Paper':
            part2_roundwise.append(selected_shape['Paper']+round_outcome['Draw'])
        elif opponent[game_data[0]]=='Scissors':
            part2_roundwise.append(selected_shape['Scissors']+round_outcome['Draw'])
    
    elif second_col[game_data[1]]=='Win':
        if opponent[game_data[0]]=='Rock':
            part2_roundwise.append(selected_shape['Paper']+round_outcome['Win'])
        elif opponent[game_data[0]]=='Paper':
            part2_roundwise.append(selected_shape['Scissors']+round_outcome['Win'])
        elif opponent[game_data[0]]=='Scissors':
            part2_roundwise.append(selected_shape['Rock']+round_outcome['Win'])
print(sum(part2_roundwise))