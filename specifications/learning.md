# Learning

Implemeted by Horváth Fruzsina Enikő

## Description
This class represents the way of the learning in the Codecool.


## Class methods

### ```morning_dojo```

Randomly picks a "question_..." classdefinition to every person in the list. 

#### Arguments

* ```persons```
  * data_type: list
  * description: must contains student objects

#### Return value

None

### ```question/_one```
### ```question/_two```
### ```question/_three```
### ```question/_four``` ################ nincskész

Randomly picks a "question_..." classdefinition to every person in the list. 

#### Arguments

* ```persons```
  * data_type: list
  * description: must contains student objects

#### Return value

```CodecoolClass``` object


## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None

### ```find_student_by_full_name```

Gives back a student with the same full name as the argument from ```students```
#### Arguments
* ```full_name```
  * data_type: string
  * description: holds the full name of the student to be found

#### Return value
```Student``` object

### ```find_mentor_by_full_name```

#### Arguments
* ```full_name```
  * data_type: string
  * description: holds the full name of the mentor to be found

#### Return value
```Mentor``` object


### ```avg_energy```

#### Return value
Average of the students's energy in a class.


### ```avg_knowledge```

#### Arguments

#### Return value
Average of the students's knowledge in a class.