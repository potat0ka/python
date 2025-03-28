### **User Input & String Concatenation in Python**  
#Python allows users to **input data** using the `input()` function.  

#✅ **Example: Asking for a User’s Name**  

name = input("What is your name? ")  # Takes user input
print("Hi " + name)  # Concatenates and prints a greeting

#💡 **Concatenation** means **joining two or more strings together** using the `+` operator.
### **Exercise: Ask for Name & Favorite Color**  
#**Problem:** Ask for a person's name and favorite color, then print a message like `"Potato likes magenta color"`.

# Taking user input for name and favorite color
name = input("What is your name? ")
color = input("What is your favorite color? ")

# Displaying the output
print(name + " likes " + color + " color.")

### **Understanding String Concatenation**  
#- **Concatenation** means joining two or more strings together using `+`.  
#- Spaces need to be added manually (`"Hi" + name` would print `"HiPotato"` instead of `"Hi Potato"`).  

#✅ **Example of Proper Concatenation:**  
first_name = "John"
last_name = "Smith"
full_name = first_name + " " + last_name  # Adding space manually
print(full_name)  # Output: John Smith

### **Improved Version Using f-Strings (Recommended)**
#A cleaner way to concatenate strings is using **f-strings** (Python 3.6+):

name = input("What is your name? ")
color = input("What is your favorite color? ")

print(f"{name} likes {color} color.")  # f-strings make concatenation easier

#✅ **Why f-strings?**  
#- They are **cleaner** and **more readable** than using `+` for concatenation.  
#- No need to worry about spaces or type conversions.
                        