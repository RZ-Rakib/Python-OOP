# prompt user to enter input
userString = input("Per Miller's Law, humans can retain ~7 items in short-term memory.\nInsert memorable string: ")

# Check the length of the string and print output
if len(userString) < 7:
    print("This string will be easy to remember.")
else:
    print("This string will be hard to remember.")
