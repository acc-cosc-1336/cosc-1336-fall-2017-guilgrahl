from tkinter import Frame, Label

class AboutFrame(Frame):
    """Frame container for about screen"""

    def __init__(self, parent):
        Frame.__init__(self, parent)

        Label(self, text='About Frame').grid(row=0, column=0, sticky='w')
