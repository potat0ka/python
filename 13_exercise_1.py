name = input('What is your name?: ').strip()  # Stripping spaces to avoid accidental input issues

if len(name) < 3:  # Should be less than 3, not <= 3
    print('Name must be at least 3 characters long.')
elif len(name) > 50:
    print('Name can be a maximum of 50 characters long.')
else:
    print(f'{name} looks GOOD.')


