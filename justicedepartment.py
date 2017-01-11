from person import Person
from student import Student
from codecool_class import CodecoolClass

import random


class JusticeDepatrment:

    @classmethod
    def random_punishment(cls, persons):
        # lista, fekvő, tökönrúgás, lefejezés
        print(persons)

        for person in persons[::-1]:
            print(person)
            punishment_factor = random.randint(0, 100)
            print("{}'s punishment is: ".format(person.fullname), end="")
            if True:  # punishment_factor > 95:
                # lefejezés
                cls.decapitation(person)
                pass
            elif punishment_factor > 80:
                # tökönrúgás
                pass
            elif punishment_factor > 50:
                # lista
                pass
            else:
                # fekvő
                pass

    @classmethod
    def decapitation(cls, person):
        print("decapitation.")
        person.kill()

codecool_msc = CodecoolClass.create_local()
#kisclass = [Student("Laci", "Kovacs", 1992, "male", 11)]
JusticeDepatrment.random_punishment(codecool_msc.students)
