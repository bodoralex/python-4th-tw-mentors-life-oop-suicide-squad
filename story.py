from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from morningrutine import MorningRoutine
from naturaldisaster import NaturalDiasaster
from justicedepartment import JusticeDepatrment

codecool_msc = CodecoolClass.create_local()

late_students = MorningRoutine.random_things(codecool_msc.students)
JusticeDepatrment.random_punishment(late_students)
"""
JusticeDepartment(late_student)
Leraning.morning_dojo(codecool_msc)"""
NaturalDiasaster.random_disasters(codecool_msc.students)
"""
Leraning.morning_dojo(codecool_msc)
NaturalDiasaster(codecool_msc)
late_students = MorningRoutine(codecool_msc)"""
