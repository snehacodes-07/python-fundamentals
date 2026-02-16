number = input("enter number: ")
rev = 0
size = len(number)

while size > 0:
    digit = int(number)%10
    rev = (rev*10)+digit
    number= int(number)//10
    size-= 1

print(rev)