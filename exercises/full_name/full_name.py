class FullName:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self) -> str:
        return(f"Full name is: {self.first_name} {self.last_name}") 
