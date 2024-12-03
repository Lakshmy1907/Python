'''
author:Lakshmy Byju
date:03-12-2024
python prorgam to find fibonacci of a function
'''
def fibonacci(n):
    sequence=[]
    first_num,second_num=5,9
    for i in range(n):
        sequence.append(first_num)
        first_num,second_num=second_num,first_num+second_num
    return sequence
fibonacci(10)