num = int(input("enter a number: "))
org = num
reverse = 0
while num>0:
    digit = num%10
    reverse = reverse*10 + digit
    num = num//10
print("original number is : ",org)
print("reversed number is : ",reverse)
