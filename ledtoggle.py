from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## Hardware
rled = LED(14)
gled = LED(15)
bled = LED(18)

## Definitions
win = Tk()
win.title("LED Toggle")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

## GUI Commands
def led1Toggle():
    rled.on()
    gled.off()
    bled.off()

def led2Toggle():
    rled.off()
    gled.on()
    bled.off()
        
def led3Toggle():
    rled.off()
    gled.off()
    bled.on()
        
def close():
    RPi.GPIO.cleanup()
    win.destroy()


## Widgets
ledButton1 = Radiobutton(win, text = "Red LED", font = myFont, command = led1Toggle, value = 1)
ledButton1.grid(row=0, column=1)

ledButton2 = Radiobutton(win, text = "Green LED", font = myFont, command = led2Toggle, value = 2)
ledButton2.grid(row=1, column=1)

ledButton3 = Radiobutton(win, text = "Blue LED", font = myFont, command = led3Toggle, value = 3)
ledButton3.grid(row=2, column=1)

exitButton = Button(win, text = "EXIT", font = myFont, command = close, bg = "red", height = 1, width = 24)
exitButton.grid(row=3, column=1)

win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()