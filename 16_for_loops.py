## 🔹 **For Loops in Python**

### ✅ What is a For Loop?
#A `for` loop is used to **iterate over a sequence** (like a list, range, or string) and run a block of code **for each item** in that sequence.


### ✅ Syntax of a For Loop:
#for item in sequence:

## 📘 Example 1: Using `range()` with a step
for item in range(1, 11, 2):
    print(item)
### 🔍 Explanation:
#- `range(1, 11, 2)` generates numbers: `1, 3, 5, 7, 9`
#- The third argument `2` is the **step** – it skips every second number.
#- This loop prints only the **odd numbers** between 1 and 10.

## 📘 Example 2: Summing List Items
Prices = [10, 20, 30]
total = 0
for price in Prices:
    total += price
print(f"total: {total}")

### 🔍 Explanation:
#- We loop over the `Prices` list and keep adding each price to `total`.
#- The `+=` operator is an **augmented assignment operator** (you learned this already 😉).
#- After the loop finishes, we print the **total**.

## 💡 Bonus: Using `range()` without step
for i in range(5):
    print(i)
# This prints numbers from `0` to `4` (total 5 numbers).  
# Default step is `1`.

## 🎯 Real-World Mini Project Idea:
#**Grocery Bill Calculator**
items = [50, 30, 100, 20]
total = 0
for item in items:
    total += item
print(f"Your total bill is Rs. {total}")