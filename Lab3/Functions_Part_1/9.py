# Calculate volume of sphere by radius

import math

radius = int(input("Enter radius: "))

def calculate_volume(radius) :
    pi = math.pi
    volume = (4/3) * pi * (radius ** 3)
    print("Volume is" , volume)

calculate_volume(radius)