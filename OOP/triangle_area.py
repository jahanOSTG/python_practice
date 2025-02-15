class triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height
        
    def calculate(self):
        area= 0.5* self.base* self.height
        print(f"triangle area: {area}")
        
t1=triangle(10,20)
t1.calculate()

t2=triangle(30,20)
t2.calculate()