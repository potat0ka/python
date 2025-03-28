## **1️⃣ What is a While Loop?**  
#A **while loop** in Python is used to execute a block of code **repeatedly** as long as a given condition is `True`.  

#🔹 **Syntax of a while loop:**  
#while condition:
    # Code to execute
#✔ The loop **keeps running** until the condition becomes `False`.  

## **2️⃣ Example of a While Loop**
x = 1  # Initialization
while x <= 5:  # Condition
    print(x)  # Statement inside loop
    x += 1  # Increment

print("Loop finished!")  # Code after the loop

### **📝 Output:**  
#1
#2
#3
#4
#5
#Loop finished!

#📌 **Explanation:**  
#- The loop starts with `x = 1`.  
#- It checks `x <= 5` → If `True`, it prints `x` and increases `x` by `1`.  
#- When `x` becomes `6`, the condition is `False`, so the loop stops.  

## **3️⃣ Using a While Loop with User Input**  
password = ""
while password != "secret":  # The loop runs until user types "secret"
    password = input("Enter password: ")

print("Access granted!")
#📌 **Explanation:**  
#- The loop **keeps asking** for the password **until** the user enters `"secret"`.  
#- Once `"secret"` is entered, the loop **stops**, and `"Access granted!"` is printed.  

## **4️⃣ Infinite Loop (Be Careful!)**
#If we **forget to update** the condition, we might create an **infinite loop**.  
x = 1
while x <= 5:
    print(x)  # ❌ No increment, loop never stops!
#🔴 **This will run forever** because `x` **never** increases!  

#✅ To fix this, always **update** the condition inside the loop.  

## **5️⃣ Using `break` to Exit a While Loop**  
#The `break` statement **immediately stops** the loop.  
x = 1
while x <= 10:
    if x == 5:
        break  # Stops the loop when x == 5
    print(x)
    x += 1

print("Loop exited!")
### **📝 Output:**  
#1
#2
#3
#4
#Loop exited!

#📌 **Explanation:**  
#- When `x == 5`, the `break` **stops** the loop.  

## **6️⃣ Using `continue` to Skip an Iteration**  
#The `continue` statement **skips the current iteration** and moves to the next one.  
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue  # Skip 3
    print(x)
### **📝 Output:**  
#1
#2
#4
#5

#📌 **Explanation:**  
#- When `x == 3`, `continue` **skips** printing `3`.  

## **🔹 Exercise:**
#Write a Python program that:  
#✔ Asks the user to enter a **number**.  
#✔ Uses a `while` loop to print numbers **from 1 to that number**.  
