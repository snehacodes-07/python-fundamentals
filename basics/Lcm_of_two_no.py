num1 = int(input("enter num1:  "))
num2 = int(input("enter num2:  "))
lcm = 0
s = max(num1,num2)

while True:
    if s%num1 == 0 and s%num2 == 0:
        print("LCM : ",s)
    break
