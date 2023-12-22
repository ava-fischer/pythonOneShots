import time
import tkinter as tk

def toSeconds(minutes):
    return minutes * 60

def setStartTime():
    global startTime
    startTime = time.time() 

root = tk.Tk()
root.title("Pomodoro Timer")

title = tk.Label(root, text = "Pomodoro Timer", font = ("Arial", 20)).pack()
countDown = tk.Label(root, text = )

startBtn = tk.Button(root, text = "Start", font = ("Arial", 20), command = setStartTime)
pauseBtn = tk.Button(root, text = "Pause", font = ("Arial", 20), command =)

pomodorosElapsed = 0

if(pomodorosElapsed == 4):
