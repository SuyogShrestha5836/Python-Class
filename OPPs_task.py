class Animal:
    def __init__(self,legs,eyes,name):
        self.legs=legs
        self.eyes=eyes
        self.name=name
    def make_sound(self):
        print("Hello")

class Lion(Animal):
    def __init__(self,legs,eyes,name):
        super().__init__(legs,eyes,name)
    def details(self):
        print(f'The name is {self.name}, It has {self.eyes} eyes, It has {self.legs} legs.')
    def make_sound(self):
        return "Lion Roarsss"

lion_object = Lion("4","2","Jungle")
lion_object.details()
print(lion_object.make_sound())
