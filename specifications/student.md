# Student

Implemented by Ujfalusi Zsolt

## Description
This class represents Codecool students.

## Parent class
Person class

## Attributes

* ```knowledge_level```
    * data type: integer
    * description: contains the knowledge level of a students
* ```energy_level```
    * data type: int
    * description: stores the energy level of the person 0 - ∞


## Class methods

### ```create_by_csv```

Reads in a list of students and returns it.

#### Arguments

The name of the file.

#### Return value

cls.students


### ```find_student_by_full_name```

Finds a student given its fullname.

#### Arguments

The full name of the student, as string.

#### Return value

Student object.


## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None


### ```kill```

Removes self from the cls.student list.

#### Arguments

None

#### Return value

None


### ```__str__```

Overrides the basic string method.

#### Arguments

None

#### Return value

The Person class's fullname method.


### ```energy(getter)```

#### Arguments

None

#### Return value

self._energy


### ```energy(setter)```

Follows the energy changes of the student objects.

#### Arguments

Assigment

#### Return value

None


### ```knowledge(getter)```

#### Arguments

None

#### Return value

self._knowledge


### ```knowledge(setter)```

Follows the knowledge changes of the student objects.

#### Arguments

Assigment

#### Return value

None