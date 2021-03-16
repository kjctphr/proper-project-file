from mymodules import *
import os


def attendance():
    print("")
    print("1.Create new attendance file ")
    print("2.Update existing attendance file")
    print("3.Delete attendance file")
    user_option = input(str("Option : "))
    if user_option == "1":
        add_attn()
    elif user_option == "2":
        update_attn()
    elif user_option == "3":
        delete_attn()


def add_attn():
    student_list = []
    callTXTintoNestedList("student.txt", student_list)
    for element in student_list:
        element[2] = ""

    course_name = input("Enter course:").upper()
    session_type = input("Enter session type:").upper()
    file_name = str(course_name + "_" + session_type)
    while True:
        try:
            with open(file_name) as f:
                f.readlines()
        except IOError:
            break
        else:
            print("Attendance file existed")
            print("Please key in another coursename")
            course_name = input("Enter course:").upper()
            session_type = input("Enter session type:").upper()
            file_name = str(course_name + "_" + session_type)
    session_start = input("Enter class start time:")
    session_end = input("Enter class end time:")


    print('{:<5} | {:<15}| {:<15}|{:<25}  '.format("No.", "Student name", "Student id", "Joined time(HH:MM) or just [P]resent/[A]bsent/[L]ate"))
    for count, line in enumerate(student_list, start=1):
        print('{:<5} | {:<15}| {:<15}| '.format(count, *line), end="")
        login_time = (input().strip()).upper()
        while True:
            try:
                if login_time == "P":
                    line[2] = "P"
                elif login_time == "Q":
                    line[2] = "Q"
                elif login_time == "L":
                    line[2] = "L"
                else:
                    line[2] = attendance_status(session_start, session_end, login_time)
            except:
                print("Invalid input.")
                login_time = (input("Please enter again:").strip()).upper()
            else:
                break
    print(student_list)
    with open(file_name, "w") as file:
        for item in student_list:
            file.write("|".join(map(str, item)))

def update_attn():
    course_name = input("Enter course:").upper()
    session_type = input("Enter session type:").upper()
    file_name = str(course_name + "_" + session_type)
    attn_list = []
    while True:
        try:
            callTXTintoNestedList(file_name,attn_list)
        except:
            print("Course file does not exist")
            course_name = input("Enter course:").upper()
            session_type = input("Enter session type:").upper()
            file_name = str(course_name + "_" + session_type)
        else:
            break

    print('{:<5} | {:<15}| {:<15}|{:<25}  '.format("No.", "Student name", "Student id", "Attendance Status"))
    for count, line in enumerate(attn_list, start=1):
        print('{:<5} | {:<15}| {:<15}| {:<5} '.format(count, *line))
    quit =""
    while quit != "Q":
        std_name = input("Please enter the name of the student to update:").upper()
        std = find_element(std_name,attn_list)
        attn_status = input("Please enter [P]resent/[A]bsent/[L]ate...")
        print(std)
        print(attn_list[std][2])
        attn_list[std][2] = attn_status
        with open(file_name, 'w') as file:
            for item in attn_list:
                file.write("|".join(map(str, item)))
        print(f"\nStudent {std_name} 's attendance status has successfully updated.")
        quit = input("\nPress Enter to update another student\nOr else, press [Q]uit.").upper()

def delete_attn():
    print("This is the function used to delete the attendance file for the particular course. ")
    course_name = input("Enter course:").upper()
    session_type = input("Enter session type:").upper()
    file_name = str(course_name + "_" + session_type)
    while True:
        try:
            os.remove(file_name)
        except:
            print("Course file does not exist")
            course_name = input("Enter course:").upper()
            session_type = input("Enter session type:").upper()
            file_name = str(course_name + "_" + session_type)
        else:
            break


attendance()



