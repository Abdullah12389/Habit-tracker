class Person:
    def __init__(self,name,password):
        self.__name=name
        self.__password=password
        self.habits=[] 
        self.points=0    
    def add_habit(self,habit): #storing objects of habit class agreegation
        self.habits.append(habit)
class Habit(Person):
    def __init__(self,name,frequency,description):
         self.name=name
         self.frequency=frequency
         self.description=description
         self.status=False
    def mark_done(self):
        self.status=True
    def refresh_habit(self):
        self.status=True       




