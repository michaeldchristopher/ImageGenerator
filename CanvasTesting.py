from tkinter import *
import time

master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(2, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")

time.sleep(1)

xy = (0, 0, 200, 100)

new_xy = (0, 0, 100, 100)


i = w.create_line(xy, fill="red")

time.sleep(1)
w.coords(i, new_xy) # change coordinates
time.sleep(1)
w.itemconfig(i, fill="blue") # change color
time.sleep(1)
w.delete(i) # remove
time.sleep(1)

mainloop()

