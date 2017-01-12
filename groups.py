import color
from color import colors

# színek printeléshez
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'


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
            print(colors['GREEN'] + "{} pairs gathered.".format(len(cls.pairs)) + colors['END'])
        return cls.pairs


"""class Group:

    def __init__(self, persons):

    @property
    def overall_energy(self):
        overall_energy = 0
        for person in self.persons:
            if hasattr(person, _energy):
                overall_energy += person._energy
        return overall_energy

    @property
    def avg_energy(self):
        energy_list = []
        for person in self.persons:
            if hasattr(person, _energy):
                energy_list.append(person.energy)
        return sum(energy_list) / len(energy_list)

    @property
    def avg_skill(self):
        skills_levels = []
        pass


class Pair(Group):

    pairs = []

    def __init__(self, persons):
        super().__init__(persons)

    def create_pairs(cls, persons):
        temp_pairs = []
        for i in range(len(persons.students)):
            temp_pairs.append(persons.students[i])
            if len(temp_pairs) == 2:
                Pair.pairs.append(Pair(temp_pairs))
                temp_pairs.clear()
        if len(temp_pairs) == 1:
            temp_pairs.append(persons.mentors[0])
            Pair.pairs.append(Pair(temp_pairs))
        return Pair.pairs"""
