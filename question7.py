# First, def a function called distance_from_zero, with one argument (choose any argument name you like). If the type of the argument is either int or float, the 
#function should return the absolute value of the function input. Otherwise, the function should return "Nope". Check if it works calling the function with -5.6 and 
#"what?".


def distance_from_zero(a):
    if type(a)==int or type(a)==float:
        return abs(a)
    else:
        return "Nope"
a=eval(input("Enter the no"))
print(distance_from_zero(a))