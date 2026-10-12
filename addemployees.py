def addemployee(employees):
    name = input("enter your name: ")
    employee_id = input("enter your employeeid: ")

    employee = [name,employee_id]

    employees.append(employee)

    print("employee added successfully!")