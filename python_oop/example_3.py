class Circle():
    
    pi = 3.14
    
    def __init__(self,radius=1):
        self.radius = radius
        
    def area(self):
        result = self.radius ** 2
        result = result * self.pi
        
        return result
        
    
    def perimeter(self):
        return 2 * self.radius * Circle.pi
    
    def double_radius(self):
        self.radius = self.radius * 2
        print(f"Radius has been doubled to {self.radius}")
        
    def multiply_radius(self,number):
        self.radius = self.radius * number
        print(f"Radius has been changed to {self.radius}")

    
    
mycircle = Circle(radius=4)
print(mycircle.radius)
print(mycircle.double_radius())
print(mycircle.multiply_radius(3))