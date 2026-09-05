print("===== Student Management System =====")

students = []

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

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

    elif choice == "2":
        if len(students) == 0:
            print("\nNo students found.")
        else:
            print("\n===== Student Details =====")

            for student in students:
                print("\nName:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                print("Marks:", student["marks"])
                print("Percentage:", student["percentage"], "%")
                print("Grade:", student["grade"])

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
