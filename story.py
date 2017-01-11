from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from morningrutine import MorningRoutine
from justicedepartment import JusticeDepatrment

codecool_msc = CodecoolClass.create_local()

late_students = MorningRoutine.random_things(codecool_msc.students)
JusticeDepatrment.random_punishment(late_students)
"""
Leraning.morning_dojo(codecool_msc)
NaturalDiasaster(codecool_msc)
late_students = MorningRoutine(codecool_msc)"""
