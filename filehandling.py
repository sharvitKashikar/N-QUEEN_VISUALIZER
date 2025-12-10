# Student Record System using File Handling

FILENAME = "students.txt"

def add_student():
    with open(FILENAME, "a") as file:
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")
        file.write(f"{roll},{name},{marks}\n")
    print("✅ Student record added")

def view_students():
    try:
        with open(FILENAME, "r") as file:
            print("\n📄 Student Records")
            for line in file:
                roll, name, marks = line.strip().split(",")
                print(f"Roll: {roll}, Name: {name}, Marks: {marks}")
    except FileNotFoundError:
        print("❌ No records found")

def search_student():
    roll_to_search = input("Enter roll number to search: ")
    found = False
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                roll, name, marks = line.strip().split(",")
                if roll == roll_to_search:
                    print(f"✅ Found: Roll={roll}, Name={name}, Marks={marks}")
                    found = True
                    break
        if not found:
            print("❌ Student not found")
    except FileNotFoundError:
        print("❌ No records file exists")


# -------- Main Program --------
print("📂 Student Record System 📂")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("👋 Exiting system")
        break
    else:
        print("❌ Invalid choice")
