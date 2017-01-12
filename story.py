from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from morningrutine import MorningRoutine
from naturaldisaster import NaturalDiasaster
from justicedepartment import JusticeDepartment
from breaks import Breaks
from groups import *
from learning import Learning


def main():

    codecool_msc = CodecoolClass.create_local()
    late_students = MorningRoutine.random_things(codecool_msc.students)
    JusticeDepartment.random_punishment(late_students)
    print(codecool_msc.avg_energy())
    print(codecool_msc.avg_knowledge())
    Learning.morning_dojo(codecool_msc.students)
    coder_pairs = Pair.create_pairs(codecool_msc)
    Learning.pair_programming(coder_pairs)
    print(codecool_msc.avg_knowledge())
    Breaks.mass_lunchbreak(codecool_msc)
    print(codecool_msc.avg_energy())
    NaturalDiasaster.random_disasters(codecool_msc.students)
    Breaks.random_breaks(codecool_msc.students)

if __name__ == "__main__":
    main()
