from tkinter import *
from PIL import Image, ImageTk
import os.path

class GUI():
    def __init__(self):
        self.filename = ""
        self.root = 0
        self.canvas = 0
        self.image = 0
        self.image_id = 0
        self.image_path = None

    def ChooseImage(self, fname):
        fname = self.image_path + fname
        oldfilename = self.filename
        if not os.path.exists(fname): # if it not a file get out
            print("can't open Image: %s " % fname)
            return
        try:
            if (self.image_id != 0):
                self.canvas.delete(self.image_id)
            self.image = Image.open(fname)
            self.image.thumbnail((1200, 1200))
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_id = self.canvas.create_image(0, 0, image=self.photo, anchor="nw")
            self.filename =  fname
            print("Change to Image: %s " % self.filename)
        except:
            self.filename = oldfilename

    def guitask(self):
        self.root.after(100, self.guitask)

    def clickCallback(self, event):
        print("clicked at", event.x, event.y)

    def ShutDown(self):
        self.root.quit()

    def key(self, event):
        print("pressed", repr(event.char))
        if (event.char == 'q'):
            self.root.quit()

    def SpinUpGui(self,picpath=None):
        if picpath == None:
            self.image_path = os.getcwd()
        else:
            self.image_path = os.path.join(picpath, '') # add a backslash if needed

        self.root = Tk()
        self.ws = self.root.winfo_screenwidth()  # width of the screen
        self.hs = self.root.winfo_screenheight()  # height of the screen
        self.w = self.ws - 10  # width for the Tk root
        self.h = self.hs - 10  # height for the Tk root
        # calculate x and y coordinates for the Tk root window
        self.x = (self.ws / 2) - (self.w / 2)
        self.y = (self.hs / 2) - (self.h / 2)
        # set the dimensions of the screen and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
        self.canvas = Canvas(self.root, width=1000, height=1000)
        #self.canvas = Canvas(self.root)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.clickCallback)
        self.root.bind("<Key>", self.key)
        self.ChooseImage('koalas.jpeg') # start with this image
        self.root.after(1000, self.guitask) # poll for changes from network every second
        self.root.mainloop()

if __name__ == '__main__':
    w = GUI()
    w.SpinUpGui()