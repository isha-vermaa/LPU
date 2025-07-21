import os
import json

fil = "employees.json"

sal_map = {
    "Programmer": 25000,
    "Manager": 30000,
    "Tester": 20000
}

def loaddb():
    try:
        if not os.path.exists(fil):
            return []
        with open(fil, "r") as f:
            return json.load(f)
    except Exception as e:
        print("Error reading file:", e)
        return []

def savedb(emp):
    try:
        with open(fil, "w") as f:
            json.dump(emp, f, indent=4)
    except Exception as e:
        print("Error saving file:", e)

def addemp():
    emp = loaddb()
    try:
        nam = input("Enter Name: ").strip()
        age = int(input("Enter Age: "))
        if age < 18 or age > 60:
            raise ValueError("Age must be between 18 and 60.")
        des = input("Enter Designation (Programmer/Manager/Tester): ").strip()
        if any(e['name'].lower() == nam.lower() for e in emp):
            print("Error: Duplicate employee name!")
            return
        if des not in sal_map:
            print("Invalid designation.")
            return
        sal = sal_map[des]
        rec = {
            "name": nam,
            "age": age,
            "designation": des,
            "salary": sal
        }
        emp.append(rec)
        savedb(emp)
        print("Employee added successfully.")
    except ValueError as ve:
        print("Input Error:", ve)
    except Exception as e:
        print("An error occurred:", e)

def showemp():
    emp = loaddb()
    if not emp:
        print("No employees to display.")
        return
    for e in emp:
        print(f"Name: {e['name']}, Age: {e['age']}, Salary: {e['salary']}, Designation: {e['designation']}")

def hikesal():
    emp = loaddb()
    nam = input("Enter the name of employee: ").strip()
    for e in emp:
        if e['name'].lower() == nam.lower():
            try:
                pct = float(input("Enter hike percentage (e.g., 30 for 30%): "))
                inc = e['salary'] * (pct / 100)
                e['salary'] += inc
                savedb(emp)
                print(f"Salary updated. New salary: {e['salary']}")
                return
            except ValueError:
                print("Invalid percentage.")
                return
    print("Employee not found.")

def runmenu():
    while True:
        print("\n==== Employee Management System ====")
        print("1. Create Employee")
        print("2. Display Employees")
        print("3. Raise Salary")
        print("4. Exit")
        ch = input("Enter your choice (1-4): ")
        if ch == "1":
            addemp()
        elif ch == "2":
            showemp()
        elif ch == "3":
            hikesal()
        elif ch == "4":
            print("Thanks for using the application!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    runmenu()