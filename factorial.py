'''#author: Lakshmy BYju
#date: 15-10-2024
To find the factorial of a number'''
number=int(input(":Enter a number"))
fact=1
while number>0:
    fact=fact*number
    number-=1
print(fact)