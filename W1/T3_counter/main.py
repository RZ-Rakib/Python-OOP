from counter import Counter

class Main:
    def __init__(self) -> None:
        print(f"Program starting.")
        print(f"Initializing counter...")

        user_counter = Counter()
        print(f"Counter initialized.\n")

        while True:
            print("Options:")
            print("1) Add count")
            print("2) Get count")
            print("3) Zero count")
            print("0) Exit program")

            user_input = input("Choice: ")

            if user_input == "1":
                user_counter.addCount()
                print(f"Count increased\n")
            elif user_input == "2":
                user_counter.getCount()
                print(f"Current count '{user_counter.getCount()}'\n")
            elif user_input == "3":
                user_counter.zeroCount()
                print(f"Count zeroed\n")
            elif user_input == "0":
                print(f"\nProgram ending.")
                break
            else:
                print("Invalid input, try again.")

if __name__ == "__main__":
    app = Main()