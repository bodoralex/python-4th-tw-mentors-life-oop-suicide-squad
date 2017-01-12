import color
from color import colors


class Pair:

    pairs = []

    def __init__(self, persons):
        self.members = [persons[0], persons[1]]

    @classmethod
    def create_pairs(cls, persons):
        mentor_in_pairs = False
        pairs_to_instantiate = []
        for student in persons.students:
            pairs_to_instantiate.append(student)
            if len(pairs_to_instantiate) == 2:
                cls.pairs.append(Pair(pairs_to_instantiate))
                pairs_to_instantiate.clear()

        if len(pairs_to_instantiate) == 1:
            pairs_to_instantiate.append(persons.mentors[0])
            cls.pairs.append(Pair(pairs_to_instantiate))
            mentor_in_pairs = True
        if mentor_in_pairs:
            print(colors['GREEN'] + "{} pairs gathered, and {} mentor was involved to complete a pair.".format(
                len(cls.pairs), persons.mentors[0].nickname) + colors['END'])
        else:
            print(
                colors['GREEN'] + "{} pairs gathered.".format(len(cls.pairs)) + colors['END'])
        return cls.pairs
