
def greet(name):
    """This is Under Greet Function
    To greet the new user """

    print("Hello "+ name + ". Good Morning!!!")

greet('paul')


# return statement 

def absolute_value(num):
    """This function returns the
    absolute value of the entered number by the user."""

    if num >= 0:
        return num
    else :
        return -1

print(absolute_value(3))
print(absolute_value(-2))


# Scope of a variable 

def func():
    x = 10
    print("inside the function :", x)

x = 22
func()
print("outside the function", x )
