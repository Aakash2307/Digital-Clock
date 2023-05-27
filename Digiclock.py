from tkinter import Tk
from tkinter import Label
import time

clock = Tk()        # clock is the variable to initialize the tk library
clock.title("DIGITAL CLOCK")  # Title of the window

def present_time():      # Function has bee created to make a logic of the present time   
    display_time = time.strftime("%H:%M:%S %p")# here the format of the time is decided by writing %H it comes in 24 hour format and for
    dig.config(text=display_time)   # it config or asks what to display
    dig.after(200, present_time)   # it says my time or program will run after every 200 ms
    
dig = Label(clock, font=("Arial", 150), bg="Yellow", fg="Black") # font decides the writing , bg means background fg means font color
dig.pack()     # fitting all the contents into the window

present_time()

clock.mainloop()     # This will display all the contents of the window
