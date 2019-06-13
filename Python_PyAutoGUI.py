

# ------------------------------------------------------------------------------------------------ #
# PyAutoGUI
# ------------------------------------------------------------------------------------------------ #

import pyautogui as pag
import time


# ------------------------------------------------------------------------------------------------ #
# FAIL SAFE (emergency stop)
# ctrl + alt + del to logoff

# pag.FAILSAFE = True  # the upper left corner fail safe is active
# move mouse to "upper left corner" will produce a stop

# pag.PAUSE = 2        # creates 2 second pause between function calls


# ------------------------------------------------------------------------------------------------ #
# PRINT SCREENS RESOLUTION for reference of x,y coordinates
# print(pag.size())
# (1920, 1080)
# NOTE: upper left = 0,0  lower right = 1919, 1079
# 2-MONITOR SETUP = # (3840, 1080)
# Left monitor upper left = 0,0  Right monitor lower right = 3839, 1079


# ------------------------------------------------------------------------------------------------ #
# GETTING MOUSE POSITION
# print(pag.position())  # (653, 412) wherever cursor is when u run it


# ------------------------------------------------------------------------------------------------ #
# MOVING THE MOUSE
# pag.moveTo(1750, 500, duration=.5)
# pag.moveRel(-200, 100, duration=.125)


# ------------------------------------------------------------------------------------------------ #
# CLICKING THE MOUSE
# pag.click(10, 5)  # x and y coordinates are optional, blank clicks current position


# ------------------------------------------------------------------------------------------------ #
# DRAGGING THE MOUSE

# time.sleep(5)
# pag.click()  # optional: to activate current operating window
# distance = 200
# while distance > 0:
#     pag.dragRel(distance, 0, duration=.25)   # drag right
#     distance = distance -5
#     pag.dragRel(0, distance, duration=.25)   # drag down
#     pag.dragRel(-distance, 0, duration=.25)  # drag left
#     distance = distance -5
#     pag.dragRel(0, -distance, duration=.25)  # drag up


# ------------------------------------------------------------------------------------------------ #
# SCROLLING THE MOUSE

# pag.scroll(200)


# ------------------------------------------------------------------------------------------------ #
# TAKING A SCREENSHOT

# ssh = pag.screenshot()       # Assigns object "ssh" to take a screen shot.
# ssh.getpixel((150, 400))     # (130, 145, 144) RGB tuple returned from ssh.getpixel()
# You can call methods on the Image object "ssh"


# ------------------------------------------------------------------------------------------------ #
# IMAGE RECOGNITION

# pag.locateOnScreen('breadIcon.png')
# (643, 745, 70, 29) 4-integer tuple
# x-coord left edge, y-coord top edge, width and height of first place image was found.

# pag.locateAllOnScreen('breadIcon.png')
# [(643, 745, 70, 29), (1007, 801, 70, 29)]
# If only 1 image is found, returns a list with 1 tuple inside.

# Once this is done you can pass in those 4 coordinates to click the center of the image.
# pag.center(643, 745, 70, 29)  # Returns (678, 759)
# pag.click(678, 759)


# ------------------------------------------------------------------------------------------------ #
# CONTROLLING THE KEYBOARD

# pag.typewrite('This deal is off !  I\'m tired of all the bullshit')
# Prints this string

# SINGLE KEY
# pag.press('4')

# MULTIKEY
# pag.keyDown('shift'); pag.press('4'); pag.keyUp('shift')
# This line presses down SHIFT, presses and releases '4', and then releases SHIFT


# pag.keyDown('ctrl')
# pag.keyDown('c')
# pag.keyUp('c')
# pag.keyUp('ctrl')
# Instead of this use a "hotkey"
# pag.hotkey('ctrl', 'c')  # Presses them in order, and releases them in the REVERSE order.



