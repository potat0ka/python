## **1️⃣ Augmented Assignment Operator (`+=`, `-=`, `*=`, etc.)**  

### **What is an Augmented Assignment Operator?**  
#- It **shortens** an operation that modifies a variable.  
#- Instead of writing `x = x + value`, we write `x += value`.  
#- It **modifies the variable in place** and improves code readability.  

x = 10

# Without augmented assignment
x = x + 11  # x becomes 21

# Using augmented assignment
x += 11  # Same as x = x + 11, now x becomes 32

print(x)  # Output: 32

# **Other Augmented Assignment Operators:**  
#| Operator | Equivalent To    | Example                    |
#| `+=`     | `x = x + value`  | `x += 5` (adds 5)          |
#| `-=`     | `x = x - value`  | `x -= 3` (subtracts 3)     |
#| `*=`     | `x = x * value`  | `x *= 2` (multiplies by 2) |
#| `/=`     | `x = x / value`  | `x /= 4` (divides by 4)    |
#| `//=`    | `x = x // value` | `x //= 2` (floor division) |
#| `%=`     | `x = x % value`  | `x %= 3` (modulus)         |
#| `**=`    | `x = x ** value` | `x **= 2` (exponentiation) |

## **2️⃣ Arithmetic Operations in Python**  

### **Python supports the following arithmetic operators:**  
#| Operator | Description                  | Example   | Output   |
#| `+`      | Addition                     | `10 + 5`  | `15`     |
#| `-`      | Subtraction                  | `10 - 5`  | `5`      |
#| `*`      | Multiplication               | `10 * 5`  | `50`     |
#| `/`      | Division (returns float)     | `10 / 3`  | `3.3333` |
#| `//`     | Floor Division (rounds down) | `10 // 3` | `3`      |
#| `%`      | Modulus (remainder)          | `10 % 3`  | `1`      |
#| `**`     | Exponentiation (power)       | `2 ** 3`  | `8`      |

a = 10
b = 3

print(a + b)   # Output: 13 (Addition)
print(a - b)   # Output: 7 (Subtraction)
print(a * b)   # Output: 30 (Multiplication)
print(a / b)   # Output: 3.3333 (Division)
print(a // b)  # Output: 3 (Floor Division)
print(a % b)   # Output: 1 (Modulus)
print(a ** b)  # Output: 1000 (Exponentiation)

### **Key Takeaways**  
#✔ **Augmented assignment operators** make code shorter and cleaner.  
#✔ **Arithmetic operators** help perform calculations on numbers.  
#✔ **Floor division (`//`)** rounds down to the nearest whole number.  
#✔ **Modulus (`%`)** gives the remainder of a division.  
#✔ **Exponentiation (`**`)** raises a number to a power.  
