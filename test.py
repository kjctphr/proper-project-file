import os
import glob
from mymodules import *
course = "FHM1234"
course_list = []
course_list_ = []
files = glob.glob(os.path.join("attendance folder",course,"*.txt"))
print(len(files))
for file in files:
    print(file)
    callTXTintoNestedList(file,course_list)
course_list.sort()
print(course_list)
for x in range(0,len(course_list),2):
    course_list_.append([0])


# print(course_list_)
