import pygetwindow
import time
import os
import pyautogui
import PIL
import subprocess
from watersolve import watersolver

# get screensize
x,y = pyautogui.size()
print(f"width={x}\theight={y}")

x2,y2 = pyautogui.size()
x2,y2 = int(str(x2)),int(str(y2))
print(x2//2)
print(y2//2)

# also able to edit z3 to specified window-title string like: "Sublime Text (UNREGISTERED)"
my = pygetwindow.getWindowsWithTitle("Offline Games")[0]
# quarter of screen screensize
x3 = x2
y3 = y2
my.resizeTo(x3,y3)
# top-left
my.moveTo(0, 0)
my.activate()
time.sleep(1)

# save screenshot
while True:
    p = pyautogui.screenshot()

    im = p

    pix = im.load()

    arr = []

    for j in range(0, 3):
        arr2 = []
        for i in range(0, 4):
            rgb_tuple = pix[150+160*j,490+50*i]
            rgb_int = rgb_tuple[0] << 16 | rgb_tuple[1] << 8 | rgb_tuple[2]
            if rgb_int == 2695222:
                arr2.append(0)
            else:
                arr2.append(rgb_int) 
        arr.append(arr2)           
            
        
    for j in range(0, 2):
        arr2 = []
        for i in range(0, 4):
            rgb_tuple = pix[150+160*j,800+50*i]
            rgb_int = rgb_tuple[0] << 16 | rgb_tuple[1] << 8 | rgb_tuple[2]
            if rgb_int == 2695222:
                arr2.append(0)
            else:
                arr2.append(rgb_int) 
        arr.append(arr2)    

    print(watersolver(arr))

    for pair in watersolver(arr):
        for point in pair:
            if point < 3:
                pyautogui.click(150+160*point,490)
            else:
                pyautogui.click(150+160*(point-3),800)
            
            time.sleep(0.8)    
    
    pyautogui.moveTo(10, 10)
            
    time.sleep(2)            
            
