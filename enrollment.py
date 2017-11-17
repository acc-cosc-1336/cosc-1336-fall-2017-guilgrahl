class Enrollment:

    def __init__(self, enroll_id, student, course):
        self.enroll_id = enroll_id
        self.course = course
        self.student = student
        self.grade = ''


    def setGrade(self, grade):
        self.grade = grade




    def __str__(self):
        
        return str(self.student) + 'Enrollment ID: ' + str(self.enroll_id) + '\t' + str(self.course) + '\t' + 'Grade: ' + self.grade
