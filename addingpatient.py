def addpatient(patients):
    name = input("Enter patient name: ")
    id = input("Enter id: ")
    disease_name = input("enter the disease: ")

    patient = [name, id, disease_name]

    patients.append(patient)

    print("patient added successfully!")