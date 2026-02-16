num = int(input("enter number: "))
fact=0

for i in range(1,num+1):
    if num%i == 0:
        fact+=1

if fact == 2:
    print("prime number")
else:
    print("not a prime number")