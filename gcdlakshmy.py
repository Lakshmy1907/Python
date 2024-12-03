'''
Author-Lakshmy Byju
Date: 3-12-2024
Python program to find the greatest common denominator using function
 '''
def gcd(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd(n2,n1%n2)
common=gcd(100,3)
print(common)