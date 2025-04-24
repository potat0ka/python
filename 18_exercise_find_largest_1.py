#Write a program to find the largest number in a list.
numbers = [10, 20, 4, 45, 99]
largest = numbers[0]  # Start with the first number
for number in numbers:
    if number > largest:
        largest = number  # Update largest if current number is bigger
print("The largest number is:", largest)
# ### **🔍 Explanation:**
# - We start by assuming the first number is the largest.
# - We loop through each number in the list.
# - If we find a number bigger than our current largest, we update it.
# - Finally, we print the largest number found.
#
# ### **🔍 Output:**
# The largest number is: 99
#