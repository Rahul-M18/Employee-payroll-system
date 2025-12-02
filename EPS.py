import csv
import os

FILE_NAME = "employees.csv"

# creating a file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Basic Salary", "HRA", "DA", "Tax", "Net Salary"])


def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))

    # Salary Calculations
    hra = basic * 0.20    # 20%
    da = basic * 0.15     # 15%
    tax = basic * 0.10    # 10%

    net = basic + hra + da - tax

    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([emp_id, name, basic, hra, da, tax, net])

    print("Employee added successfully!\n")


def view_employees():
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print("\n")


def search_employee():
    search_id = input("Enter Employee ID to Search: ")
    found = False

    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == search_id:
                print("Employee Found:")
                print(row)
                found = True
                break

    if not found:
        print("Employee Not Found!\n")


def delete_employee():
    delete_id = input("Enter Employee ID to Delete: ")
    rows = []
    found = False

    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != delete_id:
                rows.append(row)
            else:
                found = True

    if found:
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Employee Deleted Successfully!\n")
    else:
        print("Employee Not Found!\n")


def menu():
    while True:
        print("\n------ Employee Payroll System ------")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("Exiting... Thank You!")
            break
        else:
            print("Invalid Option! Try again.")


menu()