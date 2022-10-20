from cmath import e
import cv2
import numpy
import os

filterList = []
xmlList = []
path_of_the_directory= '../Modeling/OutputJpg'
print("Files and directories in a specified path:")
for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory,filename)
    if os.path.isfile(f):
        if filename.endswith(".jpg"):
            print(filename)
            filterList.append(filename)
        if filename.endswith(".xml"):
            print(filename)
            xmlList.append(filename)