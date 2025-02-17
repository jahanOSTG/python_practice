# Parent class
class Name:
    def __init__(self):
        print("You can enter age")

    

# Child class
class Section(Name):
   def __init__(self):
       super().__init__()
       print("You can enter id")

# Creating an instance of the child class
s = Section()
