from person import Person
from codecoolerror import CodecoolError


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
            print("{}'s energy changed from {} to {}.".format(
                self.fullname, self._energy, value))
        self._energy = value
        if self._energy < 1:
            print(self.fullname, "exhausted fatally.")
            self.kill()

    @property
    def knowledge_level(self):
        return self._knowledge_level

    @knowledge_level.setter
    def knowledge_level(self, value):
        if value != 100:
            print("{}'s knowledge level changed from {} to {}.".format(
                self.fullname, self._knowledge_level, value))
        self._knowledge_level = value
        if self._knowledge_level < 1:
            print(self.fullname, "became so stupid that a blackhole formed inside his brain and vanished.")
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
        print("Students are initialized from csv")
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
                print(self.fullname, "died")
                Student.students.remove(Student.students[i])
                break
