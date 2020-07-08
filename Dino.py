#This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
#Please credit me at this URL: https://github.com/CaydendW/

import cv2
import numpy as np
import pyautogui
from pynput.keyboard import Key, Controller
import time

SCREEN_SIZE = (1920, 1200)

fourcc = cv2.VideoWriter_fourcc(*"XVID")

keyboard = Controller()

keyboard.press(Key.up)
keyboard.release(Key.up)

while True:
    img = pyautogui.screenshot(region=(815,71, 75,180))
    frame1 = np.array(img)
    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
    frame = cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)
    bias = 35
    h = 154
    h2 = 135

    place1 = frame[h, 35 - bias]
    place2 = frame[h, 39 - bias]
    place3 = frame[h, 43 - bias]
    place4 = frame[h, 47 - bias]
    place5 = frame[h, 51 - bias]

    place10 = frame[h2, 35 - bias]
    place20 = frame[h2, 39 - bias]
    place30 = frame[h2, 43 - bias]
    place40 = frame[h2, 47 - bias]
    place50 = frame[h2, 51 - bias]

    lookingat = (int(place1) + int(place2) + int(place3) + int(place4) + int(place5)) / 5
    fly = (int(place10) + int(place20) + int(place30) + int(place40) + int(place50)) / 5

    if (lookingat > 250):
        # print(lookingat)
        pass
    elif (lookingat < 250):                                                  
        keyboard.press(Key.up)
        time.sleep(0.1)
        keyboard.release(Key.up)

    if (fly < 250):
        if (lookingat > 250):
            keyboard.press(Key.down)
            time.sleep(0.5)
            keyboard.release(Key.down) 
        
    if cv2.waitKey(1) == ord("q"):
        break
    
    frame1[h, 35 - bias] = np.array([0, 0, 255])
    frame1[h, 39 - bias] = np.array([0, 0, 255])
    frame1[h, 43 - bias] = np.array([0, 0, 255])
    frame1[h, 47 - bias] = np.array([0, 0, 255])
    frame1[h, 51 - bias] = np.array([0, 0, 255])

    frame1[h2, 35 - bias] = np.array([255, 0, 0])
    frame1[h2, 39 - bias] = np.array([255, 0, 0])
    frame1[h2, 43 - bias] = np.array([255, 0, 0])
    frame1[h2, 47 - bias] = np.array([255, 0, 0])
    frame1[h2, 51 - bias] = np.array([255, 0, 0])

    cv2.imshow("thing", frame1)

cv2.destroyAllWindows()
