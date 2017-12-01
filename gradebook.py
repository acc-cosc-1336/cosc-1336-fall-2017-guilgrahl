
from transcript import Transcript
from school_initializer import SchoolInitializer
from school_db import SchoolDB

class Gradebook:

    def __init__(self, schooldb):

        self.school_initializer = SchoolInitializer()
        self.students = self.school_initializer.students
        self.courses = self.school_initializer.courses
        self.professors = self.school_initializer.professors
        self.school_db = SchoolDB(self.school_initializer)
        self.schooldb = schooldb



    def update_grade(self):

        enroll_id = int(input('Enter the enrollment ID: '))

        grade = input('Enter the grade: ')

        self.school_db.data[enroll_id].setGrade(grade)

    def display_transcript(self):
        student_id = int(input('Please enter student ID: '))
        #Transcript object
        self.transcript = Transcript(self.school_db.data, student_id)
        self.transcript.print_transcript()

    def print_gpa(self, student):

        grade = {}
        credit_points_total = 0
        credit_hours_total = 0

        index = 0
        for key in self.school_db.data:
            if self.school_db.data[key].student.student_id == student:
                #print(key, self.enrollments[key])

                grade[index] = self.school_db.data[key].grade
                credit_points_total += self.get_credit_points(grade[index])
                credit_hours_total += self.school_db.data[key].course.credit_hour
                index += 1


        if not(credit_hours_total == 0 or credit_points_total == 0):
            gpa = credit_points_total / credit_hours_total
        else:
            gpa = 0

        return gpa


    def get_credit_points(self, letter_grade):

        if letter_grade == 'A':
            number_grade = 4
        elif letter_grade == 'B':
            number_grade = 3
        elif letter_grade == 'C':
            number_grade = 2
        elif letter_grade == 'D':
            number_grade = 1
        else:
            number_grade = 0

        return number_grade


    def main(self):


        selection = 0
        while selection != 6:
            print('ACADEMIC MAIN MENU')
            print()
            print('1. Update Grade')
            print('2. Print Student GPA')
            print('3. Print Student Transcript')
            print('4. Print All Enrollments')
            print('5. Save All Enrollments')
            print('6. Exit')
            selection = int(input('Selection: '))

            #Menu options
            if selection == 1:
                self.update_grade()

            elif selection == 2:
                student = int(input('Please enter student ID: '))
                print(self.print_gpa(student))

            elif selection == 3:
                self.display_transcript()

            elif selection == 4:
               # self.print_enrollments()
                for key in self.school_db.data:
                    print(self.school_db.data[key].display())


            elif selection == 5:
                self.school_db.save_data()


schooldb = SchoolDB(SchoolInitializer())
gradebook = Gradebook(schooldb)

gradebook.main()

