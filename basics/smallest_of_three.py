num1 = int(input("enter element: "))
num2 = int(input("enter element: "))
num3 = int(input("enter element: "))

if num1 < num2 and num1 < num3:
    print(num1,"is smallest")
elif num2 < num1 and num2 < num3:
    print(num2,"is smallest")
elif num3 < num1 and num3 < num2:
    print(num3,"is smallest")
else:
    print("invalid input")