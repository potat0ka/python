## 🧾 **Lists in Python**

### ✅ What is a List?

#A **list** is a collection of items (values) in a particular order.  
#You can store **strings**, **numbers**, or even **other lists** inside it.

#Lists are **mutable**, meaning you can change their content.

### 🔤 Example List:
name = ['ram', 'shyam', 'mohan']

#This list contains 3 strings. Each item in the list has an **index** starting from 0.

#| Index | Value  |
#|-------|--------|
#| 0     | 'ram'  |
#| 1     | 'shyam'|
#| 2     | 'mohan'|


## 🧪 Code Breakdown

print(name[0])     # prints 'ram'
print(name[-1])    # prints 'mohan' (last item)
print(name[0:2])   # prints ['ram', 'shyam']
print(name[0:])    # prints ['ram', 'shyam', 'mohan']
print(name[:2])    # prints ['ram', 'shyam']
print(name[1:3])   # prints ['shyam', 'mohan']
print(name[::2])   # prints ['ram', 'mohan'] (step of 2)
print(name[2:])    # prints ['mohan']

## 🧠 Explanation of List Slicing

### 🎯 `list[start:stop]`  
#Returns items from index `start` to `stop-1`

#- `name[0:2]` → from index 0 to 1 → `['ram', 'shyam']`
#- `name[1:3]` → from index 1 to 2 → `['shyam', 'mohan']`

### 🎯 `name[::step]`
#- Returns every **step**-th item.
#- `name[::2]` → `['ram', 'mohan']`

### 🎯 Negative Indexing
#- `name[-1]` → last item in the list (`'mohan'`)
#- `name[-2]` → second last item

## ✏️ Practice Challenge:

fruits = ['apple', 'banana', 'cherry', 'date', 'fig']

# 1. Print the first and last fruit
# 2. Print the first 3 fruits
# 3. Print fruits starting from 2nd item
# 4. Print every second fruit
