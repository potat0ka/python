## 🧾 **2D Lists in Python (Matrix)**

### ✅ What is a 2D List?

#A **2D list** is a list of lists — basically, it's like a **table or a grid** where data is stored in **rows and columns**.

#Think of it like this:

matrix = [
    [1, 2, 3],  # Row 0
    [4, 5, 6],  # Row 1
    [7, 8, 9]   # Row 2
]
#📌 This is a **3x3 matrix**  
#- 3 rows, each with 3 elements (columns)

## 🧪 Code Breakdown
for row in matrix:
    for item in row:
        print(item, end=' ')
    print()

### 🔍 Explanation:

#1. `for row in matrix`:  
#   Loops through each row (which is itself a list)

#2. `for item in row`:  
#   Loops through each number inside that row

#3. `print(item, end=' ')`:  
#   - Prints each number **on the same line**
#   - By default, `print()` moves to a new line, but `end=' '` changes it to print a space instead

#4. `print()` after the inner loop makes sure each row starts on a **new line**

### ✅ Output of the Code:

#1 2 3 
#4 5 6 
#7 8 9 

#Just like a nice grid. ✨

## 🧠 Accessing Elements Directly

#You can access any element like this:  
print(matrix[0][1])  # Output: 2 → first row, second column

## ✏️ Practice Challenge:

# 1. Create a 2x3 matrix with your own numbers.
# 2. Print the sum of all numbers.
# 3. Print only the numbers in the second column.
