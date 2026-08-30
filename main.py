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

def search_employee():
    employee_id = int(input("Enter Employee ID to search: "))

    for employee in employees:
        if employee["id"] == employee_id:
            print("\nEmployee Found!")
            print("ID:", employee["id"])
            print("Name:", employee["name"])
            print("Department:", employee["department"])
            print("Salary:", employee["salary"])
            return

    print("Employee not found.")

while True:

    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        print("Exitting")
        break

    else:
        print("Invalid choice.")