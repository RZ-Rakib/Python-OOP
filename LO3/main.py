from person import Person

def main():
    print("Program starting.")

    print("Creating person...")
    # Create Person object with hardcoded values
    person_object = Person("John", "Doe", 30)
    print("Person created.")

    # Print person's details
    print("Name:", person_object.getFullname())
    print("Age:", person_object.getAge())

    print("Person has now birthday...")
    # Call ageUp method
    age = person_object.getAge()
    person_object.ageUp()

    print("New age:", age + 1)

    print("Program ending.")

if __name__ == "__main__":
    main()
