
## **🔹 if, elif, and else Statements in Python**  

### **1️⃣ What is an if-elif-else statement?**  
#In Python, `if`, `elif`, and `else` statements are used for **decision-making**. These statements allow the program to execute different code blocks based on conditions.

### **2️⃣ Syntax of if-elif-else**  
#if condition1:
    # Code runs if condition1 is True
#elif condition2:
    # Code runs if condition1 is False but condition2 is True
#else:
    # Code runs if all conditions above are False

## **3️⃣ if Statement**
#🔹 The `if` statement checks a condition. If the condition is `True`, the block of code inside it is executed.

#✅ **Example: Checking if a number is positive**  
num = 10

if num > 0:
    print("The number is positive")

# Output: The number is positive

## **4️⃣ if-else Statement**
#🔹 The `else` block runs if the `if` condition is `False`.

#✅ **Example: Checking if a number is even or odd**  
num = 7

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Output: Odd Number

## **5️⃣ if-elif-else Statement**
#🔹 `elif` (short for **else if**) allows you to check multiple conditions.

#✅ **Example: Checking temperature levels**  
temperature = 30

if temperature > 35:
    print("It's too hot! ☀️")
elif temperature > 25:
    print("The weather is nice! 🌤")
elif temperature > 15:
    print("It's a bit cool! 🍃")
else:
    print("It's cold! ❄️")

# Output: The weather is nice! 🌤

## **6️⃣ Nested if Statements**
#🔹 You can also use **if statements inside another if statement**.

#✅ **Example: Checking age for a movie ticket**  
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("You can enter the movie 🎬")
    else:
        print("You need a ticket! 🎟")
else:
    print("You are too young for this movie! 🚫")

# Output: You can enter the movie 🎬

## **🔹 Key Takeaways**
#✔ `if` is used to check a condition.  
#✔ `else` is used when no `if` conditions are met.  
#✔ `elif` is used to check multiple conditions.  
#✔ Python uses **indentation** to define code blocks inside if-elif-else statements.  
#✔ You can **nest if statements** inside another if.  



