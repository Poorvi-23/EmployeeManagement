employees = []


def add_employee():
    employee_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    employee = {
        "id": employee_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    employees.append(employee)

    print("Employee added successfully!")


def view_employees():
    if not employees:
        print("No employees found.")
        return

    for employee in employees:
        print(employee)


while True:

    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")