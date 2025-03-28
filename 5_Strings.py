# Strings & String Slicing in Python

#### **What is a String?**  
#A **string** in Python is a sequence of characters enclosed in:  
#- **Single quotes** → `'hello'`  
#- **Double quotes** → `"hello"`  
#- **Triple quotes** → `'''hello'''` (for multi-line strings)  

text1 = 'Hello'
text2 = "Hello"
text3 = '''Hello'''  # Can be used for multi-line strings

### **Understanding `[]`, `[:]`, and String Indexing**  

#1️⃣ **`[]` (Square Brackets) – Accessing Characters in a String**  
#   - Strings are **indexed** starting from `0`.  
#   - We can use square brackets (`[]`) to access specific characters.  

word = "Python"
print(word[0])  # Output: P (First character)
print(word[3])  # Output: h (Fourth character)
print(word[-1]) # Output: n (Last character)


#2️⃣ **`[:]` (String Slicing) – Extracting Parts of a String**  
#   - We can use **slicing** to extract a part of a string.  
#   - **Syntax:** `string[start:end]`  
#   - **Start index is inclusive, End index is exclusive**  

text = "Python"
print(text[0:2])  # Output: Py (Characters at index 0 and 1)
print(text[2:])   # Output: thon (From index 2 to end)
print(text[:4])   # Output: Pyth (From start to index 3)
print(text[-3:])  # Output: hon (Last 3 characters)

learn = '''python'''
print(learn[0:1])  # Output: p (Only the first character)

#- `learn[0:1]` → Extracts **only the first character** (`p`).  
#- **Since slicing excludes the end index**, only `learn[0]` is included.  

## **Exercise: What will `learn[1:-1]` Output?**  
learn = '''python'''
print(learn[1:-1])

#✅ **Expected Output:**  
#ytho

#**Explanation:**  
#- `learn[1:-1]` starts from index `1` (**y**) and goes up to `-1` (**n** is excluded).  
#- The extracted portion is `"ytho"`.  

### **Summary of Key Points**  
#| Symbol                    | Meaning                   | Example         | Output  |
#| `' '` / `" "` / `''' '''` | Define a string           | `"Hello"`       | `Hello` |
#| `string[index]`           | Access character at index | `"Python"[2]`   | `t`     |
#| `string[start:end]`       | Extract substring         | `"Python"[1:4]` | `yth`   |
#| `string[-1]`              | Access last character     | `"Python"[-1]`  | `n`     |
