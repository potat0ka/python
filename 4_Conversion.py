# **Data Types in Python**  
#Python has different **data types** to store different kinds of values:  

#1. **int (Integer)** → Whole numbers (e.g., `10`, `-5`, `1000`)  
#2. **str (String)** → Text (e.g., `"Hello"`, `'Python'`, `"123"`)  
#3. **float (Floating-Point Number)** → Numbers with decimals (e.g., `3.14`, `0.5`, `-2.75`)  
#4. **bool (Boolean)** → Represents `True` or `False`  

# Example: Working with Data Types  
birth_year = input("Your Birth Year? ")  # Input is always a string
print(type(birth_year))  # Check the data type (str)

age = 2025 - int(birth_year)  # Convert birth_year to int before subtraction
print(type(age))  # Check the new data type (int)
print(age)  # Print calculated age


### **What is `type()` Used For?**  
#- The `type()` function **returns the data type** of a variable.  
#- This helps us check whether a value is stored as a string, integer, float, etc.  

num = 10
print(type(num))  # Output: <class 'int'>

text = "Hello"
print(type(text))  # Output: <class 'str'>

is_active = True
print(type(is_active))  # Output: <class 'bool'>

price = 9.99
print(type(price))  # Output: <class 'float'>
#Exercise: Convert Weight from Pounds to Kilograms**  
#Problem: Ask the user for their weight in **pounds**, convert it to **kilograms**, and print the result.

# Taking user input
full_name = input("What is Your Full Name?: ")
body_weight = input("What is Your Body Weight (in pounds)?: ")

# Convert weight from string to float and apply conversion formula
weight_kg = float(body_weight) / 2.205  

print(f"{full_name}, your weight in kilograms is: {weight_kg:.2f} kg")

### **Improvements & Explanation:**  
#1. **Used `float()`** for weight conversion (since weight can be decimal).  
#2. **Formatted output (`:.2f`)** to round the weight to 2 decimal places.  
#3. **Used f-strings (`f""`)** for a cleaner and more readable output.  
