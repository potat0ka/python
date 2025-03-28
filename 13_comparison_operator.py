# **🔹 Comparison Operators in Python**  

## **1️⃣ What are Comparison Operators?**  
#Comparison operators are used to compare **two values**. These operators return **True** or **False** based on the comparison result.

#Python has **six** comparison operators:  

#| Operator | Meaning               | Example (Returns `True`) |
#| `==`     | Equal to              | `5 == 5`                 |
#| `!=`     | Not equal to          | `5 != 3`                 |
#| `>`      | Greater than          | `10 > 5`                 |
#| `<`      | Less than             | `3 < 7`                  |
#| `>=`     | Greater than or equal | `8 >= 8`                 |
#| `<=`     | Less than or equal    | `6 <= 10`                |

## **2️⃣ Comparison Operators with Examples**  

### **✅ 1. `==` (Equal to)**
#✔ Used to check if **two values are the same**.  
x = 10
y = 10

print(x == y)  # Output: True
print(5 == 3)  # Output: False 

#📌 **Explanation:**  
#- `x == y` is `True` because both have the value **10**.  
#- `5 == 3` is `False` because **5 is not equal to 3**.  

### **✅ 2. `!=` (Not equal to)**
#✔ Used to check if **two values are different**.  
a = 7
b = 10

print(a != b)  # Output: True
print(10 != 10)  # Output: False

#📌 **Explanation:**  
#- `a != b` is `True` because **7 is not equal to 10**.  
#- `10 != 10` is `False` because **both values are the same**.  

### **✅ 3. `>` (Greater than)**
#✔ Used to check if the **left value is greater** than the right value.  
age = 21
print(age > 18)  # Output: True

marks = 50
print(marks > 60)  # Output: False

#📌 **Explanation:**  
#- `age > 18` is `True` because **21 is greater than 18**.  
#- `marks > 60` is `False` because **50 is not greater than 60**.  

### **✅ 4. `<` (Less than)**
#✔ Used to check if the **left value is smaller** than the right value.  

speed = 80
print(speed < 100)  # Output: True

height = 170
print(height < 150)  # Output: False

#📌 **Explanation:**  
#- `speed < 100` is `True` because **80 is less than 100**.  
#- `height < 150` is `False` because **170 is greater than 150**.  

### **✅ 5. `>=` (Greater than or equal to)**
#✔ Used to check if the **left value is greater than or equal** to the right value.  

score = 75
print(score >= 75)  # Output: True

money = 100
print(money >= 150)  # Output: False

#📌 **Explanation:**  
#- `score >= 75` is `True` because **75 is equal to 75**.  
#- `money >= 150` is `False` because **100 is less than 150**.  

### **✅ 6. `<=` (Less than or equal to)**
#✔ Used to check if the **left value is smaller than or equal** to the right value.  
temperature = 30
print(temperature <= 30)  # Output: True

salary = 40000
print(salary <= 35000)  # Output: False

#📌 **Explanation:**  
#- `temperature <= 30` is `True` because **30 is equal to 30**.  
#- `salary <= 35000` is `False` because **40,000 is greater than 35,000**.  

## **3️⃣ Combining Comparison Operators with Logical Operators**
#You can use **logical operators (`and`, `or`, `not`)** with comparison operators.  
age = 25
income = 5000

if age >= 18 and income >= 3000:
    print("Eligible for credit card 💳")
else:
    print("Not eligible ❌")

# Output: Eligible for credit card 💳

#📌 **Explanation:**  
#- The person **is 25 years old** and **has an income of 5000**, so they meet both conditions.

## **🔹 Exercise:**
#Write a Python program that:  
#✔ Asks the user to enter **two numbers**.  
#✔ Compares them using **comparison operators**.  
#✔ Prints whether the first number is **greater than, less than, or equal to** the second number.
