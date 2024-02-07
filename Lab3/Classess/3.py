class Shape :
    def __init__(self,length,width) :
         pass
    
    def area(self):
        return 0
        
class Rectangle(Shape) :
    def __init__(self,length,width) :
            self.length = length
            self.width = width
    
    def area(self) :
        print(self.length * self.width)
        
        
length = int(input("Enter: "))
width = int(input("Enter: "))

p1 = Rectangle(length,width)
p1.area()