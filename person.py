from codecoolerror import CodecoolError


class Person:

    def __init__(self, first_name, last_name, year_of_birth, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.gender = gender

        if type(first_name) is not str:
            raise CodecoolError("First name is not a string!")

        if type(last_name) is not str:
            raise CodecoolError("Last name is not a string!")

        if type(year_of_birth) is not int:
            raise CodecoolError("Year of birth is not an integer!")

        if gender != "male" and gender != "female" and gender != "notsure":
            raise CodecoolError("Gender is not valid!")

    @property
    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    def its(self):
        if self.gender == "male":
            return "his"
        elif self.gender == "female":
            return "her"
        else:
            return "its"

    def it(self):
        if self.gender == "male":
            return "he"
        elif self.gender == "female":
            return "she"
        else:
            return "it"
