from person import Person
import random
import color
from color import colors


class NaturalDiasaster:

    @classmethod
    def random_disasters(cls, persons):
        is_very_unlucky = random.randint(1, 10)
        if is_very_unlucky <= 2:
            disaster = random.randint(0, 1)
            if disaster == 0:
                cls.earthquake(persons)
            elif disaster == 1:
                cls.blackout(persons)
        for person in persons:
            is_mildly_unlucky = random.randint(1, 10)
            if is_mildly_unlucky <= 2:
                disaster = random.randint(2, 4)
                if disaster == 2:
                    cls.out_of_coffee(person)
                elif disaster == 3:
                    cls.no_wifi(person)
                elif disaster == 4:
                    cls.pipe_burst(person)
            elif is_mildly_unlucky >= 9:
                print(person.fullname, "enjoyed the shining sun and became empowered.")
                person.energy += 30 + random.randint(-10, 10)

    @classmethod
    def earthquake(cls, persons):
        print(colors['CYAN'] + "There was an earthquake, but luckily everybody got through it with minor injuries.")
        for person in persons:
            person._energy -= 30
        print("Everyone's energy level descended by" + colors['RED'] + " 30" + colors['END'])

    @classmethod
    def blackout(cls, persons):
        print(colors['CYAN'] + "Everybody got exhausted while searching for candles during a blackout.")
        for person in persons:
            person._energy -= 30
        print("Everyone's energy level descended by" + colors['RED'] + " 30" + colors['END'])

    @classmethod
    def out_of_coffee(cls, person):
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
