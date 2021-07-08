#=============================== testBasic02_threshold ==============================
#
# @brief    Code to create an image interface and then use it to process
#           the source image (threshold)
#
#=============================== testBasic02_threshold ==============================

#
# @file     testBasic02_threshold.py
#
# @author   Yunzhi Lin, yunzhi.lin@gatech.edu
# @date     2021/07/08 [created]
#
#!NOTE:
#!  Indent is set to 2 spaces.
#!  Tab is set to 4 spaces with conversion to spaces.
#
# @quit
#=============================== testBasic02_threshold ==============================

#==[0] Prep environment
#
import sys
sys.path.append('..')
from improcessor import basic as improcessor
# import improcessor.basic as improcessor
import cv2
import numpy as np

Image = cv2.imread('lena.png')
newImage_list = []

#==[1] Create the interface class and apply the methods
#
improc = improcessor.basic('threshold',(127,255,cv2.THRESH_BINARY))
newImage_list.append(improc.apply(Image)[1])

#==[2] Create the interface class and apply the methods
#
improc = improcessor.basic('operator.ge',(127,))
newImage_list.append(np.array(improc.apply(Image)).astype('uint8')*255)

#==[3] Display the results
#
for i in range(len(newImage_list)):
  if newImage_list[i] is not None:
    cv2.imshow('Demo',newImage_list[i])
    cv2.waitKey()
  else:
    print('Error found!')