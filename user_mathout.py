"""
Always start with a docstring that describes what the module does.
Include your name and the date.
Kellie Heckman 23JAN23

Use built-in functions and 
functions from the math module.

To illustrate the ability to call functions and 
display useful results to the user. 

Use your textbook and the examples in this repo to get ideas.

"""

import math

# define some functions

def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something 
    # could go wrong
    try: 
        area = length * width
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)
get_area_of_lot(6, 2)


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Explore some functions in the math module")
    print()
    print(f"math.comb(5,1) = {math.comb(5,1)}")
    print(f"math.perm(5,1) = {math.perm(5,1)}")
    print("your code here")

def get_area_of_lot(length, width):
    try:
        area = length * width
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None
print(f"Lot area: {get_area_of_lot(6, 2)}")

def run_area(length, width):
    area = length * width
    print(f"Run area: {area}")
run_area(20,10)

#sq feet of run space required per chicken 8 sq ft
def run_area_per_chicken(area,numchicken):
    area_chicken = area * numchicken
    print(f"Your chickens need: {area_chicken} sq ft")
run_area_per_chicken(8,15)

def run_area_round(radius):
    area_round = math.pi * (radius ** 2)
    print(f"Round run area: {area_round}")
run_area_round(10)
