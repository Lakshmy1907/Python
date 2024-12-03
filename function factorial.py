'''
author:Lakshmy BYju
date:3-12-2024
python program to fin function factorial
'''
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
f=factorial(5)
print(f)
