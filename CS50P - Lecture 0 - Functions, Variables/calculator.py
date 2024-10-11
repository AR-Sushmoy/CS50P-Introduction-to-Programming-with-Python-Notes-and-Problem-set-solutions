'''
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round((x+y), 3) # The round method rounds floating point numbers to the next integer. Or we can declare how many floating points we want to keep in that number.
# This is what the round function looks like in the documentations --> round(number[, ndigits])

# Explanation: Generally, when there is a square bracket in documentation like this shown above, This means that you're about to see something optional. And so what this means is that, if you want to specify more precisely the number of digits that you want the round function to round to, you can specify it here by adding a comma and then that number. suppose you want around to the tenths place, or the hundredths place that is one or two digits after the decimal point, you could additionally pass in comma 1 or comma 2 to be more precise. So that's what the documentation, there is saying. For Example: round(x, 2)

So, if we input x = 34.56782 and y = 74.283462
we'll get 108.851 as the output.
'''

'''
# Another feature of the f-string:

x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x + y)
print(f"{z:,}")

# So, if we input x = 1000000000000 and y = 20000000000000
# we'll get 21,000,000,000,000 as the output. It will separate every 100th place with comma for us automatically.
'''

'''
# Another interesting feature of the f-string: (Instead of using the round function)

x = float(input("What's x? "))
y = float(input("What's y? "))
z = round((x / y), 2)

print(z)
# So, if we input x = 5 and y = 7, we'll get 0.71 as the output.

# Another way of doing the same thing 
z = x / y
print(f"{z:.2}")
# So, if we input x = 5 and y = 7, we'll get the same 0.71 as output.
'''

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return pow(n, 2) # this means n ** 2

main()