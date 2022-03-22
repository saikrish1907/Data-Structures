'''
Inheritance concept in Python
'''
class university:

    def __init__(self,uname):
        self.uname = uname
    
    def display(self):
        print(self.uname)
          
    def details(self):
        print("My University name is {}".format(self.uname))

class student(university): #Keyword inheritance is necessary in paranthesis

    def __init__(self, uname, idnumber, sname ):
        self.idnumber = idnumber
        self.sname = sname
  
        # invoking the __init__ of the parent class
        university.__init__(self, uname)
          
    def details(self):
        print("My name is {}".format(self.sname))
        print("IdNumber: {}".format(self.idnumber))
        print("University: {}".format(self.uname))

st = student("sastra",1,"Sai") 
st.display() #calls the parents class university 
st.details() #calls the child class student



'''
Polymorphism concept 
'''
#Taken from geeksforgeeks for reference and learning.
class Bird:
    
    def intro(self):
        print("There are many types of birds.")
  
    def flight(self):
        print("Most of the birds can fly but some cannot.")
  
class sparrow(Bird):
    
    def flight(self):
        print("Sparrows can fly.")
  
class ostrich(Bird):
  
    def flight(self):
        print("Ostriches cannot fly.")
  
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
  
obj_bird.intro()
obj_bird.flight()
  
obj_spr.intro()
obj_spr.flight()
  
obj_ost.intro()
obj_ost.flight()

  
        