from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from morningrutine import MorningRoutine
from naturaldisaster import NaturalDiasaster
from justicedepartment import JusticeDepartment
from breaks import Breaks
from groups import *
from learning import Learning

codecool_msc = CodecoolClass.create_local()

late_students = MorningRoutine.random_things(codecool_msc.students)
JusticeDepartment.random_punishment(late_students)
Learning.morning_dojo(codecool_msc.students)
coder_pairs = Pair.create_pairs(codecool_msc)
Learning.pair_programming(coder_pairs)
NaturalDiasaster.random_disasters(codecool_msc.students)
"""
Breaks.random_breaks(codecool_msc.students)
Leraning.morning_dojo(codecool_msc)
NaturalDiasaster(codecool_msc)
late_students = MorningRoutine(codecool_msc)
"""
