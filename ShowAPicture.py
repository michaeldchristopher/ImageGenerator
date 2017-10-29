from tkinter import *
from PIL import Image, ImageTk


root = Tk()

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

w = ws-10 # width for the Tk root
h = hs-10 # height for the Tk root


# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def key(event):
    print ("pressed", repr(event.char))
    if (event.char == 'q'):
        root.quit()

def callback(event):
    print ("clicked at", event.x, event.y)

canvas = Canvas(root,width=400,height=250)
canvas.pack()

root.bind("<Key>", key)
canvas.bind("<Button-1>", callback)

image = Image.open("/Users/Michael/Pictures/koalas.jpeg")
image.thumbnail((400,400))
print(image.size)
photo = ImageTk.PhotoImage(image)
imagesprite = canvas.create_image(0,0,image=photo,anchor="nw")
canvas.image = photo
root.mainloop()