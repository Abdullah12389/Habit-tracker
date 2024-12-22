from datetime import datetime
import json
class User:
    def __init__(self,user_name,passwd):
        self.__name=user_name
        self.__password=passwd
        self.habits=[]
        self.points=0    
        self.authorized_status=True
    def add_habit(self,habit): #storing objects of habit class agreegation
        self.habits.append(habit)
    def  change_password(self,n_password):
        if self.authorized==True:
            self.__password=n_password
    def check_authorized(self,username,enter_password):
        if enter_password == self.__password and username==self.__name:
            self.authorized_status=True
    def save_habit(self):
        with open(f"person_data{self.__name}", "w") as f:
           json.dump(self.habits,f)
    def load_habit(self):
        with open(f"person_data{self.__name}", "r") as f:
           self.habits=json.load(f)  
class Habit:
    def __init__(self,name,frequency,description):
         self.name=name
         self.frequency=frequency
         self.description=description
         self.status=False
    def mark_done(self):
        self.status=True 





