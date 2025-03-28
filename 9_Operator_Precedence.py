## **🔹 Operator Precedence in Python**  

### **What is Operator Precedence?**  
#- **Operator precedence** determines the order in which expressions are evaluated.  
#- Some operations have higher priority than others.  
#- Python follows **BODMAS** (Brackets, Orders, Division/Multiplication, Addition/Subtraction).  

## **🔹 Operator Precedence Table**
#| **Precedence**  | **Operator**                     | **Description**                                   |
#| **1 (Highest)** | `()`                             | Parentheses (grouping)                            |
#| **2**           | `**`                             | Exponentiation (power)                            |
#| **3**           | `+x`, `-x`, `~x`                 | Unary plus, minus, bitwise NOT                    |
#| **4**           | `*`, `/`, `//`, `%`              | Multiplication, Division, Floor Division, Modulus |
#| **5**           | `+`, `-`                         | Addition, Subtraction                             |
#| **6**           | `<<`, `>>`                       | Bitwise shift                                     |
#| **7**           | `&`                              | Bitwise AND                                       |
#| **8**           | `^`                              | Bitwise XOR                                       |
#| **9**           | `|`                              | Bitwise OR                                        |
#| **10**          | `==`, `!=`, `>`, `<`, `>=`, `<=` | Comparison operators                              |
#| **11**          | `not`                            | Logical NOT                                       |
#| **12**          | `and`                            | Logical AND                                       |
#| **13 (Lowest)** | `or`                             | Logical OR                                        |


## **🔹 Examples of Operator Precedence**

### **✅ Example 1: Parentheses First**
result = (2 + 3) * 4  # Parentheses executed first
print(result)  # Output: 20
#✔ **Explanation**: `(2 + 3)` is evaluated first → `5 * 4 = 20`.

### **✅ Example 2: Exponentiation Before Multiplication**
result = 2 ** 3 * 4
print(result)  # Output: 32
#✔ **Explanation**: `2 ** 3` is evaluated first → `8 * 4 = 32`.

### **✅ Example 3: Multiplication Before Addition**
result = 2 + 3 * 4
print(result)  # Output: 14
#✔ **Explanation**: `3 * 4 = 12`, then `2 + 12 = 14`.

### **✅ Example 4: Division Before Subtraction**
result = 10 - 4 / 2
print(result)  # Output: 8.0
#✔ **Explanation**: `4 / 2 = 2.0`, then `10 - 2 = 8.0`.

### **✅ Example 5: Logical Operators Precedence**
result = True or False and False
print(result)  # Output: True
#✔ **Explanation**: `and` has **higher precedence** than `or`, so `False and False = False`, then `True or False = True`.

## **🔹 How to Control Precedence?**
#- Use **parentheses `()`** to make the order **clear and readable**.
result = (2 + 3) * (4 ** 2)  # Easier to read
print(result)  # Output: 80

## **🔹 Key Takeaways**
#✔ **Parentheses `()` have the highest precedence** → Always executed first.  
#✔ **Exponentiation (`**`) is evaluated before multiplication or division.**  
#✔ **Multiplication (`*`), division (`/`), and modulus (`%`) come before addition/subtraction (`+`, `-`).**  
#✔ **Logical AND (`and`) is evaluated before OR (`or`).**  
#✔ **Use parentheses to make code clearer and avoid confusion.**  
