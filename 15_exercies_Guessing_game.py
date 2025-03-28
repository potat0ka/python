## **💡 What Does This Code Do?**
#This is a **number guessing game** where:  
#- You **try to guess** a secret number (which is always **9**).  
#- You get **3 chances** to guess it correctly.  
#- The program **helps you** by telling you if your guess is **too high** or **too low**.  
#- If you guess it right, **you win! 🎉**  
#- If you use all 3 attempts without guessing correctly, **you lose! 😢**  

## **🔍 Breaking Down the Code Step by Step**
### 1️⃣ **Setting Up the Game**
secret_no = 9  # Fixed secret number
guess_count = 0
guess_limit = 3

#- The secret number is **always 9**.  
#- You start with **0 guesses** and have **3 attempts** in total.  

### 2️⃣ **Game Instructions**
print("🎯 Welcome to the Number Guessing Game!")
print("🤔 Try to guess the secret number between 1 and 10. You have 3 attempts!")

#- Displays a **welcome message** and explains the game.  

### 3️⃣ **Loop to Take Guesses**
while guess_count < guess_limit:
#```
#- Runs the loop **until you use up all 3 attempts**.  

### 4️⃣ **Taking User Input**
    try:
        guess = int(input(f"Attempt {guess_count + 1}/3 - Guess a number: "))
#- **Asks you to enter a number** and converts it to an integer.  
#- The `try` block **prevents errors** if the user enters something that’s not a number.  

### 5️⃣ **Checking if the Guess is Valid**
        if guess < 1 or guess > 10:
            print("⚠️ Please enter a number between 1 and 10!")
            continue
#- If the guess is **not between 1 and 10**, it **warns** the user and **doesn’t count the attempt**.  

### 6️⃣ **Counting the Guess**
        guess_count += 1
#- **Adds 1** to the number of guesses **each time you guess**.  

### 7️⃣ **Checking if the Guess is Correct**
        if guess == secret_no:
            print("🎉 You Won! Congratulations! 🎊")
            break
#- If the guess is **exactly 9**, the player **wins** 🎉 and the game **stops** (`break`).  

### 8️⃣ **Helping the Player with Hints**
        elif guess < secret_no:
            print("🔼 Too low! Try again.")
        else:
            print("🔽 Too high! Try again.")
#- If the guess is **too low**, it tells the player `"Too low! Try again."`  
#- If the guess is **too high**, it tells the player `"Too high! Try again."`  

### 9️⃣ **Handling Invalid Inputs (Errors)**
    except ValueError:
        print("⚠️ Invalid input! Please enter a number.")
#- If the user enters **letters or symbols** instead of a number, it **warns them** instead of crashing.  

### 🔟 **Game Over Message**
else:
    print(f"😢 Sorry, you lose! The secret number was {secret_no}.")
#- If the player **doesn’t guess the number in 3 attempts**, they **lose** and the program tells them the correct number.  

## **🎯 How to Remember This?**
#1️⃣ **Set a secret number & guesses** → `secret_no = 9, guess_limit = 3`  
#2️⃣ **Loop until guesses run out** → `while guess_count < guess_limit:`  
#3️⃣ **Ask for input & check errors** → `try-except` for invalid inputs  
#4️⃣ **Check if the guess is correct** → `if guess == secret_no:`  
#5️⃣ **Give hints if wrong** → `"Too high" or "Too low"`  
#6️⃣ **End game after 3 tries** → `"You lose! The number was 9."`  


## **🔹 Quick Summary**
#- **You have 3 tries** to guess a secret number (always **9**).  
#- **You get hints** if your guess is too high or too low.  
#- **You can't enter invalid inputs** (e.g., words or symbols).  
#- **If you guess correctly, you win! 🎉**  
#- **If you fail after 3 tries, you lose! 😢**  

## **🎮 Example Runs**
### ✅ **Winning Example**
#🎯 Welcome to the Number Guessing Game!
#🤔 Try to guess the secret number between 1 and 10. You have 3 attempts!
#Attempt 1/3 - Guess a number: 7
#🔼 Too low! Try again.
#Attempt 2/3 - Guess a number: 10
#🔽 Too high! Try again.
#Attempt 3/3 - Guess a number: 9
#🎉 You Won! Congratulations! 🎊

### ❌ **Losing Example**
#🎯 Welcome to the Number Guessing Game!
#🤔 Try to guess the secret number between 1 and 10. You have 3 attempts!
#Attempt 1/3 - Guess a number: 4
#🔼 Too low! Try again.
#Attempt 2/3 - Guess a number: 10
#🔽 Too high! Try again.
#Attempt 3/3 - Guess a number: 6
#😢 Sorry, you lose! The secret number was 9.
 
