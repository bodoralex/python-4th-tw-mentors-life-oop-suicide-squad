from mentor import Mentor
from student import Student
from codecoolerror import CodecoolError
import color
from color import colors

# színek printeléshez
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'


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
        print(colors['GREEN'] + "School @ Miskolc, in year 2017 is created, with {} mentors and {} students.".format(
            len(mentors), len(students)) + colors['END'])
        return cc_object

#ccclass = CodecoolClass.create_local()
