class Shape :
    def __init__(self,length) :
         pass
    def area(self) :
        return 0
        
class Square(Shape) :
    def __init__(self,length) :
            self.length = length
    
    def area(self) :
        print(self.length * self.length)
        
        
length = int(input("Enter: "))
p1 = Square(length)
p1.area()