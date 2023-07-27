'''from demo_package.module_demo_one import sum,Animal
from demo_package.module_demo_three import sub
from random import randint

print(sum(10,20))
object_animal = Animal()'''

from demo_package.module_demo_one import Mammal
class Cow(Mammal):
    def __init__(self,smell_power,legs,eyes,name):
        self.smell_power=smell_power
        super().__init__(legs,eyes,name)
        
    def print_details(self):
        print(f'Name is: {self.name}, It has {self.eyes} eyes, It has {self.legs} legs, It has {self.smell_power} percent smell power')

white_object = Cow("60","4","2","White")
white_object.print_details()
