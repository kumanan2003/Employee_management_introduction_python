def viewemployee(employees):

    if len(employees) == 0:
        print("no employees available!")

    for employee in employees:
        print("---"*4)
        print("Name: ",employee[0])
        print("employee_id: ",employee[1])


    