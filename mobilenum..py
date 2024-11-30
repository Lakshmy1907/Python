def valid_number():
    num=input("enter a number:")
    if len(num)==10 and num[0]=='7'or num[0]=='8' or num[0]=='9':
        print("num is valid")
    else:
        print("num is invalid")

valid_number()