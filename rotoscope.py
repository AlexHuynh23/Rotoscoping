from lib2to3.pytree import convert
from sqlite3 import Row
from turtle import color
import cv2
import numpy
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

ColorCategory = []
image = cv2.imread(args["image"])
hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
print(hsvImage[0,0])
for i in range(len(hsvImage)):
    for j in range(len(hsvImage[0])):
        FOUND = False
        for lists in ColorCategory:
            if int(hsvImage[i, j][0]) == int(lists[0]):
                # print("%s, %s, %s" % (i, j, hsvImage[i, j][0]))
                lists.append(hsvImage[i, j])
                FOUND == True
                break
        if FOUND == False:
            newList = [int(hsvImage[i, j][0]), hsvImage[i, j]]
            ColorCategory.append(newList)
print(ColorCategory)
print(len(ColorCategory))
for list in ColorCategory:
    for i in range(2, len(list)):
        list[i] = list[1]
cv2.imshow('canvas', hsvImage)
cv2.waitKey(0)