### **Python Code Execution**
#Python executes code **line by line from top to bottom**. This is called **sequential execution**.  

print("I'm potato")  

#- This prints `"I'm potato"` to the console.  
#- The `print()` function is used to display output in Python.  


### **Strings in Python**  
#- **Definition:** A **string** is a sequence of characters enclosed in **single (`'`) or double (`"`) quotes**.  
#- Strings can contain letters, numbers, and symbols.  

#✅ **Example:**  
#text1 = "Hello, world!"  # Using double quotes
#text2 = 'Python is fun!' # Using single quotes
#print(text1)  # Output: Hello, world!
#print(text2)  # Output: Python is fun!

#💡 **Note:** Both `'Hello'` and `"Hello"` are valid strings in Python.  

### **Operators in Python**  
#Operators perform operations on variables and values.  

#✅ **Examples of Basic Operators:**  

a = 10
b = 5

print(a + b)  # Addition: Output → 15
print(a - b)  # Subtraction: Output → 5
print(a * b)  # Multiplication: Output → 50
print(a / b)  # Division: Output → 2.0


### **Expressions in Python**  
#- An **expression** is a piece of code that produces a value.  
#- Expressions can contain numbers, variables, and operators.  

#✅ **Example:**  
x = 5 + 3  # Expression: 5 + 3 produces the value 8
y = x * 2  # Expression: 8 * 2 produces the value 16
print(y)   # Output: 16


#💡 **Key Point:** Expressions always result in a value.

### **Evaluating Statements in Python**  
#- If a statement is inside **quotation marks**, Python treats it as a string.  
#- If it's outside quotation marks, Python evaluates it as an expression.

#✅ **Example:**  
print("5 + 3")  # Output: 5 + 3 (String, no calculation)
print(5 + 3)    # Output: 8 (Evaluated as an expression)


#**VS Code** is lightweight and powerful for Python development. To optimize it:  
#1. **Install Python Extension** (by Microsoft) – Adds IntelliSense, debugging, and linting.  
#2. **Set Up a Virtual Environment**  
#   - Open the terminal (`Ctrl + ~`) and run:       
#     python -m venv venv    
#   - Activate it:  
#     - Windows: `venv\Scripts\activate`  
#     - macOS/Linux: `source venv/bin/activate`  
#3. **Enable Linting & Auto-formatting**  
#   - Install `black` (formatter) and `pylint` (linter):  
#     pip install black pylint
#   - Enable formatting on save in settings (`Ctrl + ,` > Search "Format On Save").  
#4. **Use Jupyter Notebooks** 
#   - Install Jupyter: `pip install notebook`  
#   - Create `.ipynb` files in VS Code for an interactive coding experience.  
#5. **Run Python Files Easily**  
#   - Use `Ctrl + Shift + P` > "Run Python File in Terminal"  
#   - Or click the "▶ Run" button in the top right.🚀