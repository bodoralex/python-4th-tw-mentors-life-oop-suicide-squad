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
print(codecool_msc.avg_energy())
Learning.morning_dojo(codecool_msc.students)
Breaks.mass_lunchbreak(codecool_msc)
coder_pairs = Pair.create_pairs(codecool_msc)
Learning.pair_programming(coder_pairs)
Breaks.random_breaks(codecool_msc.students)
NaturalDiasaster.random_disasters(codecool_msc.students)

"""
NaturalDiasaster(codecool_msc)
late_students = MorningRoutine(codecool_msc)
"""
