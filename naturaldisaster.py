from person import Person
import random


class NaturalDiasaster:

    @classmethod
    def random_disasters(cls, persons):
        for person in persons:
            is_very_unlucky = random.randint(0, 3)
            if is_very_unlucky == 0:
                disaster = random.randint(0, 4)
                if disaster == 0:
                    cls.earthquake(person)
                elif disaster == 1:
                    cls.blackout(person)
                elif disaster == 2:
                    cls.out_of_coffee(person)
                elif disaster == 3:
                    cls.no_wifi(person)
                elif disaster == 4:
                    cls.pipe_burst(person)
            elif is_very_unlucky > 0:
                print(person.fullname, "enjoyed the shining sun and became empowered.")
                person.energy += 30 + random.randint(-10, 10)

    @classmethod
    def earthquake(cls, person):
        print(person.fullname, "suffered minor injuries from an earthquake.")
        person.energy -= 30 + random.randint(-10, 10)

    @classmethod
    def blackout(cls, person):
        print(person.fullname, "became exhausted while searching for candles during a blackout.")
        person.energy -= 30 + random.randint(-10, 10)

    @classmethod
    def out_of_coffee(cls, person):
        print(person.fullname, "ran out of coffee and could hardly keep his.")
        if person.gender == "male":
            print(person.fullname, "ran out of coffee and could hardly keep his eyes open.")
        if person.gender == "female":
            print(person.fullname, "ran out of coffee and could hardly keep her eyes open.")
        if person.gender == "notsure":
            print(person.fullname, "ran out of coffee and could hardly keep its eyes open.")
        person.energy -= 30 + random.randint(-10, 10)

    @classmethod
    def no_wifi(cls, person):
        print(person.fullname, "had problems with connecting to the WiFi and couldn't keep up with the others.")
        person.knowledge_level -= 30 + random.randint(-10, 10)

    @classmethod
    def pipe_burst(cls, person):
        print(person.fullname, "got soaking wet from a pipe burst and had to go home to change clothes.")
        person.energy -= 30 + random.randint(-10, 10)
        person.knowledge_level -= 30 + random.randint(-10, 10)
