import time
import tkinter as tk

isPaused = False
pomodorosElapsed = 0

def togglePaused():
    if isPaused == True:
        isPaused == False
    else:
        isPaused == True

def runTimer():

    countDownFrom = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    displayedText.set("Time to work!")

    while countDownFrom >= 0 and not isPaused:
        hours = 0
        minutes, seconds = divmod(countDownFrom, 60)

        if minutes > 60:
            hours, minutes = divmod(minutes, 60)

        entryHour.set("{0:2d}".format(hours))
        entryMinute.set("{0:2d}".format(minutes))
        entrySecond.set("{0:2d}".format(seconds))

        root.update()
        time.sleep(1)

        if countDownFrom == 0:
            #time is up!
            countDownFrom -= 1

    if(pomodorosElapsed == 4):
        #long break


root = tk.Tk()
root.title("Pomodoro Timer")

hour = tk.StringVar(root, "00")
minute = tk.StringVar(root, "25")
second = tk.StringVar(root, "00")

displayedText = tk.StringVar(root, "")

entryHour = tk.Entry(root, width = 3, font = ("Arial", 20), textvariable = hour)
entryMinute = tk.Entry(root, width = 3, font = ("Arial", 20), textvariable = minute)
entrySecond = tk.Entry(root, width = 3, font = ("Arial", 20), textvariable = second)

title = tk.Label(root, text = "Pomodoro Timer", font = ("Arial", 20)).pack()
message = tk.Label(root, width = 120, font = ("Arial", 20), textvariable = displayedText).pack()

startBtn = tk.Button(root, text = "Start", font = ("Arial", 20), command = runTimer())
pauseBtn = tk.Button(root, text = "Pause", font = ("Arial", 20), command = togglePaused())