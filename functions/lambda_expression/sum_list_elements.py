def lst():
    size = int(input("enter size of list: "))
    l = []
    for i in range(1,size+1):
        print("enter element",i,": ",end='')
        a = int(input())
        l.append(a)
    return(l)

arr = lst()
print("given list: ",arr)

summation = sum(list(map(lambda x: x, arr)))
print("summation of elements: ",summation)