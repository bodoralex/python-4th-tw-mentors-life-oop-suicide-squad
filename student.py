from person import Person
from codecoolerror import CodecoolError


class Student(Person):

    students = []

    def __init__(self, first_name, last_name, year_of_birth, gender, knowledge_level):
        self.knowledge_level = knowledge_level
        super().__init__(first_name, last_name, year_of_birth, gender)

    def __str__(self):
        return self.last_name + " " + self.first_name

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
                raise CodecoolError


"""Student.create_by_csv("data//students.csv")
Student.find_student_by_full_name("Pisti Tóth")"""
