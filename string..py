string_input=input("Enter a number")
vowels="AEIOUaeiou"
vowels_count=0
for char in string_input:
    if char in vowels:
        vowels_count+=1
print(f"number of vowels in the given string{string_input}  is {vowels_count}")