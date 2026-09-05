print("===== Student Management System =====")

students = []

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        name = input("Student ka naam: ")
        age = int(input("Student ki age: "))
        course = input("Student ka course: ")
        marks = float(input("Student ke marks (out of 100): "))

        if marks < 0 or marks > 100:
            print("Marks 0 se 100 ke beech hone chahiye.")
            continue

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

        if not found:
            print("\nStudent not found.")

    # Update Student
    elif choice == "4":
        update_name = input("Kis student ko update karna hai? ")
        found = False

        for student in students:
            if student["name"].lower() == update_name.lower():

                print("\nStudent mil gaya!")

                student["name"] = input("New name: ")
                student["age"] = int(input("New age: "))
                student["course"] = input("New course: ")
                marks = float(input("New marks (out of 100): "))

                if marks < 0 or marks > 100:
                    print("Marks 0 se 100 ke beech hone chahiye.")
                    break

                student["marks"] = marks
                student["percentage"] = marks

                if marks >= 90:
                    student["grade"] = "A+"
                elif marks >= 80:
                    student["grade"] = "A"
                elif marks >= 70:
                    student["grade"] = "B"
                elif marks >= 60:
                    student["grade"] = "C"
                elif marks >= 50:
                    student["grade"] = "D"
                else:
                    student["grade"] = "F"

                print("\nStudent successfully updated!")
                found = True
                break

        if not found:
            print("\nStudent not found.")

    # Delete Student
    elif choice == "5":
        delete_name = input("Student ka naam delete karo: ")
        found = False

        for student in students:
            if student["name"].lower() == delete_name.lower():
                students.remove(student)
                print("\nStudent successfully deleted!")
                found = True
                break

        if not found:
            print("\nStudent not found.")

    # Exit
    elif choice == "6":
        print("\nThank you!")
        break

    else:
        print("\nInvalid choice!")
