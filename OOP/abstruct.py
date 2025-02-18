from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self,dimention1,dimention2):
        self.dimention1=dimention1
        self.dimention2=dimention2
    def area():
        pass
        
class Triangle(Shape):
    
    def area(self):
        triangle_area= 0.5* self.dimention1 *self.dimention2
        print("Area of Triangle : ",triangle_area)
        
        


class Rectengle(Shape):
  
    
    def area(self):
        rectengle_area=self.dimention1 *self.dimention2
        print("Area of Triangle : ",rectengle_area)
        



t1=Triangle(10,5)
t1.area() 

t2=Rectengle(10,5)
t2.area()
    
        