"""
Engineering major and 
math major both extend 
student
"""

class Student:
  title="student"
  def __init__(self, dorm, name):
    pass
  def get_info(self):
    pass

class EngineeringStudent(Student):
  title="BSE"
  def build_robot(self):
    pass

class MedicalStudent(Student):
  title="Md"
  def cure_patient(self):
    pass

def tests(tester):
  jon = EngineeringStudent(12, "Jon")
  jack = MedicalStudent(21, "Jack")
  tester.set_env(locals())
  tester.ae("jon.get_info()", "BSE. Jon is in dorm 12", "engineering get info")
  tester.ae("jack.get_info()", "Md. Jack is in dorm 21", "medical get info")
  tester.ae("jon.build_robot()", "Jon built a robot", "build robot")
  tester.ae("jack.cure_patient()", "Jack cured a patient", "cure patient")