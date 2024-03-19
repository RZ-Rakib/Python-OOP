from car import Car

# create main calss to iterate and test the methods
class Main:
    def __init__(self) -> None:
        car1 = Car("Blue", 2010, 120)
        car2 = Car("Green", 2016, 159)

        print(car1.get_color())
        print(car1.get_speed())

if __name__ == "__main__":
    app = Main()