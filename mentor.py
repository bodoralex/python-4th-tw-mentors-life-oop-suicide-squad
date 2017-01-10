from person import Person


class Mentor(Person):

    mentors = []

    def __init__(self, first_name, last_name, year_of_birth, gender, nickname):
        self.nickname = nickname
        super().__init__(
            first_name, last_name, year_of_birth, gender)

    @classmethod
    def find_mentor_by_full_name(cls, full_name):
        for obj in cls.mentors:
            if obj.fullname == full_name:
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
        print("Mentors are initialized from csv")


Mentor.create_by_csv("data//mentors.csv")
print(Mentor.mentors)
mentor_lacika = Mentor.find_mentor_by_full_name("Laci Juhász")
print(mentor_lacika)
