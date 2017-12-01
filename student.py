from person import Person

class Student(Person):

    def __init__(self, student_id, first_name, last_name, enroll_date):

        Person.__init__(self, first_name, last_name)
        self.student_id = student_id
        self.enroll_date = enroll_date


    def __str__(self):

        return 'Student ID: ' + str(self.student_id) + ' - ' + str(self.first_name) + ' ' + str(self.last_name) + '\t'

    def display(self):
        print(self.first_name + ' ' + self.last_name)
