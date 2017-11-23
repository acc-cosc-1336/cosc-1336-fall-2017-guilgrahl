from student import Student
from enrollment import Enrollment
from course import Course
from professor import Professor
from transcript import Transcript


class Gradebook:

    def __init__(self):

        self.professors = {}
         #professor_id   first_name   last_name  hire_date
        p = Professor(1, "Kim", "Abercrombie", "1995-03-11")
        self.professors[p.professor_id] = p

        p = Professor(2, "Fadi", "Fakhouri", "2002-07-06")
        self.professors[p.professor_id] = p

        p = Professor(3, "Roger", "Harui", "1998-07-01")
        self.professors[p.professor_id] = p

        p = Professor(4, "Candace", "Kapoor", "2001-01-15")
        self.professors[p.professor_id] = p

        p = Professor(5, "Roger", "Zheng", "2004-02-12")
        self.professors[p.professor_id] = p


        self.students = {}

        #add to student dictionary
        s = Student(1, "Carson", "Alexander", "09012005")
        self.students[s.student_id] = s
        s = Student(2, "Meredith", "Alonso", "09022002")
        self.students[s.student_id] = s
        s = Student(3, "Arturo", "Anand", "09032003")
        self.students[s.student_id] = s
        s = Student(4, "Gytis", "Barzdukas", "09012001")
        self.students[s.student_id] = s
        s = Student(5, "Peggy", "Justice", "09012001")
        self.students[s.student_id] = s
        s = Student(6, "Laura", "Norman", "09012003")
        self.students[s.student_id] = s
        s = Student(7, "Nino", "Olivetto", "09012005")
        self.students[s.student_id] = s


        self.courses = {}

        #add to course dictionary
        c = Course(1050, "Chemistry", 3, self.professors[1])
        self.courses[c.course_id] = c
        c = Course(4022, "Microeconomics", 3, self.professors[2])
        self.courses[c.course_id] = c
        c = Course(4041, "Macroeconomics", 3, self.professors[3])
        self.courses[c.course_id] = c
        c = Course(1045, "Calculus", 4, self.professors[4])
        self.courses[c.course_id] = c
        c = Course(3141, "Trigonometry", 4, self.professors[5])
        self.courses[c.course_id] = c
        c = Course(2021, "Composition", 3, self.professors[1])
        self.courses[c.course_id] = c
        c = Course(2042, "Literature", 4, self.professors[2])
        self.courses[c.course_id] = c


        self.enrollments = {}

        #add enrolled students into courses
        enroll_id = 11050 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[1], self.courses[1050])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 14022 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[1], self.courses[4022])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 14041 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[1], self.courses[4041])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 21045 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[2], self.courses[1045])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 23141 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[2], self.courses[3141])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 22021 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[2], self.courses[4041])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 31050 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[3], self.courses[1050])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 41050 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[4], self.courses[1050])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 44022 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[4], self.courses[4022])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 54041 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[5], self.courses[2021])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 61045 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[6], self.courses[1045])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 73141 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[7], self.courses[3141])
        self.enrollments[enroll_id] = enrollment



    def update_grade(self):

        enroll_id = int(input('Enter the enrollment ID: '))

        grade = input('Enter the grade: ')

        self.enrollments[enroll_id].setGrade(grade)


    def print_enrollments(self):

        for key in self.enrollments:
            print(self.enrollments[key].display())

    def display_transcript(self):
        student_id = int(input('Please enter student ID: '))
        #Transcript object
        self.transcript = Transcript(self.enrollments, student_id)
        self.transcript.print_transcript()

    def print_gpa(self, student):

        grade = {}
        credit_points_total = 0
        credit_hours_total = 0

        index = 0
        for key in self.enrollments:
            if self.enrollments[key].student.student_id == student:
                #print(key, self.enrollments[key])

                grade[index] = self.enrollments[key].grade
                credit_points_total += self.get_credit_points(grade[index])
                credit_hours_total += self.enrollments[key].course.credit_hour
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
        while selection != 5:
            print('ACADEMIC MAIN MENU')
            print()
            print('1. Update Grade')
            print('2. Print Student GPA')
            print('3. Print Student Transcript')
            print('4. Print All Enrollments')
            print('5. Exit')
            selection = int(input('Selection: '))

            print(selection)

            if selection == 1:
                self.update_grade()

            elif selection == 2:
                student = int(input('Please enter student ID: '))
                print(self.print_gpa(student))

            elif selection == 3:
                self.display_transcript()

            elif selection == 4:
                self.print_enrollments()



gradebook = Gradebook()

gradebook.main()
