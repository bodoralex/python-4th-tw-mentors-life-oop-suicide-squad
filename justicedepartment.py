from person import Person
from studen import Studen
import random


class JusticeDepatrment:

    @classmethod
    def random_punishment(cls, persons):
        # lista, fekvő, tökönrúgás, lefejezés
        for person in persons:
            punishment_factor = random.randint(0, 100)
            print("{}'s punishment is: ", end='')
            if punishment_factor > 95:
                # lefejezés
                cls.decapitation(person)
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
        print(person.fullname, )
