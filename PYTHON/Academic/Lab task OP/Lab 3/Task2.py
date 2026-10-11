import math

def calculate_area(radius):
    area = math.pi * (radius ** 2)
    return area

def calculate_perimeter(radius):
    perimeter = 2 * math.pi * radius
    return perimeter
radius = float(input("Enter the radius of the circle: "))

if radius >= 0:
    area = calculate_area(radius)
    perimeter = calculate_perimeter(radius)
    print(f"The area of the circle is {area:.2f} square units")
    print(f"The perimeter (circumference) of the circle is {perimeter:.2f} units")
else:
    print("Invalid radius. Please enter a non-negative value for the radius.")
