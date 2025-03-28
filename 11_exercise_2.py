#1️⃣ Age Classifier: Write a program that asks the user for their age and categorizes them as child, teenager, adult, or senior citizen.
age = int(input('How old are you? : '))

if age < 16:
    print(f'You are {age} years old, which means you are a child.')
elif age < 20:
    print(f'You are {age} years old, which means you are a teenager.')
elif age < 40:
    print(f'You are {age} years old, which means you are an adult.')
else:
    print(f'You are {age} years old, which means you are senior citizen.')


