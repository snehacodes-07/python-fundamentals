# FIBONACCI SERIES
size = int(input("enter limit of the series: "))
a=0
b=1
for i in range(0,size+1):
        print(a,end=' ')
        c=a+b
        a=b
        b=c
print("\nexecuted successfully")