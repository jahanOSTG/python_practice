#parent class
class name:
    def age(self):
        print("You can enter age")
    def id(self):
        print("you can enter id")

#child class
class section(name):
    def dept(self):
        print("you can enter department")
        
        
        
n=section()
n.age()
n.id()
n.dept()
print(issubclass(section,name))