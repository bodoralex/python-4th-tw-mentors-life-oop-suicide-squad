from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from morningrutine import MorningRoutine
from naturaldisaster import NaturalDiasaster
from justicedepartment import JusticeDepartment
from breaks import Breaks
from groups import *

codecool_msc = CodecoolClass.create_local()

late_students = MorningRoutine.random_things(codecool_msc.students)
JusticeDepatrment.random_punishment(late_students)
coder_pairs = Pair.create_pairs(codecool_msc)
print(coder_pairs[0].members)
print(coder_pairs[1].members)
NaturalDiasaster.random_disasters(codecool_msc.students)
Breaks.random_breaks(codecool_msc.students)
"""
Learn.pairprograming(coder_pairs)
Leraning.morning_dojo(codecool_msc)
NaturalDiasaster(codecool_msc)
late_students = MorningRoutine(codecool_msc)
"""
