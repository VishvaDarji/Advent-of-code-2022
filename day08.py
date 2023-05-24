with open('day08.txt', 'rt') as file:
    day8_data=file.readlines()
l=[]
for i in range(len(day8_data)):
    if '\n' in list(day8_data[i]):
        l.append(list(day8_data[i].replace('\n','')))
    else:
        l.append(list(day8_data[i]))
import numpy as np
arr=np.array(l)
row1=arr[0]
last_row=arr[-1]
col1=arr[:,0]
last_col=arr[:,-1]
edge_trees=len(row1)+len(last_row)+len(col1)+len(last_col)-4
total_inner_visibility=0

for i in range(1,len(arr)-1):#1-98 colwise

    for j in range(1,len(arr[i])-1):
        
        top_trees=max(arr[:i,j])
        bottom_trees=max(arr[i+1:,j])
        
        right_trees=max(arr[i,j+1:])
        left_trees=max(arr[i,:j])
        
        #right side
        if arr[i,j]>right_trees:
            total_inner_visibility+=1
            continue
        #left side
        elif arr[i,j]>left_trees:
            total_inner_visibility+=1
            continue
        #top side
        elif arr[i,j]>top_trees:
            total_inner_visibility+=1
            continue
        #bottom side
        elif arr[i,j]>bottom_trees:
            total_inner_visibility+=1
            continue      
print(total_inner_visibility+edge_trees)

#part b
top=[]
bottom=[]
right=[]
left=[]
scenic_score=[]

for i in range(1,len(arr)-1):
    for j in range(1,len(arr[i])-1):
        #top
        #print(arr[:i,j])
        for num in list(reversed(arr[:i,j])):
            if arr[i,j]>num:
                top.append(1)
            else:
                top.append(1)
                break  
    
        #bottom
        #print(arr[i+1:,j])
        for num in arr[i+1:,j]:
            if arr[i,j]>num:
                bottom.append(1)
            else:
                bottom.append(1)
                break
            
        #right
        #print(arr[i,j+1:])
        for num in arr[i,j+1:]:
            if arr[i,j]>num:
                right.append(1)
            else:
                right.append(1)
                break
            
        #left
        #print(arr[i,:j])
        for num in list(reversed(arr[i,:j])):
            if arr[i,j]>num:
                left.append(1)
            else:
                left.append(1)
                break
             
        #scenic_score.append(top*bottom*right*left)
        #print(arr[i,j],'top',top,'bottom',bottom,'right',right,'left',left)
        scenic_score.append(sum(top)*sum(bottom)*sum(right)*sum(left))
        top.clear()
        bottom.clear()
        right.clear()
        left.clear()
        
print(max(scenic_score))