'''
Comparision Operators:
>
>=
<
<=
==
!=

'''

# score = int(input("Score: "))
'''
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")
'''
'''
if 90 <= score <= 100: # Same as, if 90 <= score and score <= 100
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")
'''
''' 
# This Program will produce bugs later on, It is better to include the upper limit as well.
if score >= 90: 
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
'''
#--------------------------------------------------------
'''
Arithmatic Symbols:
+
-
*
/
% ---> Modulo operator

'''

def main():
    x = int(input("What's x? "))

    if is_even(x):
        print("Even")
    else: 
        print("Odd")

def is_even(n):
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

    ### This is another way of doing the same thing in python
    # return True if n % 2 == 0 else False

    ### or you can do this too (The tightest way)
    return n % 2 == 0

main()  

#--------------------------------------------------------
name = input("What's your name? ")

'''
if name == "Harry" or name == "Hermoine" == name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
'''


''' ---- Match ----
match is somthing similar to switch case in Javascript or other programming languages but here in python you don't need to use the keyword break and instead of default you'll have to use underscore symbol -> case _:
'''
match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
