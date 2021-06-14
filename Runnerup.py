n = int(input())
if n>=2 and n<=10:
    list1=list(map(int,input().split()))
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i);
list2.sort(reverse=True);
print(list2[1])
    
    
