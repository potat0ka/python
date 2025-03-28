#This program **converts weight** between **pounds (Lbs)** and **kilograms (Kg)** based on user input.

### **1️⃣ Taking User Input**
weight = float(input("Weight: "))  

#- `input("Weight: ")` → Asks the user to **enter their weight**.  
#- `float(...)` → Converts the input from **string** to **float** (so it supports decimal values like `70.5`).  

unit = input("(L)bs or (K)g: ").strip().upper()
#- `input(...)` → Asks the user whether the input is in **pounds (L)** or **kilograms (K)**.  
#- `.strip()` → Removes any **extra spaces** before or after the input.  
#- `.upper()` → Converts the input to **uppercase**, so both `"l"` and `"L"` are treated the same.  

### **2️⃣ Checking the Unit & Converting Weight**
#### ✅ **If User Entered "L" (Weight in Pounds)**
if unit == "L":
    converted = weight * 0.45
    print(f"You are {converted:.2f} kilos.")  
#- If the user **entered "L"** (pounds), we **convert it to kilograms**.  
#- **Formula:** `kg = pounds * 0.45`  
#- `print(f"You are {converted:.2f} kilos.")`  
#- `{converted:.2f}` → Formats the output to **2 decimal places**.  

##### **Example Run**
#Weight: 150
#(L)bs or (K)g: L
#You are 67.50 kilos.

#### ✅ **If User Entered "K" (Weight in Kilograms)**
elif unit == "K":
    converted = weight / 0.45  
    print(f"You are {converted:.2f} pounds.")  
#- If the user **entered "K"** (kilograms), we **convert it to pounds**.  
#- **Formula:** `pounds = kg / 0.45`  
#- Again, it prints the result **formatted to 2 decimal places**.  

##### **Example Run**
#Weight: 68
#(L)bs or (K)g: K
#You are 151.11 pounds.

### **3️⃣ Handling Invalid Input**
else:
    print("Invalid input! Please enter 'L' for pounds or 'K' for kilograms.")
#- If the user enters **something other than "L" or "K"**, it prints an **error message**.  

##### **Example Run**
#Weight: 80

#(L)bs or (K)g: X
#Invalid input! Please enter 'L' for pounds or 'K' for kilograms.

### **🔥 Key Takeaways**
#✅ **Used `float()`** → To allow decimal values for better precision.  
#✅ **Used `.strip().upper()`** → To handle extra spaces & lowercase input.  
#✅ **Used `if-elif-else`** → To check and convert correctly.  
#✅ **Formatted output** → `{converted:.2f}` ensures 2 decimal places.  
#✅ **Handled invalid input** → Prevents errors if users type wrong input.  

