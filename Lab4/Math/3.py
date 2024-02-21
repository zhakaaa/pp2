import math

number = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
area = (number / 4) * (length ** 2) * (1 / (math.tan(math.radians(180 / number))))

print(f"The area of the polygon is: {area}")