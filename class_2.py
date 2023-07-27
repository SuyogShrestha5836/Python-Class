class Fruits():
    list = "These are the list of fruits"

    def __init__(self,names,weight):
        self.name=names
        self.weight=weight
        
    def greeting(self):
        print(f'{self.list}The name of fruit is: {self.name}, weight is: {self.weight}')

fruit1_object= Fruits("Apple", 10)
fruit2_object= Fruits("Mango", 20)
fruit1_object.greeting()
fruit2_object.greeting()