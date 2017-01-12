from mentor import Mentor
from student import Student
from codecoolerror import CodecoolError
import color
from color import colors


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

    def avg_energy(self):
        energy_sum = 0
        for student in self.students:
            energy_sum += student.energy

        return round(energy_sum / len(self.students), 2)

    def avg_knowledge(self):
        skill_sum = 0
        for student in self.students:
            sklii_sum += student.knowledge_level
        return round(skill_sum / len(self.students), 2)

    @classmethod
    def create_local(cls):
        mentors = Mentor.create_by_csv("data/mentors.csv")
        students = Student.create_by_csv("data/students.csv")
        cc_object = CodecoolClass("Miskolc", 2017, mentors, students)
        print(colors['GREEN'] + "School @ Miskolc, in year 2017 is created, with {} mentors and {} students.".format(
            len(mentors), len(students)) + colors['END'])
        return cc_object
