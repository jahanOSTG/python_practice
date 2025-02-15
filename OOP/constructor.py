class Employee:  # Creating class
    def __init__(self, name, id, number):  # Correct constructor
        self.name = name
        self.id = id
        self.number = number

    def display(self):  # Function1
        print(f"Name: {self.name}, ID: {self.id}, Number: {self.number}")

# Creating object1
janie = Employee("Janie", 171, 92893)  
janie.display()

# Creating object2
mahabi = Employee("Mahabi", 271, 9181)  
mahabi.display()
