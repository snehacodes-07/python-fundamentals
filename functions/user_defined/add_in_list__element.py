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

def update_lst(arr):
    arr1 = []
    for i in arr:
        i += 10
        arr1.append(i)
    return(arr1)

updated_arr = update_lst(arr)
print("updated list: ",updated_arr)

        

