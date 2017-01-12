from person import Person
from student import Student
from codecool_class import CodecoolClass

import random


class Breaks:

    @classmethod
    def mass_lunchbreak(cls, persons):

        for student in persons.students:
            cls.lunch_break(student)
        print("The lunchbreak is done, the class average energy became",
              CodecoolClass.avg_energy(persons, "notnull"))

    @classmethod
    def random_breaks(cls, persons):
        for person in persons:
            breaks = random.randint(0, 5)
            if breaks == 0:
                szunet = random.randint(1, 2)
                if szunet == 0:
                    cls.lunch_break(person)
                elif szunet == 1:
                    cls.coffee_break(person)
                elif szunet == 2:
                    cls.pee_break(person)

    @classmethod
    def lunch_break(cls, person):
        #print(person.fullname, "Ohh Yeah! This is lunchtime.")
        person._energy += 30

    @classmethod
    def coffee_break(cls, person):
        print(person.fullname, "goes to the kitchen to drink a coffee.")
        person.energy += 15

    @classmethod
    def pee_break(cls, person):
        print(person.fullname, ": uhh, I have to go to the toilett.")
        person.energy += 7
