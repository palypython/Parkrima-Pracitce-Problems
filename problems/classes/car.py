"""
Create a class called 'Car' that
represents a car. 
"""

class Car:
  def __init__(self,tank_capacity):
    pass
  # return the amount of petrol
  # currently in the tank
  def get_current_petrol(self):
    pass
  # drive the car a certain distrnace
  # and use up some petrol while
  # driving
  def drive(self,kilometers):
    pass
  # refill the petrol tank to full
  def refill_tank(self):
    pass

# this functions tests if your program 
# is actually correct, do not touch it.
def tests(tester):
  c = Car(10)
  tester.set_env(locals())
  c.drive(2)
  tester.ae("c.get_current_petrol()", 8, "driving reduces gas")
  c.refill_tank();
  tester.ae("c.get_current_petrol()", 10, "refilling resets the tank")