from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from morningrutine import MorningRoutine
from justicedepartment import JusticeDepatrment
from groups import *

codecool_msc = CodecoolClass.create_local()


late_students = MorningRoutine.random_things(codecool_msc.students)
JusticeDepatrment.random_punishment(late_students)
print(codecool_msc.students)
coder_pairs = Pair.create_pairs(codecool_msc)
print(coder_pairs[0].members)
print(coder_pairs[1].members)
"""
Learn.pairprograming(coder_pairs)
Leraning.morning_dojo(codecool_msc)
NaturalDiasaster(codecool_msc)
late_students = MorningRoutine(codecool_msc)
"""
