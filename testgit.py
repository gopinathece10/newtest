import cv2
import numpy as np
import os
import pyautogui
import time
from PIL import Image
import tkinter as Tk
import pygetwindow as gw
from pywinauto import *
from pywinauto.win32functions import *
#from skimage.measure import compare_ssim as ssim


#bring QSC viewer into front
app = Application().connect(path=r"C:\Program Files (x86)\QSC\Q-SYS UCI Viewer\uci.exe")
w = app.top_window().set_focus()

if w.has_style(win32defines.WS_MINIMIZE):
    ShowWindow(w.wrapper_object())
else:
    print("QSC viewer not launched")
    SetForegroundWindow(w.wrapper_object())
print("UCI_Viewer_Launched")
pyautogui.sleep(0.5)
pyautogui.screenshot(r'D:\Python_Training\QSC\Test\uci.png')
#print("captured image saved in D:\Python_Training\QSC\Test\uci.png")
pyautogui.sleep(5)

#bring QSC designer into front
#app = Application().connect(path=r"C:\Program Files\QSC\Q-SYS Designer 8.4\Q-Sys Designer.exe")
#w = app.top_window().set_focus()

#if w.has_style(win32defines.WS_MINIMIZE):
#    ShowWindow(w.wrapper_object())
#else:
#    print("QSC designer not launched")
#    SetForegroundWindow(w.wrapper_object())
#print("UCI_designer_Launched")
#pyautogui.sleep(0.5)
#pyautogui.screenshot(r'D:\Python_Training\QSC\Test\designer.png')
#print("captured image saved in D:\Python_Training\QSC\Test\uci.png")
#pyautogui.sleep(5)


img = Image.open(r"D:\Python_Training\QSC\Test\uci.png").convert('L')
left = 350
top = 90
right = 1350
bottom = 682
img_crop = img.crop((left, top, right, bottom))
#img_res.show()
img_crop.save(r"D:\Python_Training\QSC\Test\crop_uci.png")
#designer
#img2 = Image.open(r"D:\Python_Training\QSC\Test\designer.png").convert('L')
#left = 440
#top = 142
#right = 1259
#bottom = 600

#img2_crop = img2.crop((left, top, right, bottom))

#img2_res.show()
#img2_crop.save(r"D:\Python_Training\QSC\Test\crop_designer.png")
# load images
image1 = cv2.imread(r"D:\Python_Training\QSC\Test\crop_uci.png")
image2 = cv2.imread(r"D:\Python_Training\QSC\Test\refer.png.png")
# compute difference
time.sleep(1)

#image1 = cv2.imread(r"D:\Python_Training\QSC\Test\crop_uci.png")
#image2 = cv2.imread(r"D:\Python_Training\QSC\Test\crop_designer.png")
#cv2.destroyAllWindows()
if image1.shape == image2.shape:
    print("The image have same size")
    difference = cv2.subtract(image1, image2)
    b, g, r = cv2.split(difference)
    cv2.imshow("b", b)
    cv2.imshow("g", g)
    cv2.imshow("r", r)
else:
    print("The images have different size")

result = not np.any(difference)

if result is True:
    print("Images are same")
else:
    cv2.imwrite(r"D:\Python_Training\QSC\result.png",difference)
    cv2.imshow("difference", difference)
    print("The images are difference")

