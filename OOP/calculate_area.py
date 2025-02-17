class Shape:
    def __init__(self,dimention1,dimention2):
        self.dimention1=dimention1
        self.dimention2=dimention2
    def area():
        print("area")
        
class Triangle(Shape):
    
    def area(self):
        triangle_area= 0.5* self.dimention1 *self.dimention2
        print("Area of Triangle : ",triangle_area)
        
        
t1=Triangle(20,10)
t1.area()

class Rectengle(Shape):
  
    
    def area(self):
        rectengle_area=self.dimention1 *self.dimention2
        print("Area of Triangle : ",rectengle_area)
 
t2=Rectengle(7,5)
t2.area()
    
        