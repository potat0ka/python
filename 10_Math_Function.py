## **🔹 Math Functions and Math Module in Python**  

### **1️⃣ Built-in Math Functions**  
#Python provides some basic math functions that don’t require importing any module.  

#| **Function**        | **Description**                     | **Example**          |
#| `abs(x)`            | Returns the absolute value of `x`   | `abs(-5) → 5`        |
#| `pow(x, y)`         | Returns `x` raised to the power `y` | `pow(2, 3) → 8`      |
#| `round(x)`          | Rounds `x` to the nearest integer   | `round(3.6) → 4`     |
#| `max(x, y, z, ...)` | Returns the maximum value           | `max(5, 10, 3) → 10` |
#| `min(x, y, z, ...)` | Returns the minimum value           | `min(5, 10, 3) → 3`  |

### **✅ Example: Using Built-in Math Functions**
print(abs(-10))   # Output: 10
print(pow(2, 4))  # Output: 16
print(round(3.7)) # Output: 4
print(max(10, 20, 5)) # Output: 20
print(min(10, 20, 5)) # Output: 5

## **2️⃣ Math Module (`math`)**  
#Python has a **math module** with additional functions for advanced mathematical calculations.  
#To use it, you need to **import** it first:  

import math

### **Commonly Used Math Functions**
#| **Function**                                | **Description**                               | **Example**                     |
#| `math.sqrt(x)`                              | Returns the square root of `x`                | `math.sqrt(25) → 5.0`           |
#| `math.ceil(x)`                              | Rounds `x` up to the nearest integer          | `math.ceil(3.2) → 4`            |
#| `math.floor(x)`                             | Rounds `x` down to the nearest integer        | `math.floor(3.9) → 3`           |
#| `math.factorial(x)`                         | Returns the factorial of `x`                  | `math.factorial(5) → 120`       |
#| `math.fabs(x)`                              | Returns the absolute value of `x` as a float  | `math.fabs(-7) → 7.0`           |
#| `math.log(x)`                               | Returns the natural logarithm (base e) of `x` | `math.log(10)`                  |
#| `math.log10(x)`                             | Returns the base-10 logarithm of `x`          | `math.log10(100) → 2.0`         |
#| `math.sin(x)`, `math.cos(x)`, `math.tan(x)` | Trigonometric functions (input in radians)    | `math.sin(math.pi/2) → 1.0`     |
#| `math.degrees(x)`                           | Converts radians to degrees                   | `math.degrees(math.pi) → 180.0` |
#| `math.radians(x)`                           | Converts degrees to radians                   | `math.radians(180) → 3.14`      |

### **✅ Example: Using the `math` Module**
import math

print(math.sqrt(64))    # Output: 8.0
print(math.ceil(4.2))   # Output: 5
print(math.floor(4.8))  # Output: 4
print(math.factorial(5)) # Output: 120
print(math.log10(1000))  # Output: 3.0
print(math.sin(math.pi/2)) # Output: 1.0

## **3️⃣ Constants in the Math Module**
#| **Constant** | **Value**         |
#| `math.pi`    | 3.141592653589793 |
#| `math.e`     | 2.718281828459045 |

### **✅ Example: Using Constants**
import math

print(math.pi)  # Output: 3.141592653589793
print(math.e)   # Output: 2.718281828459045

## **🔹 Key Takeaways**
#✔ Python has **built-in math functions** for simple calculations (`abs()`, `pow()`, `round()`, etc.).  
#✔ The **math module** provides **advanced** mathematical functions (`sqrt()`, `log()`, `factorial()`, etc.).  
#✔ You need to **import `math`** before using its functions.  
#✔ **Use `math.pi` and `math.e`** for precision in calculations.  

## **🔹 Exercise:**
#🔸 Write a program that asks the user for a number and prints:  
#✔ The **square root** of the number  
#✔ The **factorial** of the number  
#✔ The **log base 10** of the number  
#✔ The **ceiling and floor** of the number  
