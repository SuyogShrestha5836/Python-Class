class HumanBeing():
    greet = "Welcome to the application"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greeting(self):
        print(f'{self.greet}, Name is: {self.name}, Age is: {self.age}')
binod_object = HumanBeing("Binod", 10)
suyog_object = HumanBeing("Suyog", 12)
durga_object = HumanBeing("Durga", 14)
reya_object = HumanBeing("Reya", 16 )
bibid_object = HumanBeing("Bibid", 18)
binod_object.greeting()
suyog_object.greeting()
durga_object.greeting()
reya_object.greeting()
bibid_object.greeting()