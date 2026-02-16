num = int(input("Enter a number: "))
original = num
sum_factorial = 0

while num > 0:
    digit = num % 10
    
    # Calculate factorial of digit
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    
    sum_factorial += fact
    num = num // 10

print("logic vale: ",sum_factorial)
if sum_factorial == original:
    print("Strong Number")
else:
    print("Not a Strong Number")
