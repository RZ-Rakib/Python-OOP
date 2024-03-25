class Car:
    def __init__(self, color: str) -> None:
        self.color = color
        self.engine_on = False

    def start(self) -> None:
        if self.engine_on:
            print(f"{self.color} is already running.")
        else:
            print(f"{self.color} car started.")
            self.engine_on = True