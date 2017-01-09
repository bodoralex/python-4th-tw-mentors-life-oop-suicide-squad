from person import Person


class Mentor(Person):

    mentors = []

    def __init__(self, first_name, last_name, year_of_birth, gender, nickname):
        self.nickname = nickname  # lekezelni
        super(Person, self).__init__(
            first_name, last_name, year_of_birth, gender)

    @classmethod
    def find_mentor_by_full_name(self, full_name):
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
                                      year_of_birth, gender, nickname))

            # string = "{} = Mentor('{}', '{}', {}, '{}', '{}')".format(cls.variable_name_gen(
            # nickname), first_name, last_name, year_of_birth, gender, nickname.strip())
            # exec(string)

    @classmethod
    def variable_name_gen(cls, nickname):
        return "mentor_" + cls.apostrophe_del(nickname).lower().strip()

    @classmethod
    def apostrophe_del(cls, nickname):
        letters1 = ["á", "é", "í", "ó", "ö", "ő", "ú", "ü", "ű"]
        letters2 = ["a", "e", "i", "o", "o", "o", "u", "u", "u"]
        result = ""
        for i in range(len(nickname)):
            if nickname[i].lower() in letters1:
                result += letters2[letters1.index(nickname[i])]
            else:
                result += nickname[i]
        return result

Mentor.create_by_csv("data//mentors.csv")
print(Mentor.mentors[0])
mentor_lacika = Mentor.find_mentor_by_full_name("Miklós Beöthy")
