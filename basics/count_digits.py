num = int(input("enter number: "))
original = num
sum=0

while num>0:
    sum+= 1
    num//= 10

print("total digits = ",sum)

