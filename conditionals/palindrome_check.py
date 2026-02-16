number = int(input("enter number: "))
original = number
rev = 0
size = len(str(number))

while size > 0:
    digit = number%10
    rev = (rev*10)+digit
    number= number//10
    size-= 1
print("reversed number: ",rev)

if original == rev:
    print("palindrome number")
else:
    print("nope! not a palindrome")