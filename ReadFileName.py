from PIL import Image
import glob
import cv2
import os
import re # get file name


path = 'C:/Users/Admin/PythonLession/CarPlate/images/Bienxemay/*.*'
for file in glob.glob(path):
    img = Image.open(file)
    filename = img.filename
    print(filename)
# Remove File Name from path
    file_name1 = os.path.basename(filename)
    print(file_name1)
# Remove name for file Ex test.txt   , Result = test
    pattern = '[\w-]+?(?=\.)'
    # searching the pattern
    a = re.search(pattern, file_name1)
    # printing the match
    print(a.group())





    img = cv2.imread(file)
    cv2.imshow(str(file_name1), img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()




# Open an image
'''
img = Image.open("output.png")

# Get image file name
filename = img.filename
print(filename)


#=-------------------
from pathlib import Path

file_path = 'C:/Users/test.txt'

# stem attribute extracts the file
# name
print(Path(file_path).stem)  # Answer test

# name attribute returns full name
# of the file
print(Path(file_path).name)  # test.txt

#----------------------
import re

file_path = 'C:/Users/test.txt'
pattern = '[\w-]+?(?=\.)'

# searching the pattern
a = re.search(pattern, file_path)

# printing the match
print(a.group())


'''