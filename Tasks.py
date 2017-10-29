import tkinter
import _thread
import time


class GUI(tkinter.Tk):

    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.shouldPrint = True
        self.initialize()
        _thread.start_new_thread(self.lock_func, ())

    def lock_func(self):
        while True:
            if self.shouldPrint:
                print ("blah")
            else:
                print ("nah")
            time.sleep(1)

    def setShouldPrint(self, value):
        self.shouldPrint = value

    def initialize(self):
        self.processBtn = tkinter.Button(self, text="Process", command = lambda: self.setShouldPrint(True))
        self.stopBtn = tkinter.Button(self, text = "Stop", command = lambda: self.setShouldPrint(False))
        self.processBtn.grid(row = 1)
        self.stopBtn.grid(row = 2)


app = GUI(None)
app.mainloop()