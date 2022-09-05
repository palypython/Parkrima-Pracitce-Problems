"""
fill in the code below to create
a dog simulator. Every time 
a dog is pet, the happiness of
the dog increases by its friendliness
factor, which is dependent on
the species of the dog
"""


class Dog:
    # initially, a dog has 0 happiness
    def __init__(self, friendliness=1):
      self.happiness=-1  
      pass
    # when a dog is pet, it becomes
    # happier
    def pet(self):
        pass
    # the face of a dog is
    # 🙁 if the happiness is <= 3
    # 😬 if the happiness is >3 and <4
    # 😊 if the happiness is >= 4
    def get_face(self):
      pass

# a poodle is a kind of dog, so
# poodles extend the dog class
class Poodle(Dog):
    # poodles have a friendliness of 0.1
  
    def __init__(self, name):
        super().__init__()

# a bulldog is a kind of dog, so
# bulldogs extend the dog class
class Bulldog(Dog):
    # bulldogs have a friendliness of 2
  
    def __init__(self, name):
        super().__init__()

      
def tests(tester):
  sam = Poodle("Sam")
  rick = Bulldog("Rick")
  tester.set_env(locals())
  tester.ae("sam.happiness", 0, "Sam happiness")
  tester.ae("rick.happiness", 0, "Rick happiness")
  tester.ae("sam.get_face()","🙁", "sam's face")
  tester.ae("rick.get_face()", "🙁", "rick's face")
  sam.pet()
  tester.ae("sam.happiness", 0.1, "Sam hapiness after 1 pet")
  sam.pet()
  tester.ae("sam.happiness", 0.2, "Sam hapiness after 2 pets")
  rick.pet()
  tester.ae("rick.happiness", 2, "Rick hapiness after 1 pet")
  rick.pet()
  tester.ae("rick.happiness", 4, "Rick hapiness after 2 pets")
