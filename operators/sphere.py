# Write a Python program to calculate the surface volume and area of a sphere.

import math
radius = float(input("Enter the radius of the sphere: "))

surfaceVolume = 4/3 * math.pi * radius**3
surfaceArea = 4 * math.pi * radius**2

print("Surface volume is ",surfaceVolume,"cubic units")
print("Surface Area is: ",surfaceArea,"square units")


