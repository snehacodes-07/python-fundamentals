num = int(input("enter number: "))
org = num
sum = 0
while num>0:
    digit = num%10
    sum += digit
    num = num//10
print("entered number : ",org)
print("sum of digits: ",sum)