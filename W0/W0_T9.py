try:
    file_name = input("Insert filename to read: ")
    with open(file_name, "r") as file:
        file_content = file.read()
        print(f"#### {file.name} content ####\n{file_content}\n#### {file.name} content ####")
except FileNotFoundError:
    print(f"File '{file_name}' not found.")