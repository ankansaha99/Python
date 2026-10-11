import math

def calculate_area_of_triangle(a, b, c):

    s = (a + b + c) / 2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if the given sides form a valid triangle
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    area = calculate_area_of_triangle(side1, side2, side3)
    print(f"The area of the triangle is {area:.2f} square units")
else:
    print("These side lengths do not form a valid triangle.")
