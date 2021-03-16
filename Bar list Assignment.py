#5-10 stds for one class one course
#12 weeks for each course


#3 = Display barlist (Only listed std who barred)??
  #Calculation :
     #Total hours =(1st week until one week b4 bar list come out)*(each week de total hrs for L&T class )
     #Std attend de hour <0.8 , barred

  #Print BarList content : Std name ,Std ID , Attendance( XX / Total class) ,Status

#4 = Comment : Eg :If students are barred, please submit an appeal letter and/or supporting documents to the respective course leader latest by 3 p.m. on Wednesday of Week 10.
#5 = Button : Exit 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

std_list_week1=[]
#Student list (Just Assume):
#Week1
student_A=["Apple","2001234","8.00am","11.00am","Present"]
std_list_week1.append(student_A)
student_B=["Joanne","2004321","8.00am","11.00am","Present"]
std_list_week1.append(student_B)
student_C=["Ann","2005678","8.00am","11.00am","Present"]
std_list_week1.append(student_C)
student_D=["William","2008765","9.00am","11.00am","Absent"]
std_list_week1.append(student_D)
student_E=["Nick","2009911","8.00am","11.00am","Present"]
std_list_week1.append(student_E)

std_list_week2=[]
#Week2
student_A=["Apple","2001234","9.00am","11.00am","Absent"]
std_list_week2.append(student_A)
student_B=["Joanne","2004321","8.00am","11.00am","Present"]
std_list_week2.append(student_B)
student_C=["Ann","2005678","8.00am","11.00am","Present"]
std_list_week2.append(student_C)
student_D=["William","2008765","8.00am","11.00am","Present"]
std_list_week2.append(student_D)
student_E=["Nick","2009911","8.00am","11.00am","Present"]
std_list_week2.append(student_E)

std_list_week3=[]
#Week3
student_A=["Apple","2001234","8.00am","11.00am","Present"]
std_list_week3.append(student_A)
student_B=["Joanne","2004321","8.00am","11.00am","Present"]
std_list_week3.append(student_B)
student_C=["Ann","2005678","8.00am","11.00am","Present"]
std_list_week3.append(student_C)
student_D=["William","2008765","9.30am","11.00am","Absent"]
std_list_week3.append(student_D)
student_E=["Nick","2009911","8.00am","11.00am","Present"]
std_list_week3.append(student_E)

#Extract student name into a list
std_name=[]
for each_list in std_list_week1:
    name=each_list[0]
    std_name.append(name)
    
print("*"*15,"Welcome to UTAR (Foundation) Bar List System","*"*15)
print("-"*80)

#Assume that only one class and one course involved.
#To check the students are from Foundation's Programme X/Y/P/S 
programme=input("Programme(X,Y,P,S): ")
print("-"*80)
while programme!=0:
    if programme=="X"or programme=="Y"or programme=="P"or programme=="S":
        print("\t\t***Please continue for checking ^^***\n")
        course=input("Course taken: ")
        sess=int(input("Session(YYYYMM): "))
        break
    else:
        print("\t\t***Please reenter the correct programme!***\n")
        programme=input("Programme(X,Y,P,S): ")
   
print("-"*80)

#Form a big list which included all 3 weeks' list
status_list=[]
#Week 1 Status List
week1_status_list=[]

for each_list in std_list_week1:
    status=each_list[4]
    week1_status_list.append(status)

status_list.append(week1_status_list)

#Week 2 Status List
week2_status_list=[]

for each_list in std_list_week2:
    status=each_list[4]
    week2_status_list.append(status)

status_list.append(week2_status_list)

#Week 3 Status List
week3_status_list=[]

for each_list in std_list_week3:
    status=each_list[4]
    week3_status_list.append(status)

status_list.append(week3_status_list)

#Append Student's status into a list
count1=0
std_1_list=[]
for each_list in status_list:
    std1=each_list[0]
    std_1_list.append(std1)
 
for item in std_1_list:
    if item=='Present':
        count1+=1
    else:
        count1+=0

count2=0
std_2_list=[]
for each_list in status_list:
    std2=each_list[1]
    std_2_list.append(std2)
 
for item in std_2_list:
    if item=='Present':
        count2+=1
    else:
        count2+=0

count3=0
std_3_list=[]
for each_list in status_list:
    std3=each_list[2]
    std_3_list.append(std3)
 
for item in std_3_list:
    if item=='Present':
        count3+=1
    else:
        count3+=0

count4=0
std_4_list=[]
for each_list in status_list:
    std4=each_list[3]
    std_4_list.append(std4)
 
for item in std_4_list:
    if item=='Present':
        count4+=1
    else:
        count4+=0

count5=0
std_5_list=[]
for each_list in status_list:
    std5=each_list[4]
    std_5_list.append(std5)
 
for item in std_5_list:
    if item=='Present':
        count5+=1
    else:
        count5+=0
        
####Determine the status either barred or pass form their attendance
tablestatus_list=[]

attendance_std1=count1*3/9
if attendance_std1<0.80:
    
    print("Barred")
    
else:
    print("Pass")

     
#Display status in table form 
print("Number |       Student Name       | Attendance(XX/24) | Status ")
print("-"*80)
for i in range(len(std_name)):
    if i < (len(std_name)):
        print(str(i+1)," " * (5 - len(str(i+1))),"|",
        std_name[i]," " * (23 - len(std_name[i])),"|  ")


        
                        
               
