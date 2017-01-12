from person import Person
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


class Mentor(Person):

    mentors = []

    def __init__(self, first_name, last_name, year_of_birth, gender, nickname):
        self.nickname = nickname
        super().__init__(
            first_name, last_name, year_of_birth, gender)

    def __str__(self):
        return self.fullname

    @classmethod
    def find_mentor_by_full_name(cls, full_name):
        for obj in cls.mentors:
            if obj.fullname == full_name:
                print(full_name, "was found in mentors")
                return obj

    @classmethod
    def create_by_csv(cls, filename):
        file = open(filename)
        database = file.readlines()
        for row in database:
            first_name, last_name, year_of_birth, gender, nickname = row.split(
                ",")
            cls.mentors.append(Mentor(first_name, last_name,
                                      int(year_of_birth), gender, nickname.strip()))
        file.close()
        print(colors['GREEN'] + "Mentors are initialized from csv." + colors['END'])
        return Mentor.mentors


"""Mentor.create_by_csv("data//mentors.csv")
print(Mentor.mentors)
mentor_lacika = Mentor.find_mentor_by_full_name("Laci Juhász")"""
