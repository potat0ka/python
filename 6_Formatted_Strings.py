#**Formatted Strings in Python**  

#**What is a Formatted String?**  
#A **formatted string** (also called an **f-string**) is a modern and efficient way to insert variables into strings.  
#- Introduced in **Python 3.6**  
#- Uses the prefix **`f`** before the string  
#- Allows you to embed expressions inside curly braces **`{}`**  

### **Why Use Formatted Strings?**  
#1. **Cleaner & More Readable** → Avoids messy concatenation (`+`)  
#2. **More Efficient** → Faster than older methods like `format()`  
#3. **Can Include Expressions** → You can perform calculations inside `{}`  

### **Example of a Formatted String**
name = "Potato"
age = 25

# Using an f-string
message = f"My name is {name} and I am {age} years old."
print(message)

### **Comparison with Other Methods**  

#### **1️⃣ Using Concatenation (`+`)** → ❌ **Messy & Less Readable**  

name = "Potato"
age = 25
print("My name is " + name + " and I am " + str(age) + " years old.")

#### **2️⃣ Using `.format()` (Older Method)**  
name = "Potato"
age = 25
print("My name is {} and I am {} years old.".format(name, age))

#### **3️⃣ Using f-strings (Recommended) ✅**  
name = "Potato"
age = 25
print(f"My name is {name} and I am {age} years old.")

### **Advanced Examples of f-strings**
#### **1️⃣ Inline Calculations**
price = 50
discount = 10
print(f"The final price after discount is {price - discount} dollars.")

#### **2️⃣ Formatting Numbers (Rounding)**

pi = 3.14159
print(f"Pi rounded to 2 decimal places: {pi:.2f}")

#### **3️⃣ Using Functions in f-strings**
def greet(name):
    return f"Hello, {name}!"

print(f"{greet('Potato')}, Welcome to Python!")

### **Key Takeaways**
#| Feature               | Description                                            |
#| **Prefix `f`**        | Start the string with `f` or `F`                       |
#| **Curly braces `{}`** | Used to insert variables or expressions inside strings |
#| **More readable**     | Cleaner than `+` concatenation                         |
#| **More efficient**    | Faster than `.format()` method                         |