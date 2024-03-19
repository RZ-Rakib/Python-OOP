from full_name import FullName

class Main:
    def __init__(self) -> None:
        Users: list[FullName] = [
            FullName("RZ", "Rakib"),
            FullName("Asif", "Niloy")
        ]

        print("All users: ")
        for user in Users:
            print(user.full_name())
        
if __name__ == "__main__":
    app = Main()