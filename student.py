class Student:

    def __init__(self, student_id, first_name, last_name, enroll_date):

        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.enroll_date = enroll_date


    def __str__(self):

        return str(self.student_id) + '\t' + self.first_name + ' ' + self.last_name + '\t' + str(self.enroll_date) + '\t'
