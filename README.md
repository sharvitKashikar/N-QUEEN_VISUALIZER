# N-QUEEN VISUALIZER

*(Previous content of N-QUEEN VISUALIZER, if any, would go here. As no README was provided, assuming a new content piece.)*

## Student Record Management System

This project now includes a simple command-line based student record management system implemented in C++. It allows users to perform basic operations on student data, which is persisted to a file named `student_record.txt`.

### Features

1.  **Add Student**: Allows you to add a new student record including name, roll number, class, and fee.
2.  **View All Records**: Displays all existing student records stored in the system.
3.  **Search Record**: Enables searching for a student record by their name.

### How to Compile and Run

To compile and run the student record system, follow these steps:

1.  **Navigate to the project directory** where `main.cpp` and `Record.h` are located.
2.  **Compile the C++ code** using a g++ compiler:
    ```bash
    g++ main.cpp -o student_records
    ```
3.  **Run the executable**:
    ```bash
    ./student_records
    ```

### Usage

Upon running the program, you will be presented with a menu of options:

```
1. Add Student
2. View Records
3. Search Record
4. Exit
```

Enter the number corresponding to the action you wish to perform.

#### Example: Adding a Student

```
Enter your choice: 1
Enter Student Name: Alice
Enter Roll No.: 101
Enter Class: 12
Enter Fee: 500.00
Student Added Successfully!
```

#### Example: Viewing Records

```
Enter your choice: 2

Student Records:
Name: Alice, Roll No: 101, Class: 12, Fee: 500.00
--------------------------------------------
```

#### Example: Searching for a Record

```
Enter your choice: 3
Enter the name of the student to search: Alice

Student Found:
Name: Alice, Roll No: 101, Class: 12, Fee: 500.00
--------------------------------------------
```

#### Data Persistence

All student records are automatically saved to `student_record.txt` in the same directory as the executable. This file is created if it doesn't exist.