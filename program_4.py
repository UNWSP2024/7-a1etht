#Programmer: Alethea Lo
#Date: 3/3/25
#Title: Coordinates

import math

def distance(point1, point2):
    """Calculates and returns the distance between two 3D points."""
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)

def get_coordinates(prompt):
    """Gets a 3D coordinate from the user with input validation."""
    while True:
        try:
            x, y, z = map(float, input(prompt).split())
            return (x, y, z)
        except ValueError:
            print("Invalid input. Please enter three numerical values separated by spaces.")

#Main Program
print("Enter two 3D coordinates to calculate the distance between them.")
point1 = get_coordinates("Enter first coordinate (x y z): ")
point2 = get_coordinates("Enter second coordinate (x y z): ")

dist = distance(point1, point2)
print(f"The distance between {point1} and {point2} is: {dist:.2f}")