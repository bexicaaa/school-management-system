class School:
  #To define a School object I gave it a name, type of school(elementary school, highschool or college), and a boolean to determie if it has successful students. At the beggining it set to False because we want to imagine we are just at the beginning of the year.

    def __init__(self, name, type, students):
      self.name = name 
      self.type = type
      self.students = students
      self.has_name = 
      # self.has_successful_students = False
      # self.has_extracurricular_activities = True
      # self.gives_scholarship = True 
      
      
#Printing a school gives us name, type of school and number of enrolled students
    def __repr__(self):
        return "This {type} school {name} has {students} of students".format(type = self.type, name = self.name, students = self.students)

#Prompt the user to give us an average GPA of all students in the school
# print("Enter average GPA of all students in school")
# average_gpa = int(input())

    def success(self, average_gpa):
      self.has_successful_students = False
      if average_gpa > 3.5:
        self.has_successful_students == True
        print("{name} school has successful students!".format(self = self.name))

class Teacher:
  def __init__(self, name, subject, enrolled_students = 60):
    self.name = name
    self.subject = subject
    self.enrolled_students = 60
    self.is_mentor = False
    self.is_funny = False
    self.is_successful = False

#Prints the teacher's name, what subject are they teaching and how many students they have in total.
  def __repr__(self):
    return "Teacher {name} is teaching his {enrolled_students} students {subject}".format(name = self.name, enrolled_students = self.enrolled_students, subject = self.subject)



#Prints out a studets name and age, their gpa and also a year they are currently in.
class Student:
  def __init__(self, name, age, gpa, year):
    self.name = name
    self.gpa = gpa
    self.year = year
    self.has_scholarship = False
    self.has_honors = False
    self.has_favorite_subject = True


#Testing Student class:
first_school = School("OŠ SSK", "Elementary", 500)
second_school = School("Klasična", "Gimnazija", 800)
third_school = School("Glazbena škola", "Instrumenti", 700)
