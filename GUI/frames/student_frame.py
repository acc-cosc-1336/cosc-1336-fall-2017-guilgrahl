from tkinter import Frame, Label

class StudentFrame(Frame):
    """Frame container for Student screen"""

    def __init__(self, parent, school_db):
        Frame.__init__(self, parent)
        self.school_db = school_db
        Label(self, text='Student Frame').grid(row=0, column=0, sticky='w')
