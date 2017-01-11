from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from morningrutine import MorningRoutine
from naturaldisaster import NaturalDiasaster
from justicedepartment import JusticeDepatrment

codecool_msc = CodecoolClass.create_local()

late_students = MorningRoutine.random_things(codecool_msc.students)
JusticeDepartment.random_punishment(late_students)
NaturalDiasaster.random_disasters(codecool_msc.students)
"""
Learning.morning_dojo(codecool_msc)
Break.x(codecool_msc.students)
Group.x(codecool_msc.students)
late_students = MorningRoutine(codecool_msc)"""
