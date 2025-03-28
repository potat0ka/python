## **String Functions & Methods in Python**  

### **1️⃣ `len()` - Finding the Length of a String**
#- `len()` is a **general-purpose function** that returns the number of characters in a string.  
#- It works with strings, lists, tuples, etc.  

learn = 'python'
print(len(learn))  # Output: 6 (There are 6 characters in 'python')

### **2️⃣ String Methods Using `.` Operator**  
#Methods specific to strings use **dot notation (`.`)**.  

#### **a) `upper()` - Convert to Uppercase**  
print(learn.upper())  # Output: PYTHON

#### **b) `lower()` - Convert to Lowercase**  
print(learn.lower())  # Output: python

#### **c) `title()` - Capitalizes the First Letter of Each Word**  
print(learn.title())  # Output: Python

#### **d) `find()` - Locating a Character or Substring**  
#- **Returns the index of the first occurrence** of the given character/substring.  
#- **Case-sensitive** (i.e., `'P'` is different from `'p'`).  
print(learn.find('p'))  # Output: 0 (The letter 'p' is at index 0)
print(learn.find('y'))  # Output: 1
print(learn.find('z'))  # Output: -1 (Not found)

#### **e) `replace()` - Replacing Part of a String**  
print(learn.replace('python', 'coding'))  # Output: coding
#- Replaces `'python'` with `'coding'` in the string.  
#- **Does not modify the original string** (strings are immutable).  

## **3️⃣ The `in` Operator - Checking for Substrings**
#- Used to check if a **substring exists in a string**.  
#- Returns **`True`** or **`False`**.  
print('python' in learn)  # Output: True
print('code' in learn)    # Output: False

## **4️⃣ Difference Between `find()` and `in` Operator**  
#| Feature              | `find()`                                | `in` Operator                |
#| **Purpose**          | Finds the index of a substring          | Checks if a substring exists |
#| **Return Type**      | Returns an index (or `-1` if not found) | Returns `True` or `False`    |
#| **Case Sensitivity** | Case-sensitive                          | Case-sensitive               |
#| **Example**          | `"python".find('y') → 1`                | `"y" in "python" → True`     |

## **5️⃣ Difference Between Functions & Methods**  
#| Feature         | Function                             | Method                                 |
#| **Definition**  | A block of code that performs a task | A function that belongs to an object   |
#| **Call Syntax** | `function(argument)`                 | `object.method()`                      |
#| **Works on**    | Can work on multiple data types      | Specific to a data type (like strings) |
#| **Example**     | `len("Python")`                      | `"Python".upper()`                     |
 

learn = 'python'

# General-purpose function
print(len(learn))  # Output: 6

# String methods
print(learn.upper())   # Output: PYTHON
print(learn.lower())   # Output: python
print(learn.title())   # Output: Python

# Find method (case-sensitive)
print(learn.find('p'))  # Output: 0
print(learn.find('z'))  # Output: -1

# Replace method
print(learn.replace('python', 'coding'))  # Output: coding

# 'in' operator
print('python' in learn)  # Output: True
print('code' in learn)     # Output: False
