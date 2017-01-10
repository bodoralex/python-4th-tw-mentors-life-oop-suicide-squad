from mentor import Mentor
from student import Student
from codecoolerror import CodecoolError


class CodecoolClass:

    def __init__(self, location, year, mentors, students):
        try:
            self.location = location
            self.year = int(year)
            self.mentors = mentors
            self.students = students
        except:
            raise CodecoolError

    def find_mentor_by_full_name(self, full_name):
        for obj in self.mentors:
            if obj.fullname == full_name:
                print(full_name, "was found in mentors")
                return obj

    def find_student_by_full_name(self, full_name):
        for obj in self.mentors:
            if obj.fullname == full_name:
                print(full_name, "was found in mentors")
                return obj

    @classmethod
    def create_local(cls):
        mentors = Mentor.create_by_csv("data/mentors.csv")
        students = Student.create_by_csv("data/students.csv")
        cc_object = CodecoolClass("Miskolc", 2017, mentors, students)
        print("School @ Miskolc, in year 2017 is created, with {} mentors and {} students".format(
            len(mentors), len(students)))
        return cc_object

#ccclass = CodecoolClass.create_local()
