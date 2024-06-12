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

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return pow(n, 2) # this means n ** 2

main()