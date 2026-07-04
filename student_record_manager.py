import re

FILE_NAME = "students.txt"

# Email Validation
def validate_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(pattern, email)

# Add Student
def add_student():
    try:
        name = input("Enter Student Name: ")

        age = int(input("Enter Age: "))
        if age <= 0:
            raise ValueError("Age must be greater than 0.")

        department = input("Enter Department: ")
        roll = input("Enter Roll Number: ")

        email = input("Enter Email: ")
        if not validate_email(email):
            raise ValueError("Invalid Email Format!")

        with open(FILE_NAME, "a") as file:
            file.write(f"{name},{age},{department},{roll},{email}\n")

        print("\n✅ Student Record Saved Successfully!\n")

    except ValueError as e:
        print("\n❌ Error:", e)

    except Exception as e:
        print("\n❌ Unexpected Error:", e)

# Read Student Records
def read_students():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

            if not records:
                print("\nNo Records Found.\n")
                return

            print("\n=========== STUDENT RECORDS ===========")

            print("{:<20}{:<8}{:<15}{:<15}{:<30}".format(
                "Name", "Age", "Department", "Roll No", "Email"))

            print("-" * 90)

            for record in records:
                name, age, dept, roll, email = record.strip().split(",")

                print("{:<20}{:<8}{:<15}{:<15}{:<30}".format(
                    name, age, dept, roll, email))

            print()

    except FileNotFoundError:
        print("\nNo Student Records Found.\n")

# Main Menu
while True:

    print("===================================")
    print("     STUDENT RECORD MANAGER")
    print("===================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            read_students()

        elif choice == 3:
            print("\nThank You!\n")
            break

        else:
            print("\nInvalid Choice.\n")

    except ValueError:
        print("\nPlease Enter Numbers Only!\n")