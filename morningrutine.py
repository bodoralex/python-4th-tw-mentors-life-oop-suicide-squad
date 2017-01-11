from person import Person
from student import Student


import random


class MorningRoutine:

    # villamos ex, ballábbal felkelés, késés

    @classmethod
    def random_things(cls, persons):
        for person in persons:
            is_unlucky = random.randint(0, 1)
            if is_unlucky:
                accident = 0  # random.randint(0, 3)
                if accident == 0:
                    cls.meets_ex_on_tram(person)
                elif accident == 1:
                    # balláb
                    pass
                elif accident == 2:
                    # késikmertkisiklik
                    pass
                elif accident == 3:
                    # kibicsaklik
                    pass
            elif random.randint(0, 10) == 10:
                student.energy = 9001
            else:
                student.energy = 100

        @classmethod
        def meets_ex_on_tram(cls, person):
            print(person.fullname, "met his/her ex on the tram")
            person.energy -= 33
