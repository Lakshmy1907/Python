check_prime=int(input("Enter a number"))
isprime =True
for i in range(2,check_prime//2+1):
    if check_prime % i==0:
        isprime=False
    break
if isprime:
    print(f"The given number {check_prime}is prime")
else:
    print(f"THe given number {check_prime}is not prime")
