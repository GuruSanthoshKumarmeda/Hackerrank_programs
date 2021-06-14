import itertools
x=int(input())
y=int(input())
z=int(input())
n=int(input())
list2=[]
list1=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
for i in list1:
    if sum(i)!=n:
        list2.append(i)
print(list2)
        
