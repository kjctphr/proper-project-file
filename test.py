import os
import glob
course = "FHM1234"
files = glob.glob(os.path.join("attendance folder",course,"*.txt"))
for file in files:
    with open(file,"r")as f:
        print(f.readlines()[0])
