print("===== Student Management System =====")

students = []

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        name = input("Student ka naam: ")
        age = int(input("Student ki age: "))
        course = input("Student ka course: ")
        marks = float(input("Student ke marks: "))

        percentage = marks

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        student = {
            "name": name,
            "age": age,
            "course": course,
            "marks": marks,
            "percentage": percentage,
            "grade": grade
        }

        students.append(student)

        print("\nStudent successfully added!")

    # Show Students
    elif choice == "2":
        if len(students) == 0:
            print("\nNo students found.")
        else:
            print("\n===== All Students =====")

            for student in students:
                print("\nName:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                print("Marks:", student["marks"])
                print("Percentage:", student["percentage"], "%")
                print("Grade:", student["grade"])

    # Search Student
    elif choice == "3":
        search_name = input("Student ka naam search karo: ")
        found = False

        for student in students:
            if student["name"].lower() == search_name.lower():
                print("\n===== Student Found =====")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                print("Marks:", student["marks"])
                print("Percentage:", student["percentage"], "%")
                print("Grade:", student["grade"])

                found = True
                break

        if found == False:
            print("\nStudent not found.")

    # Delete Student
    elif choice == "4":
        delete_name = input("Student ka naam delete karo: ")
        found = False

        for student in students:
            if student["name"].lower() == delete_name.lower():
                students.remove(student)
                print("\nStudent successfully deleted!")
                found = True
                break

        if found == False:
            print("\nStudent not found.")

    # Exit
    elif choice == "5":
        print("\nThank you!")
        break

    else:
        print("\nInvalid choice!")
