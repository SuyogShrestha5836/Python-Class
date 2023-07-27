class Mammal:
    def __init__(self,legs,eyes,name):
        self.legs=legs
        self.eyes=eyes
        self.name=name
def print_details(self):
    print(self.legs,self.eyes)

class HumanBeing(Mammal):
    def __init__(self,brain_power,legs,eyes,name):
        self.brain_power=brain_power
        super().__init__(legs,eyes,name)
        
    def print_details(self):
        print(f'Name is: {self.name}, {self.eyes}, {self.legs}, {self.brain_power}')

oshan_object = HumanBeing("100","2","2","Oshan")
oshan_object.print_details()

class Cow(Mammal):
    def __init__(self,smell_power,legs,eyes,name):
        self.smell_power=smell_power
        super().__init__(legs,eyes,name)
        
    def print_details(self):
        print(f'Name is: {self.name}, It has {self.eyes} eyes, It has {self.legs} legs, It has {self.smell_power} percent smell power')

white_object = Cow("60","4","2","White")
white_object.print_details()