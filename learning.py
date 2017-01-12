from person import Person
from student import Student
from codecool_class import CodecoolClass

import random


class Learning:

    @classmethod
    def pair_programming(cls, pairs):
        max_improvement = 0
        best_pair = None
        for pair in pairs:
            knowlegde_adjust = random.randint(15, 40)
            if max_improvement < knowlegde_adjust:
                max_improvement = knowlegde_adjust
                best_pair = pair
            energy_adjust = random.randint(10, 30)
            for person in pair.members:
                person._knowledge_level += knowlegde_adjust
                person._energy += energy_adjust
        print("While pair programming the most improved pair was {} and {}.\n\
         Their knowledge levels was increased by {}.".format(best_pair.members[0], best_pair.members[1], max_improvement))
        # mentors knowledge

    @classmethod
    def morning_dojo(cls, persons):
        print("A morning dojo started with {} students.".format(len(persons)))
        for person in persons:
            questions = random.randint(0, 3)
            if questions == 0:
                question = random.randint(0, 4)
                if question == 0:
                    cls.question_one(person)
                elif question == 1:
                    cls.question_two(person)
                elif question == 2:
                    cls.question_three(person)
                elif question == 3:
                    cls.question_four(person)
            else:
                person._knowledge_level += 5 + random.randint(0, 10)
        print("All the other students gain some knowledge.")

    @classmethod
    def question_one(cls, person):
        print(person.fullname, "wrote a lamba function.")
        person.knowledge_level += 20

    @classmethod
    def question_two(cls, person):
        print(person.fullname, "did some exercises.")
        person.knowledge_level += 25

    @classmethod
    def question_three(cls, person):
        print(person.fullname, "refactoreted a program.")
        person.knowledge_level += 40

    @classmethod
    def question_four(cls, person):
        print(person.fullname, "wrote a cool application.")
        person.knowledge_level += 30
