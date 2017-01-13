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



## Instance methods

### ```__init__```
The constructor of the object.
If first_name or last_name is not a string, raises Codecool Error 
If last_name is not an int, raises Codecool Error
If gender is not a string or not not male, female or notsure raises Codecool Error


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


### ```it```

Gives back the person's noun.

#### Arguments

None

#### Return value

"he", "she", "it" depending on the person's gender.


### ```its```

Gives back the person's posessive pronuon.

#### Arguments

None

#### Return value

"his", "her", "its" depending on the person's gender.



### ```fullname(getter)```

#### Arguments

None

#### Return value
A string which contains the person's first_name and last_name.