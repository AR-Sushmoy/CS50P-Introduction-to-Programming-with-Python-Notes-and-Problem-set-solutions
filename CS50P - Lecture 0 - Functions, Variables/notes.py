""" Data Types """


# Strings --> str

'''
# --- String Methods ---

# Remove whitespaces from 'str'
name = name.strip()

# Capitalize the first letter from 'str'
name = name.capitalize()

# Capitalize the first character in every word in a 'str'
name = name.title()

name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, middle, last = name.split(" ")

print(f"hello, {last}")
'''

# Integers --> int

'''
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)
'''

# Float 

'''
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round((x+y), 3) # The round method rounds floating point numbers to the next integer. Or we can declare how many floating points we want to keep in a number.

So, if we input x = 34.56782 and y = 74.283462
we'll get 108.851 as the output.
'''

'''
z = round(x + y)
print(f"{z:,}")

So, if we input x = 999 and y = 1
we'll get 1,000 as the output. 
'''
'''
z = round((x / y), 2)

print(z)
So, if we input x = 2 and y = 3
we'll get 0.67 as the output.

# Another way of doing the same thing 
z = x / y
print(f"{z:.2}")
'''

# def (Function)

def display():
    print("Hello")

name = input("What's your name? ")
display()
print(name)


''' ------ USEFUL LINKS ------
Visual Studio Code for CS50P
URL: code.cs50.io
Tutorial Video: https://cs50.harvard.edu/python/2022/shorts/visual_studio_code_for_cs50/

Submission Portal for CS50P
URL: https://submit.cs50.io/courses
URL: https://submit.cs50.io/courses/1202/
URL: https://submit.cs50.io/users/AR-Sushmoy

CS50P Progress tracker 
URL: https://cs50.me/
URL: https://cs50.me/cs50p

'''