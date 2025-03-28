# **🔹 Logical Operators in Python**  

## **1️⃣ What are Logical Operators?**  
#Logical operators are used to combine multiple **conditions** in Python. They return either `True` or `False` based on the conditions.

#Python has three logical operators:  
#✔ `and` – Returns `True` if **both** conditions are `True`.  
#✔ `or` – Returns `True` if **at least one** condition is `True`.  
#✔ `not` – Reverses the condition (`True` becomes `False`, and `False` becomes `True`).  

## **2️⃣ Logical Operators with Examples**  

### **✅ and Operator**
#✔ `and` returns `True` **only if both conditions are True**.  
age = 25
has_id = True

if age >= 18 and has_id:
    print("You can enter the club 🎉")
else:
    print("Access Denied 🚫")

# Output: You can enter the club 🎉

#📌 **Explanation:**  
#- Since both `age >= 18` and `has_id` are `True`, the output is `"You can enter the club"`.

### **✅ or Operator**
#✔ `or` returns `True` **if at least one condition is True**.  
is_raining = False
has_umbrella = True

if is_raining or has_umbrella:
    print("You can go outside ☂️")
else:
    print("Stay indoors 🏠")

# Output: You can go outside ☂️

#📌 **Explanation:**  
#- Since `has_umbrella = True`, the output is `"You can go outside"` **even if it's not raining**.

### **✅ not Operator**
#✔ `not` **reverses** the condition.  

is_logged_in = False

if not is_logged_in:
    print("Please log in 🔒")
else:
    print("Welcome back! 😊")

# Output: Please log in 🔒

#📌 **Explanation:**  
#- `not is_logged_in` turns `False` into `True`, so the message **"Please log in"** is printed.

## **3️⃣ Combining Logical Operators**
#You can combine multiple logical operators in one condition.  
age = 22
has_ticket = True
is_vip = False

if (age >= 18 and has_ticket) or is_vip:
    print("Access Granted 🎟")
else:
    print("Access Denied 🚫")

# Output: Access Granted 🎟

#📌 **Explanation:**  
#- The condition `(age >= 18 and has_ticket)` is `True`, so the program prints `"Access Granted"`.

## **🔹 Exercise:**
#Write a program that:  
#✔ Asks the user for their age and whether they have a driver's license (`True` or `False`).  
#✔ If they are **18 or older** and have a driver's license, print `"You can drive 🚗"`.  
#✔ Otherwise, print `"You cannot drive yet 🚫"`.

