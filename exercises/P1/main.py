from file_handler import FileHandler
class Main:
    def __init__(self) -> None:
        print("Program starting...")
        # initialize
        file_name = input('File name: ')
        inventory_file = FileHandler(file_name)
        rows = inventory_file.read()
        # operate
        print(f'#### {file_name} ####')
        for row in rows:
            print(row)
        print(f'#### {file_name} ####')
        # cleanup
        print("program ending...")
        return None
    
if __name__ == "__main__":
    app = Main()