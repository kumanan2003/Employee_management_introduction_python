def viewpatient(patients):

    if len(patients) == 0:
        print("no patients available!")

    for patient in patients:
        print("---"*4)
        print("Name: ",patient[0])
        print("id: ",patient[1])
        print("disease_name: ",patient[2])