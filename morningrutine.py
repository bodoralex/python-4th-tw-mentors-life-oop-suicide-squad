from person import Person
from student import Student
import random


class MorningRoutine:

    @classmethod
    def random_things(cls, persons):
        late_students = []
        for person in persons:
            if random.randint(0, 2) == 1:
                is_unlucky = random.randint(0, 2)
                if is_unlucky == 2:
                    accident = random.randint(0, 4)
                    if accident == 0:
                        cls.meets_ex_on_tram(person)
                    elif accident == 1:
                        cls.bad_morning(person)
                    elif accident == 2:
                        cls.twisted_ankle(person)
                    elif accident == 3:
                        late_students.append(person)
                        cls.oversleep(person)
                    elif accident == 4:
                        late_students.append(person)
                        cls.hangover(person)

                elif not is_unlucky and random.randint(1, 10) >= 8:
                    print(person.fullname,
                          "listened to a podcast on the way to school.")
                    podcast = 20 + random.randint(-10, 10)
                    person.knowledge_level += podcast

                elif random.randint(1, 10) == 10:
                    print(person.fullname,
                          "had a great sleep and became a super saiyan.")
                    person.energy = 9001
                    person.knowledge_level += 30 + random.randint(0, 10)
                else:
                    person.energy = 100
        return late_students

    @classmethod
    def hangover(cls, person):
        print("{} is hangover, {} will be punished.".format(
            person.fullname, person.it()))
        person.energy -= 30 + random.randint(-5, 20)

    @classmethod
    def oversleep(cls, person):
        print("{} didn't want to wake up in time, {} will be more energized, but {} will be punished too.".format(
            person.fullname, person.it(), person.it()))
        person.energy += 20 + random.randint(5, 10)
        person.knowledge_level -= 6 + random.randint(-5, 5)

    @classmethod
    def meets_ex_on_tram(cls, person):
        print("{} met {} ex on the tram.".format(
            person.fullname, person.its()))

        person.energy -= 33 + random.randint(-10, 10)

    @classmethod
    def bad_morning(cls, person):
        print(person.fullname, "got out of bed on the wrong side.")

        person.energy -= 26 + random.randint(-10, 10)

    @classmethod
    def twisted_ankle(cls, person):
        print("{} twisted {} ankle on {} way to shcool".format(
            person.fullname, person.its(), person.its()))

        person.energy -= 50 + random.randint(-10, 10)
