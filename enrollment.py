class Enrollment:

    def __init__(self, enroll_id, student, course):
        self.enroll_id = enroll_id
        self.course = course
        self.student = student
        self.grade = ''
        self.__credit_points = 0


    def setGrade(self, grade):
        self.grade = grade

    def display(self):

        print(str(self.student) + 'Enrollment ID: ' + str(self.enroll_id) + '\t' + str(self.course) + '\t' + 'Grade: ' + self.grade)

    def __str__(self):
        return str(self.student.student_id) + ' ' + self.student.first_name + ' ' + self.student.last_name
