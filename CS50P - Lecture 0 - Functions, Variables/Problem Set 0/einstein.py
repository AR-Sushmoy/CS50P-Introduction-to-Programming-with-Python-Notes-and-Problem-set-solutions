"""
Question: implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
"""

speed_of_light = 300000000
mass = int(input("m: "))

energy = mass * pow(speed_of_light, 2)

print("E:", energy)
