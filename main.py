from mymodules import *
from student_data import *

def main():
    while 1:
        print("Welcome to the UTAR SMART Student Management & Attendance Registration Technology")
        print("")
        print("1. Login as student")
        print("2. Login as admin")

        user_option = input(str("Option : "))
        if user_option == "1":
            auth_student()
        elif user_option == "2":
            auth_admin()
        else:
            print("No valid option was selected")

def auth_student():#login verification
    global id_no , pwd
    student_list = []
    print("")
    print("Student's Login")
    print("")
    id_no = input("Id_no:")
    pwd = input("Password:")
    callTXTintoNestedList("student.txt",student_list)
    std_valid = find_element(id_no,student_list)
    if std_valid != None and student_list[std_valid][2] == pwd:
        student_session()
    else:
        print("\nUser doesn't exist or wrong password!\n")

def auth_admin():
    print("")
    print("Admin Login")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    if username == "admin":
        if password == "password":
            admin_session()
        else:
            print("Incorrect password !")
    else:
        print("Login details not recognised")

def student_session():
    print("")
    print("1. View attendance")



def admin_session():
    print("")
    print("1.CRUD Student data")
    print("CRUD Student Attendance")
    print("Generate Report")
    user_option = input(str("Option : "))
    if user_option == "1":
        student_data()
    elif user_option == "2":
        attendance()
    if user_option == "1":
        report()
    else:
        print("No valid option was selected")


main()


# 1. admin_session()
# -CRUD student data
# -CRUD Attendance
# -Report
# Bar list
# -....
# 2.student_session()
# -View attendance
# 3.flowchart & report
# total  = 5
