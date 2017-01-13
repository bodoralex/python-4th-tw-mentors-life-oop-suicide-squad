# Mentor

Implemented by Bodor Alex

## Description
This class contains the mentors.

## Parent class
Person class

## Attributes

All the attributes of the parent class

* ```nickname```
    * data type: string
    * description: contains the nickname of the mentor

## Class methods

### ```create_by_csv```

Creates Mentor instances from a .csv file
The .csv file need to be formatted like this:

    "Laci,Juhász,1999,male,Lacika
     Józsi,Kovács,1000,notsure,Józsibácsi"

#### Arguments
* ```filename```
    * data type: string
    * description: contains the name of the file

#### Return value

The read and instantiated mentor objects in a list. 

### ```find_mentor_by_full_name(cls, full_name)```

Find a Mentor object from the full name

#### Arguments

* ```full_name```
    * data type: string
    * description: the addition of the first name and the last name. For example: "Laci Juhász"

#### Return value

A mentor object


## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None

    def __str__(self):
        return self.fullname

## Instance methods

### ```__str__```


#### Arguments

None

#### Return value

The parent's fullname method.