

class Transcript:

    def __init__(self, enrollment, student):

        self.enrollments = enrollment
        self.__name = ' '
        self.__course = {}
        self.__grade = {}
        self.__credit_points = {}
        self.__grade_points = {}
        self.__credit_hour_total = 0
        self.__grade_point_total = 0

        index = 0
        for key in self.enrollments:
            if self.enrollments[key].student.student_id == student:
                #print(key, self.enrollments[key])

                self.__course[index] = self.enrollments[key].course
                self.__grade[index] = self.enrollments[key].grade
                self.__credit_hour_total += self.__course[index].credit_hour

                index += 1


                self.__name = self.enrollments[key].student.first_name + ' ' + self.enrollments[key].student.last_name
                #print(self.__name)

        for index in self.__course:
            self.__credit_points[index] = self.get_credit_points(self.__grade[index])
            self.__grade_points[index] = self.__credit_points[index] * self.__course[index].credit_hour
            self.__grade_point_total += self.__grade_points[index]

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

    def get_gpa(self):


        if not(self.__credit_hour_total == 0 or self.__grade_point_total == 0):
            gpa = self.__grade_point_total / self.__credit_hour_total
        else:
            gpa = 0
        
        return gpa

    def print_transcript(self):


        print('Name: ' + self.__name)
        print('Class: ' + 2*'\t' + 'Credit Hours' + '\t' + 'Credit Points' + '\t' + 'Grade Points' + '\t' + 'Grade')

        for index in self.__course:
            print(self.__course[index].title + 2*'\t' + str(self.__course[index].credit_hour) + 2*'\t'  \
                  + 3*'\t' + str(self.__credit_points[index]) + 3*'\t' + str(self.__grade_points[index]) + 3*'\t' + str(self.__grade[index]))

        print(100*'_')
        print(5*'\t' + str(self.__credit_hour_total) + 8*'\t' + str(self.__grade_point_total))
        print('GPA: ' + str(self.get_gpa()))




