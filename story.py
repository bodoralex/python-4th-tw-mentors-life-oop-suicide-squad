from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from morningrutine import MorningRoutine
from naturaldisaster import NaturalDiasaster
from justicedepartment import JusticeDepartment
from breaks import Breaks

codecool_msc = CodecoolClass.create_local()

late_students = MorningRoutine.random_things(codecool_msc.students)
JusticeDepartment.random_punishment(late_students)

"""
JusticeDepartment(late_student)
Leraning.morning_dojo(codecool_msc)"""

NaturalDiasaster.random_disasters(codecool_msc.students)
Breaks.random_breaks(codecool_msc.students)
"""
Learning.morning_dojo(codecool_msc)
Break.x(codecool_msc.students)
Group.x(codecool_msc.students)
late_students = MorningRoutine(codecool_msc)"""
