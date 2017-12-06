from tkinter import Frame, Label


class CourseFrame(Frame):
    """Frame container for Course screen"""

    def __init__(self, parent, school_db):
        Frame.__init__(self, parent)
        self.school_db = school_db
        Label(self, text='Course Frame').grid(row=0, column=0, sticky='w')
