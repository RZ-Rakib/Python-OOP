# prompt user for enter age
age = input("Insert age: ")

# Convert the user input from a string to an integer
userAge = int(age)

# Compare the age and print the result
if userAge >= 18:
    print("Adult")
else:
    print("Child")
