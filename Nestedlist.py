n=int(input())
list1=[]
list2=[]
list1=[[input(),float(input())] for i in range(n)]
for i in list1:
    list2.append(i[1])
list3=list(set(list2))
list3.sort()
x=list3[1]
list4=[]
for i in list1:
    if i[1]==x:
        list4.append(i[0])
for i in sorted(list4):
    print(i)
        
