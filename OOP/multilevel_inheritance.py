#multilevel inheritance
class A:
    def display1(self):
        print("Class A")

class B(A):
    def display2(self):
        print("Class B")
        
class C(B):
    
    def display3(self):
        super().display1()
        super().display2()
        print("Class c")
        
d3= C()
d3.display3()