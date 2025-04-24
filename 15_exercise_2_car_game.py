command = ""
car_started = False  # 🔹 Variable to track if the car is running

while True:
    command = input("> ").lower()

    if command == "start":
        if car_started:
            print("Car is already started! 🚗💨")
        else:
            car_started = True
            print("Car Started... Ready to go!")
    
    elif command == "stop":
        if not car_started:
            print("Car is already stopped! 🛑")
        else:
            car_started = False
            print("Car Stopped.")
    
    elif command == "help":
        print("""              
start - To start the car
stop - To stop the car
quit - To exit the program                            
""")

    elif command == "quit":
        break       
    else:
        print("Sorry, I don't understand that...")


#🔥 How It Works
#1️⃣ car_started = False → Keeps track of whether the car is running.
#2️⃣ If user types "start" when the car is already started, it prints "Car is already started!".
#3️⃣ If user types "stop" when the car is already stopped, it prints "Car is already stopped!".
#4️⃣ If "start" is typed for the first time, it starts the car.
#5️⃣ If "stop" is typed after starting, it stops the car.