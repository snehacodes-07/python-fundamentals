num = int(input("enter number: "))
original = num
sum=0

while num>0:
    str_num = str(num)
    for i in str_num:
        sum+= int(i)**(len(str_num))
        num//= 10

print("given number: ",original)
print("summation: ",sum)

if original == sum:
    print("armstrong number")
else:
    print("not an armstrong number")


