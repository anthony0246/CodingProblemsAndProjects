
from math import *

#take in all necessary information in order to calculate the defined integral (the function itself, the location of the bornes and the number of sub intervals desired by the user)
function_to_integrate = input('Please input the function you want to integrate, please make sure to watch you bracket placement and use "**" instead of "^": ' )
top_borne = int(input(f'Please input the top borne of the defined integral, in other words "x2": '))
bottom_borne = int(input(f'Please input the bottom borne of the defined integral, in other words "x1": '))

number_of_sub_intervals = int(input(f"Please input the number of sub intervals for the defined integral. Note: This value must be an even integer for Simpson's method and the Trapezium method: "))

def apply_simpsons_method(function_to_integrate, top_borne, bottom_borne, number_of_sub_intervals): #applying Simpson's method to calculate the defined integral
    difference_between_bornes = top_borne - bottom_borne
    size_of_sub_intervals = difference_between_bornes / number_of_sub_intervals
    accumulative_sum = 0
    current_interval = bottom_borne
    is_even_interval = True

    for i in range(number_of_sub_intervals + 1):
        temporary_function = function_to_integrate.replace("x", str(current_interval))
        temporary_function = float(f"{eval(temporary_function)}")
        
        if i == 0 or i == number_of_sub_intervals:
            accumulative_sum += temporary_function
            current_interval += size_of_sub_intervals
        elif is_even_interval:
            accumulative_sum += 4*(temporary_function)
            current_interval += size_of_sub_intervals
            is_even_interval = False
        elif not is_even_interval:
            accumulative_sum += 2*(temporary_function)
            current_interval += size_of_sub_intervals
            is_even_interval = True

    return ((size_of_sub_intervals) / 3) * accumulative_sum

if number_of_sub_intervals % 2 == 0: 
    print("\nSimpson's method: ")
    print(apply_simpsons_method(function_to_integrate, top_borne, bottom_borne, number_of_sub_intervals), "\n")


def apply_trapezium_method(function_to_integrate, top_borne, bottom_borne, number_of_sub_intervals): #applying the Trapezium method to calculate the defined integral
    difference_between_bornes = top_borne - bottom_borne
    size_of_sub_intervals = difference_between_bornes / number_of_sub_intervals
    accumulative_sum = 0
    current_interval = bottom_borne
    
    for i in range(number_of_sub_intervals + 1):
        temporary_function = function_to_integrate.replace("x", str(current_interval))
        temporary_function = float(f"{eval(temporary_function)}")
        
        if i == 0 or i == number_of_sub_intervals:
            accumulative_sum += temporary_function
            current_interval += size_of_sub_intervals
        else:
            accumulative_sum += 2*(temporary_function)
            current_interval += size_of_sub_intervals

    return ((size_of_sub_intervals) / 2) * accumulative_sum

if number_of_sub_intervals % 2 == 0:
    print("Trapezium method: ")
    print(apply_trapezium_method(function_to_integrate, top_borne, bottom_borne, number_of_sub_intervals), "\n") 


def apply_mid_point_rule(function_to_integrate, top_borne, bottom_borne, number_of_sub_intervals): #applying the Middle Points method to calculate the defined integral
    difference_between_bornes = top_borne - bottom_borne
    size_of_sub_intervals = difference_between_bornes / number_of_sub_intervals
    accumulative_sum = 0
    current_interval = bottom_borne + (size_of_sub_intervals) / 2

    for i in range(number_of_sub_intervals):
        temporary_function = function_to_integrate.replace("x", str(current_interval))
        temporary_function = float(f"{eval(temporary_function)}")

        accumulative_sum += temporary_function
        current_interval += size_of_sub_intervals

    return size_of_sub_intervals * (accumulative_sum)

if number_of_sub_intervals % 2 != 0:
    print("\nMiddle points method: ")
else:
    print("Middle points method: ")
print(apply_mid_point_rule(function_to_integrate, top_borne, bottom_borne, number_of_sub_intervals), "\n")

