class Person():

    GENDERS = ('male', 'female', 'notsure')

    def __init__(self, first_name=0, last_name=0, year_of_birth=0, gender=0):
        if(first_name == 0):
            raise AttributeError
        else:
            self.first_name = first_name
        if(last_name == 0):
            raise AttributeError
        else:
            self.last_name = last_name
        if(year_of_birth == 0):
            raise AttributeError
        else:
            self.year_of_birth = year_of_birth
        if(gender not in self.GENDERS):
            raise AttributeError
        else:
            self.gender = gender