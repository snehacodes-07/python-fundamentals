num1 = float(input("enter number 1: "))
num2 = float(input("enter number 2: "))
ask = input(" select the operation you want to opt for? \n+ (summation)\n-(substraction\n/ (division)\n% (modulus)")

if ask == "+" :
    print("summation = ",num1+num2)
elif ask == "-" :
    print("subtraction = ",num1-num2)
elif ask == "/" :
    if num2 != 0:
         print("division = ",num1/num2)
    else:
        print("number divide by zero")
elif ask == "%" :
    print("modulus = ",num1%num2)
else:
    print("invalid")