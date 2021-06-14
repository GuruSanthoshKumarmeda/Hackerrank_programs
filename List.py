if __name__ == '__main__':
    N = int(input())
    list1=[]
    for i in range(0,N):
        name= input().split();
        if name[0] == "print":
            print(list1)
        elif name[0] == "insert":
            list1.insert(int(name[1]),int(name[2]))

        elif name[0] == "remove":
            list1.remove(int(name[1]))
        elif name[0] == "append":
            list1.append(int(name[1]))
        elif name[0] == "sort":
            list1.sort();
        elif name[0]=="reverse":
            list1.reverse();
        else:
            list1.pop()
