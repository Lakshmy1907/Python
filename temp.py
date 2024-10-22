temperature=int(input("Enter the nnumber"))
scale=input("is this in(c)celsius or (f)fahrenheit")
if(scale=="c"):
    f=(9/5*temperature)+32
    print(temperature,"celsius is",f,"fahrenheit")
else:
    c=5/9*(temperature-32)
    print(temperature,"fahrenheit is",c,"celsius")