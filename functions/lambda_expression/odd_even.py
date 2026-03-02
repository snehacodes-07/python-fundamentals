def check(a):
    if a%2 == 0:
        print("the number is divisible by 2 \n\nIT'S AN EVEN NUMBER")
    else:
        print("the number is not divisible by 2 \n\nIT'S AN ODD NUMBER")
a = int(input("enter number: "))
check = lambda x:"EVEN"if x%2 ==0 else "ODD"
print("the number is : ",check(a))