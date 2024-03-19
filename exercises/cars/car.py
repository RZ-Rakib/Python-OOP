# creating class for cars
class Car:
    # add __init__ constructor
    def __init__(self, color, year, speed) -> None:
        self.color = color
        self.year = year
        self.speed = speed

    # developer defined color method
    def get_color(self) -> str:
        return (f"The color of the car is {self.color}")
    
    # developer defined model-year method
    def get_model_year(self) -> int:
        return (f"The year of this car's model is {self.year}")
    
    # developer defined speed method
    def get_speed(self) -> float:
        return (f"Car is heading with {self.speed}km/h")