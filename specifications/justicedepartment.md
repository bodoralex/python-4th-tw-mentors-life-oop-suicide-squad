# JusticeDepartment

Implemented by Bodor Alex. Has no instantiation.

## Description

This class represents the justice department of the school.

## Parent class

None


## Class methods

### ```random_punishment```

Pick a random punishment from below

#### Arguments 
* ```persons```
  * data_type: list
  * description: student object to punish

#### Return value

None


### ```decapitation```

Simply calls the person's kill() method.

#### Arguments 
* ```person```
  * data_type: student object
  * description: student object to punish

#### Return value

None


### ```punish_presentation```


#### Arguments 
* ```person```
  * data_type: student object

#### Return value

None


### ```pushups```

Takes energy from the person.

#### Arguments 
* ```persons```
  * data_type: student object

#### Return value

None



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