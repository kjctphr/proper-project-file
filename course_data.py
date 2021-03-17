from mymodules import *
import os
import fileinput

def course_data():
    print("Enter [C] to create a course")
    print("Enter [R] to show course list")
    print("Enter [D] to delete a student")
    print("Enter [Q] to quit")
    print("")

    course_list = []
    callTXTintoNestedList("course.txt",course_list)

    user_option = input(str("Option : ")).upper()
    if user_option == "C":
        session_list = []
        course_name = input("New course name:").upper()
        session_list.append(course_name)
        while True:
            try:
                os.makedirs(course_name)
            except FileExistsError:
                print("Course file existed")
                print("Please enter another course code")
                course_name = input("\nNew course name:").upper()
            else:
                break
        session_type = input("Session type(L/P/T/...):").upper()
        session_length = str(float(input("Session length(if 1 hours and 30 minutes , enter 1.5:)")))
        session_list.append(session_type)
        session_list.append(session_length)
        more = input("More session type?(if yes enter [Y]es ):").upper()
        while more == "Y" or more == "YES":
            session_type = input("Session type(L/P/T/...):").upper()
            session_length = str(float(input("Session length(if 1 hours and 30 minutes , enter 1.5:)")))
            more = input("More session type?(Y/N):").upper()
            session_list.append(session_type)
            session_list.append(session_length)
        else:
            pass
        with open("course.txt","r+") as f:
            session_data = "|".join(session_list)
            f.read().rstrip('\n')  # to avoid blank line while adding new student
            f.write("\n"+session_data)
        print("\nThank You!\n")
        print(f"The course {course_name} has been added to the system\n")

        input("Press Enter to continue")


    elif user_option == "R":
        print('{:<5} | {:<15}| {:<15}| {:<15} '.format("No.", "Student name", "Student id", "Student login password"))
        for count, line in enumerate(student_list, start=1):
            print('{:<5} | {:<15}| {:<15}| {:<15} '.format(count, *line))
        print("")
        input("Press Enter to continue")

    elif user_option == "U":
        print("Change password")
        print('{:<5} | {:<15}| {:<15}| {:<15} '.format("No.", "Student name", "Student id", "Student login password"))
        for count, line in enumerate(student_list, start=1):
            print('{:<5} | {:<15}| {:<15}| {:<15} '.format(count, *line))
        print("")
        name = input("Please Enter the student name that you want to update...").upper()
        std_valid = find_element(name, student_list)
        while std_valid is None:
            print("Student not found")
            name = input("Please enter again!:")
            std_valid = find_element(name, student_list)

        print(f"\nStudent {name} is found")
        old_pwd = input("Please enter the old password for the student:")
        new_pwd = input("Please enter the new password for the student:")
        while old_pwd != student_list[std_valid][2]:
            print("Old password entered is wrong")
            old_pwd = input("Please enter again!:")
        student_list[std_valid][2] = new_pwd
        with open('student.txt', 'w') as file:
            for item in student_list:
                file.write("|".join(map(str, item)))
        print(f"\nStudent {name} 's login password has successfully updated.")
        input("\nPress Enter to continue")

    elif user_option == "D":
        print('{:<5} | {:<15}| {:<15}| {:<15} '.format("No.", "Student name", "Student id", "Student login password"))
        for count, line in enumerate(student_list, start=1):
            print('{:<5} | {:<15}| {:<15}| {:<15} '.format(count, *line))
        print("")
        name = input("Please Enter the student name that you want to delete...").upper()
        std_valid = find_element(name, student_list)
        while std_valid is None:
            print("Student not found")
            name = input("Please enter again!:")
            std_valid = find_element(name, student_list)
        print(f"\nStudent {name} is found")
        delete_a_line("student.txt", name)
        print(f"Student {name} has been deleted from system.")
        input("\nPress Enter to continue")

    elif user_option == "Q":
        pass

    else:
        print("Invalid option.")


course_data()