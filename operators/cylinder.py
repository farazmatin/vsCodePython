# A cylinder's volume is π r² h, and its surface area is 2π r h + 2π r².
import math
radius = float(input("Enter the value of radius: "))
height = float(input("Enter the value of height: "))

surfaceVolume = math.pi * radius**2 * height
surfaceArea = (2 * math.pi * radius * height) + (2*math.pi*radius**2)
print("Surface Volume is: ",surfaceVolume,"cubic units")
print("Surface Area is: ",surfaceArea,"Square units")
