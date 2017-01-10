# Person

## Description
This class represents a person.

## Parent class
None

## Attributes

* ```first_name```
  * data type: string
  * description: stores the first name of the person
* ```last_name```
  * data type: string
  * description: stores the last name of the person
* ```year_of_birth```
   * data type: int
   * description: stores the year of birth of the person
* ```gender```
  * data type: string
  * description: stores the gender of the person
* ```energy_level```
  * data type: int
  * description: stores the energy level of the person 0 - ∞
* ```skill_level```
  * data type: int
  * description: stores the skill level of the person 0 - 100

## Class methods

### ```class method name here```

description here

#### Arguments
None

#### Return value

```return value here```

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

first_name (string), last_name (string), year_of_birth (int), gender (string)
* ```first_name```
  * data_type: string
  * description: holds the first name of the person
* ```last_name```
  * data_type: string
  * description: holds the last name of the person
* ```year_of_birth```
  * data_type: integer
  * description: holds the year of birth of the person
* ```gender```
  * data_type: string
  * description: holds the gender of the person


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
