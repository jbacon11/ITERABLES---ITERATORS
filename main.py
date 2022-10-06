"""
Python code learning about iterators and iterables
Pythons is dope
so stronkg
much stonks

i will update to actually make sense
two other python files are included
roster.py has the data dictionary for students in a class

"""

#import student_roster from roster
from roster import student_roster
from classroom_organizer import ClassroomOrganizer
import itertools

roster = iter(student_roster)
#print(next(roster))
#print(next(roster))
#print(next(roster))
#print(next(roster))
#print(next(roster))
#print(next(roster))
#print(next(roster))
#print(next(roster))
#print(next(roster))
#print(next(roster))

class_room = ClassroomOrganizer()

for class_stu in class_room:
  print(class_stu)
print("\n###############################\n")
class_seatings = class_room.class_seats()
for seat in class_seatings:
  print(seat)
print("\n###############################\n")
math_stu = class_room.get_students_with_subject("Math")
sci_stu = class_room.get_students_with_subject("Science")

comb_stu = itertools.chain(math_stu, sci_stu)
print(comb_stu)
list_stu = []
for comb in comb_stu:
  print(comb)
  list_stu.append(comb)

print(list_stu)

comb_comb_stu = itertools.combinations(list_stu, 4)
print(comb_comb_stu)
for i in comb_comb_stu:
  print(i)