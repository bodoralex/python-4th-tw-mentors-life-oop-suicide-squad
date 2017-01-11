from person import Person
from student import Student
from codecool_class import CodecoolClass

import random


class JusticeDepatrment:

    @classmethod
    def random_punishment(cls, persons):
        # lista, fekvő, tökönrúgás, lefejezés

        for person in persons[::-1]:
            punishment_factor = random.randint(0, 100)
            print("{}'s punishment is: ".format(person.fullname), end="")
            if punishment_factor > 95:
                cls.decapitation(person)
            elif punishment_factor > 50:
                cls.punish_presentation(person)
            else:
                cls.pushups(person)

    @classmethod
    def decapitation(cls, person):
        print("decapitation.")
        person.kill()

    @classmethod
    def punish_presentation(cls, person):
        print("punishment presentation")
        person.energy -= 25 + random.randint(-5, 10)
        person.knowledge_level += 30 + random.randint(0, 20)

    @classmethod
    def pushups(cls, person):
        print("pushups")
        person.energy -= 15 + random.randint(0, 10)


def main():

    codecool_msc = CodecoolClass.create_local()
    #kisclass = [Student("Laci", "Kovacs", 1992, "male", 11)]
    JusticeDepatrment.random_punishment(codecool_msc.students)


if __name__ == "main":
    main()
