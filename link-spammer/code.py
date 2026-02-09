import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import time
import digitalio
from board import *
import random

# config start
start_delay = 10
# Make sure to set this link! This is what will be typed into the adress bar. Requires a \n at the end.
link = "Change me!\n"
# Options are "off", "low", "min", "max". Change to a higher setting if on a slower computer.
slowdown_level = "low"
# config end


# V DEV                      by numycode (original by rocklake)
# DEV
#  |
# \_/
# TPS (tabs per second)      Unknown


kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
def slowdown(level1):
    if level1 == "l":
        if slowdown_level == "low":
            time.sleep(0.05)
        elif slowdown_level == "min":
            time.sleep(0.1)
        elif slowdown_level == "max":
            time.sleep(0.2)
        elif slowdown_level == "off":
            pass
    elif level1 == "m":
        if slowdown_level == "low":
            time.sleep(0.1)
        elif slowdown_level == "min":
            time.sleep(0.2)
        elif slowdown_level == "max":
            time.sleep(0.3)
        elif slowdown_level == "off":
            pass
    elif level1 == "h":
        if slowdown_level == "low":
            time.sleep(0.2)
        elif slowdown_level == "min":
            time.sleep(0.3)
        elif slowdown_level == "max":
            time.sleep(0.4)
        elif slowdown_level == "off":
            pass
cap = kbd.led_on(Keyboard.LED_CAPS_LOCK)
while cap == True:
    exit()
while True:
    time.sleep(start_delay)
    try:
        # main code
        while True:
            slowdown("m")
            kbd.press(Keycode.CONTROL)
            kbd.press(Keycode.T)
            kbd.release_all()
            slowdown("l")

            kbd.press(Keycode.CONTROL)
            kbd.press(Keycode.L)
            kbd.release_all()
            slowdown("l")

            layout.write(link)
            slowdown("l")



    except:
        print("Failed!")
