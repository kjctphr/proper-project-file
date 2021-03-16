import os

file_location = os.path.join('Desktop','Desktop', 'proper project file', '*.py')
print(file_location)
import glob

filenames = glob.glob(file_location)
print(filenames)
