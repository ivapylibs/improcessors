#=============================== testBasic01_usage ==============================
#
# @brief    Code to create an image interface and then use it to process
#           the source image
#
#=============================== testBasic01_usage ==============================

#
# @file     testBasic01_usage.py
#
# @author   Yunzhi Lin, yunzhi.lin@gatech.edu
# @date     2021/07/07 [created]
#
#!NOTE:
#!  Indent is set to 2 spaces.
#!  Tab is set to 4 spaces with conversion to spaces.
#
# @quit
#=============================== testBasic01_usage ==============================

#==[0] Prep environment
#
import sys
sys.path.append('..')
from improcessor import basic as improcessor
# import improcessor.basic as improcessor
import cv2

Image = cv2.imread('lena.png')
newImage_list = []

#==[1] Create the interface class, you can also try any opencv functions based on the needs
#
improc = improcessor.basic('resize',((400,10),),'clip',((2,100),))

#==[2] Apply the methods
#
newImage_list.append(improc.apply(Image))

#==[3] Reset the methods
#
# improc.set('ignore',True)
improc.set('processing',['clip',((2,20),)])
newImage_list.append(improc.apply(Image))

#==[4] Directly apply the builtin methods
#
newImage_list.append(improcessor.builtin_clip(Image, (2,20)))

#==[5] Disaplay the methods
#
print(improc.get('processing'))

#==[6] Display the results
#
for i in range(len(newImage_list)):
  if newImage_list[i] is not None:
    cv2.imshow('Demo',newImage_list[i])
    cv2.waitKey()
  else:
    print('Error found!')