import math

class Point :
    def __init__ (self,x,y) :
        self.x = x
        self.y = y
        
    def show_coordinates(self) :
        print(f"The coordinates of point ({self.x};{self.y})")
        
    def add_new_point(self) :
        print("Enter coordinates of new point: ")
        self.x2 = int(input())
        self.y2 = int(input())

    def calculate_distance(self) :
        distance = math.sqrt( (pow(self.x2 - self.x,2) + (pow(self.y2 - self.y,2) ) ) ) 
        print(f"The distance between ({self.x};{self.y}) and ({self.x2};{self.y2}) is: {distance}")
        

x = int(input())
y = int(input())

point_A = Point(x,y)

point_A.show_coordinates()

point_A.add_new_point()

point_A.calculate_distance()