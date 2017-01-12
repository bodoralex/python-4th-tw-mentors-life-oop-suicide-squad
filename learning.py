from person import Person
from student import Student
from codecool_class import CodecoolClass

import random


class Learning:
    # pair programming

    @classmethod
    def morning_dojo(cls, persons):
        print("A morning dojo started with {} students.".format(len(persons)))
        for person in persons:
            questions = random.randint(0, 2)
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
            else:
                person.knowledge_level += 5 + random.randint(0, 10)

    @classmethod
    def question_one(cls, person):
        print(person.fullname, "wrote a lamba function .")
        person.knowledge_level += 20

    @classmethod
    def question_two(cls, person):
        print(person.fullname, "was made some exercises")
        person.knowledge_level += 25

    @classmethod
    def question_three(cls, person):
        print(person.fullname, "refactoreted a program")
        person.knowledge_level += 40

    @classmethod
    def question_four(cls, person):
        print(person.fullname, "wrote a cool application")
        person.knowledge_level += 30
