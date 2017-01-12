from person import Person
from codecoolerror import CodecoolError
import color
from color import colors


class Student(Person):

    students = []

    def __init__(self, first_name, last_name, year_of_birth, gender, knowledge_level):
        self._energy = 100
        super().__init__(first_name, last_name, year_of_birth, gender)
        self._knowledge_level = knowledge_level

    def __str__(self):
        return self.fullname

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value):
        if value != 100:
            print(colors['YELLOW'] + "{}'s energy changed from {} to {}.".format(colors['PURPLE'] +
                                                                                 self.fullname + colors['YELLOW'], colors['RED'] + str(self._energy) + colors['YELLOW'], colors['RED'] + str(value) + colors['YELLOW']) + colors['END'])
        self._energy = value
        if self._energy < 1:
            print(colors['PURPLE'] + self.fullname + colors['RED'], "exhausted fatally.")
            self.kill()

    @property
    def knowledge_level(self):
        return self._knowledge_level

    @knowledge_level.setter
    def knowledge_level(self, value):
        if value != 100:
            print(colors['BLUE'] + "{}'s knowledge level changed from {} to {}.".format(colors['PURPLE'] +
                                                                                        self.fullname + colors['BLUE'], colors['RED'] + str(self._knowledge_level) + colors['BLUE'], colors['RED'] + str(value) + colors['BLUE']) + colors['END'])
        self._knowledge_level = value
        if self._knowledge_level < 1:
            print(colors['RED'] +
                  str(self.fullname) + "became so stupid that a blackhole formed inside his brain and vanished." + colors['END'])
            self.kill()

    @classmethod
    def create_by_csv(cls, filename):
        file = open(filename)
        data = file.readlines()
        for row in data:
            first_name, last_name, year_of_birth, gender, knowledge_level = row.strip(
                '\n').split(",")
            cls.students.append(Student(first_name, last_name, int(
                year_of_birth), gender, int(knowledge_level)))
        file.close()
        print(colors['GREEN'] + "Students are initialized from csv." + colors['END'])
        return cls.students

    @classmethod
    def find_student_by_full_name(cls, full_name):
        for obj in cls.students:
            if obj.fullname == full_name:
                print(full_name, "was found in students.")
                return obj
            else:
                raise CodecoolError(full_name + " wasn't found in students.")

    def kill(self):
        for i in range(len(Student.students)):
            if Student.students[i].fullname == self.fullname:
                print(colors['RED'] + "✝✝✝ " + str(self.fullname) + " died. ✝✝✝" + colors['END'])
                Student.students.remove(Student.students[i])
                break
