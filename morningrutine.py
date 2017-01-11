from person import Person
from student import Student


import random


class MorningRoutine:

    # villamos ex, ballábbal felkelés, késés

    @classmethod
    def random_things(cls, persons):
        late_students = []
        for person in persons:
            is_unlucky = random.randint(0, 2)
            if is_unlucky == 2:
                late_students.append(person)
                accident = random.randint(0, 2)
                if accident == 0:
                    cls.meets_ex_on_tram(person)
                elif accident == 1:
                    cls.bad_morning(person)
                elif accident == 2:
                    cls.twisted_ankle(person)
                elif accident == 3:
                    # kibicsaklik
                    pass
            elif not is_unlucky and random.randint(1, 10) >= 8:
                print(person.fullname, "listened to a podcast on the way to school.")
                podcast = 30 + random.randint(-10, 10)
                person.knowledge_level += podcast
                print(person.fullname +
                      "'s knowledge level increased by", str(podcast) + ".")

            elif random.randint(1, 10) == 10:
                print(person.fullname, "became a super saiyan.")
                person.energy = 9001
            else:
                person.energy = 100
        return late_students

    @classmethod
    def meets_ex_on_tram(cls, person):

        if person.gender == "male":
            print(person.fullname, "met his ex on the tram.")
        if person.gender == "female":
            print(person.fullname, "met her ex on the tram.")
        if person.gender == "notsure":
            print(person.fullname, "met its ex on the tram.")
        person.energy -= 33 + random.randint(-10, 10)

    @classmethod
    def bad_morning(cls, person):
        print(person.fullname, "got out of bed on the wrong side.")

        person.energy -= 26 + random.randint(-10, 10)

    @classmethod
    def twisted_ankle(cls, person):
        if person.gender == "male":
            print(person.fullname, "twisted his ankle on his way to school.")
        if person.gender == "female":
            print(person.fullname, "twisted her ankle on her way to school.")
        if person.gender == "notsure":
            print(person.fullname, "twisted its ankle on its way to school.")

        person.energy -= 50 + random.randint(-10, 10)

"""codecool_msc = CodecoolClass.create_local()
print(MorningRoutine.random_things(codecool_msc.students))"""
