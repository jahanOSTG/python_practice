class employee: #ceating class
    name=""
    id=""
    number=""
    
    def value(each,name,id,number): #function1
        each.name=name
        each.id=id
        each.number=number
        
    def display(each): #function2
        print(f"name: {each.name}, id: {each.id}, number: {each.number}")


janie=employee() #creating object1
janie.value("janie",171,+92893)
janie.display()



mahabi=employee() #creating object1
mahabi.value("mahabi",271,+9181)
mahabi.display()






