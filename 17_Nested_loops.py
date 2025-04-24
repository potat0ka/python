## 🔁 **Nested Loops in Python**

### ✅ What is a Nested Loop?

#A **nested loop** means a loop **inside another loop**.

#It's often used when you need to repeat something **within each step** of a bigger loop.

### 🧠 Example Code:
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
### 🔍 Explanation (Step-by-step):

#1. You have a list called `numbers`:
#
#   [5, 2, 5, 2, 2]
#2. The **outer loop** runs once for each number in the list.
#
#   for x_count in numbers:
#3. For each number (`x_count`), it creates an empty string called `output`.
#4. The **inner loop**:
#
#   for count in range(x_count):
#   ```
#   This runs `x_count` times — and adds an `'x'` to the `output` each time.
#5. Finally, it prints the result:
#
#   print(output)
## 🔢 How the output is generated:
#- First number is `5`: → `'xxxxx'`
#- Second number is `2`: → `'xx'`
#- Third number is `5`: → `'xxxxx'`
#- Fourth number is `2`: → `'xx'`
#- Fifth number is `2`: → `'xx'`
## 🖨 Final Output:
#xxxxx
#xx
#xxxxx
#xx
#xx

### 🧩 Visual Way to Imagine It:

#You’re saying:
#👉 “Hey Python! For each number in my list, draw that many x's.”
# 🎯 Practice Challenge:

#Try printing triangles with stars `*` instead of `x`:
numbers = [1, 2, 3, 4]
for n in numbers:
    output = ''
    for i in range(n):
        output += '*'
    print(output)
### 🔸 Output:
#*
#**
#***
#****