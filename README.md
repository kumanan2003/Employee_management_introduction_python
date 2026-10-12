# Hospital Management System

A simple Python-based Hospital Management System project for managing basic patient and employee records through a menu-driven workflow.

## Features

- **Add patients** by entering their name, ID, and disease.
- **View patient records** with the patient's name, ID, and disease.
- **Add employees** by entering their name and employee ID.
- **View employee records** to display saved employee details.
- **Empty-list handling** to show a message when no patients or employees have been added.

## Tech Stack

- **Language:** Python
- **Interface:** Command-line / console
- **Notebook:** Jupyter Notebook (`Hospital_management.ipynb`)

## Project Structure

```text
Hospital-Management-System/
├── Hospital_management.ipynb   # Main notebook / project workflow
├── addemployees.py              # Adds employee records
├── viewemployee.py              # Displays employee records
├── addingpatient.py             # Adds patient records
└── viewpatient.py               # Displays patient records
```

## How It Works

The project separates record-entry and record-display tasks into small Python functions:

- `addemployee(employees)` collects an employee's name and employee ID, then appends the record to the employee list.
- `viewemployee(employees)` displays employee names and IDs.
- `addpatient(patients)` collects a patient's name, ID, and disease, then appends the record to the patient list.
- `viewpatient(patients)` displays patient names, IDs, and disease names.

The records are stored in Python lists while the program is running. Based on the supplied files, persistent database storage is not implemented.

## Getting Started

### Prerequisites

- Python 3
- Jupyter Notebook or JupyterLab (if you want to run the `.ipynb` file)

### Run the Python files

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the main notebook in Jupyter Notebook/JupyterLab, or import/call the functions from a Python entry-point file.

> **Note:** The supplied `.py` files define functions; they do not start the application on their own. A main script or notebook cell must initialize the lists and call the functions.

### Example usage

```python
employees = []
patients = []

addemployee(employees)
viewemployee(employees)

addpatient(patients)
viewpatient(patients)
```

Import the functions from their respective files before running this example:

```python
from addemployees import addemployee
from viewemployee import viewemployee
from addingpatient import addpatient
from viewpatient import viewpatient
```

## Current Limitations

- Records are held in memory and are lost when the Python process ends.
- The current functions collect input from the console.
- The supplied functionality covers adding and viewing records; editing, deleting, searching, authentication, and database integration are not shown in the supplied files.

## Possible Improvements

- Add a menu-driven main program.
- Connect a database such as SQLite or MySQL for persistent storage.
- Add validation to prevent duplicate IDs and incomplete records.
- Implement search, update, and delete operations.
- Add authentication and role-based access for staff.

## Purpose

This project demonstrates Python functions, lists, console input/output, and basic record management for a hospital setting.
