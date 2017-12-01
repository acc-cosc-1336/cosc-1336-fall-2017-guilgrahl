from tkinter import Tk, Frame
from GUI.main_menu import MainMenu
from GUI.frames.about_frame import AboutFrame
from GUI.frames.course_frame import CourseFrame
from GUI.frames.enrollment_frame import EnrollmentFrame
from GUI.frames.student_frame import StudentFrame

class ContosoApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        Tk.wm_title(self, 'Contoso University')

        self.menubar = MainMenu(self)
        self.config(menu=self.menubar)

        self.frames = {}
        self.__init_frames()

    def __init_frames(self):

        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for frame in (AboutFrame, CourseFrame, EnrollmentFrame, StudentFrame):
            current_frame = frame(container)
            self.frames[frame.__name__] = current_frame
            current_frame.grid(row=0, column=0, sticky='nsew')


    def show_frame(self, frame_name):

        frame = self.frames[frame_name]
        Tk.wm_title(self, 'Contoso University - ' + frame_name.replace('Frame', ''))
        frame.tkraise()



app = ContosoApp()
app.geometry('640x400')
app.mainloop()
