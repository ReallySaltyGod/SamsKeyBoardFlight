### File Header ###
# File Name: Sam's Keyboard Flight
# Version:3
# Author: Samuel Smith
# Start Date: 5/1/2025
# Last Updated Date: 5/12
# Use: Flight for Drone code

### Imports ###

from codrone_edu import *
# This imports every thing from codrone

from codrone_edu.drone import Drone
# This brings in the drone class

import time
# this imports time for time.sleep()
import keyboard

from keyboard import *
#import random
# this imports random so you can make random numbers


# Define Objects

drone = Drone() #creates the drone class from Drone()

### --- Key Map --- ###

ForwardButton = "w"
LeftButton = "a"
BackwardButton = "s"
RightButton = "d"
UpButton = "tab"
DownButton = "shift"
LeftTurnButton = "q"
RightTurnButton = "e"
FlipKey = "f"
# Uneditable Keybinds #
"i" # is takeoff
"o" # is land
"esc" # is emergency shutdown
# --- setup --- #

drone.pair()

moving = False
last_pitch = 0
last_roll = 0
last_yaw = 0
last_throttle = 0

while True:
    if keyboard.is_pressed("i"):
        drone.takeoff()

    if keyboard.is_pressed("o"):
        drone.land()




    if keyboard.is_pressed("esc"):
        drone.emergency_stop()
        drone.close()
        quit()

    # Flipping
    Forward = keyboard.is_pressed(ForwardButton)
    Backward = keyboard.is_pressed(BackwardButton)
    Left = keyboard.is_pressed(LeftButton)
    Right = keyboard.is_pressed(RightButton)
    Lturn = keyboard.is_pressed(LeftTurnButton)
    Rturn = keyboard.is_pressed(RightTurnButton)
    Up = keyboard.is_pressed(UpButton)
    Down = keyboard.is_pressed(DownButton)

    if keyboard.is_pressed(FlipKey):
        if Forward:
            drone.flip("front")
        elif Backward:
            drone.flip("back")
        elif Left:
            drone.flip("left")
        elif Right:
            drone.flip("right")
        continue

    # Recalculate pitch and roll
    pitch = 0
    roll = 0
    yaw = 0
    throttle = 0

    if Up:
        throttle += 60
    if Down:
        throttle -= 60

    if Forward:
        pitch += 50
    if Backward:
        pitch -= 50
    if Right:
        roll += 50
    if Left:
        roll -= 50
    if Lturn:
        yaw -= 70
    if Rturn:
        yaw += 70

    # Update drone's pitch and roll settings
    drone.set_pitch(pitch)
    drone.set_roll(roll)
    drone.set_yaw(yaw)
    drone.set_throttle(throttle)
    if pitch != 0 or roll != 0 or yaw != 0 or throttle != 0:
        # If movement changed, refresh move()
        if pitch != last_pitch or roll != last_roll or yaw != last_yaw or throttle != last_throttle or not moving:
            drone.move()
            moving = True
    else:
        if moving:
            drone.set_pitch(0)
            drone.set_roll(0)
            drone.set_yaw(0)
            drone.set_throttle(0)
            drone.move()  # Stops motion
            moving = False

    # Save current movement state
    last_pitch = pitch
    last_roll = roll
    last_yaw = yaw
    last_throttle = throttle
    time.sleep(0.05)
