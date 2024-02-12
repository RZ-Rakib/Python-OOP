# Initialize the current value
currentValue = 0.0

# Print the initial current value
print(f"Current value {currentValue}")

# while-loop
userInput = input("Add number(empty stops): ")

while userInput != "":
    try:
        number = float(userInput)
        currentValue += number
        print(f"Current value {currentValue}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Prompt user to enter another number
    userInput = input("Add number(empty stops): ")

# Print the final value
print(f"Final value {currentValue}")
