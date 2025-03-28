#2️⃣ Odd or Even Checker: Ask the user to enter a number and determine whether it is odd or even.
num = int(input('Enter the Number: '))

if num %2 == 0:
    print(f'the {num} is even. ')
else:
    print(f'the {num} is odd ')    

#Why use if num % 2 == 0?
#The modulus operator (%) returns the remainder when dividing two numbers.

#If a number is even, it is divisible by 2 with no remainder.
#Example: 4 % 2 = 0, 10 % 2 = 0
#If a number is odd, it is not perfectly divisible by 2 and leaves a remainder of 1.
#Example: 5 % 2 = 1, 11 % 2 = 1
    