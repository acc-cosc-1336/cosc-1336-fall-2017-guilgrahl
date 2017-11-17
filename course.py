class Course:

    def __init__(self, course_id, title, credit_hour):
        self.course_id = course_id
        self.title = title
        self.credit_hour = credit_hour

    def __str__(self):

        return 'Course ID: ' + str(self.course_id) + '\t' + 'Course Title: ' + self.title + '\t' + 'Credit Hour: ' + str(self.credit_hour)

