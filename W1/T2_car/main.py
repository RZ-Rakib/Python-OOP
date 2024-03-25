from car import Car

class Main:
    def __init__(self) -> None:
        print(f"Program starting.")
        print(f"Initializing three car objects.")

        car1 = Car("red")
        car2 = Car("green")
        car3 = Car("blue")
        print(f"Car objects initialized.")

        print(f"Starting the first car object.")
        car1.start()
        print(f"Starting the second car object.")
        car2.start()
        print(f"Starting the third car object.")
        car3.start()
        print(f"Starting the third car object.")
        car3.start()

        print(f"Program ending.")

if __name__ == "__main__":
    Main()