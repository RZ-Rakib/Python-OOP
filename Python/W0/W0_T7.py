# create a main function fo check the input is valid number or not
def main():
    try:
        user_input_number = float(input("Insert number: "))
        print(f"Inserted value is '{user_input_number}'")
    except ValueError:
        print("Oops! That wasn't a valid number.")

# calling the main function
if __name__ == "__main__":
    main()
