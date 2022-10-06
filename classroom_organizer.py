#this python file contains the class for the program learing about iterables
#a classroom organization has group of students from a roster file, has the POWERFUL iterator protocol customer class methods, two methods {1: sort student by alpha names | 2: get students for subject}
# this code is the driving logic behind main.py and is dependent on the roster data of roster.py


from roster import student_roster
import itertools
# Import modules above this line
class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)
    self.count = 0
  
  def __iter__(self):
     return self

  def __next__(self):
    if self.count >= 10:
      raise StopIteration
    else:
      self.count += 1
      return self.sorted_names[self.count - 1]


  def _sort_alphabetically(self,students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)

  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students

  def class_seats(self):
    return itertools.combinations(self.sorted_names, 2)