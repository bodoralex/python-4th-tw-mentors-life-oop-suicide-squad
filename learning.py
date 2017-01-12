from person import Person
from student import Student
from codecool_class import CodecoolClass

import random

class Learning:

    @classmethod
    def morning_dojo(cls, persons):
        for person in persons:
            questions = random.randint(0, 4)
            if questions == 0:
                question = random.randint(0, 4)
                if question == 0:
                    cls.question_one(person)
                elif question == 1:
                    cls.question_two(person)
                elif question == 2:
                    cls.question_three(person)
                elif question == 2:
                    cls.question_four(person)              

    @classmethod
    def question_one(cls, person):
        print(person.fullname, "Wrote a lamba function .")
        person.knowledge_level += 5

    @classmethod
    def question_two(cls, person):
        print(person.fullname, "Made some exercises")
        person.knowledge_level += 25

    @classmethod
    def question_three(cls,person):
        print(person.fullname, "Refactoreted a program")
        person.knowledge_level += 50

    @classmethod
    def question_four(cls,person):
        print(person.fullname, "Wrote a cool application")
        person.knowledge_level += 30