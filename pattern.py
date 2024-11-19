limit=int(input("Enter the limit"))
for i in range(limit):
    for j in range(i):
       print(" *",end=" ")
    print()


row=int(input("Enter the row"))
for i in range(row,0,-1):
    for j in range(i):
        print(" *",end=" ")
    print()


row=int(input("Enter the row"))
for i in range(1,row + 1):
    for j in range(row - i):
        print(" ",end="")
    for k in range(2 * i -1):
            print("*",end="")
    print()




row=int(input("Enter the row"))
for i in range(row,0,-1):
    for j in range(row - i):
         print(" ",end="")
    for k in range(2 * i -1):
            print("*",end="")
    print()