num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))
if num2>num3 and num2:
    print(num2)
elif num3>num1 and num3>num2:
    print(num3)
elif num1>num3 and num1>num2:
    print(num1)