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

def sum_lst(a):
    sum = 0
    for i in a:
        sum += i
    return(sum)

print("summation of elements: ",sum(arr))