#This program calculates the derivative of common functions and can apply the chain rule. 
import math

dict_with_base_functions = {
    'cos(x)': "-sin(x)",
    'sin(x)': "cos(x)",
    'tan(x)': "(sec(x))^(2)",
    'ln(x)': "(1/x)",
    'e^(x)': "e^(x)"
}

possible_operations = ["+", "-", "*", "/"]

list_for_check_poly = ["(", ")"]

list_for_cancel_poly = ["^"]

list_of_pre = ["cos", "sin", "ln", "tan", "e^"]

def derivative(function_to_derive):
    #check which derivative rule to apply (product or quotient), if necessary
        #do the derivative 
    if (function_to_derive == "" or function_to_derive == None):
        return ""

    function_to_derive = function_to_derive.replace(" ", "")

    first_operation = find_least_indented_operator(function_to_derive)

    if (type(first_operation) == list and first_operation[0] != ''):
        fx = remove_extra_brackets(function_to_derive[ : first_operation[1]])
        gx = remove_extra_brackets(function_to_derive[first_operation[1] + 1 :])

        if first_operation[0] == "*":
            return apply_product_rule(fx, gx)
        elif first_operation[0] == "/":
            return apply_quotient_rule(fx, gx)
        elif first_operation[0] == "+":
            return f"{derivative(fx)}+{derivative(gx)}"
        elif first_operation[0] == "-":
            return f"{derivative(fx)}-{derivative(gx)}"
        else:
            raise Exception("The operations don't match. Don't know how that's possible")

    else:
        '''
        outside_function = IdentifyOutsideFunction()
        apply chain rule
            We need to take the derivative of the outside function and apply the chain rule if necessary
        '''
        outside_function = IdentifyOutsideFunction(function_to_derive)

        if outside_function in list_of_pre:
            if outside_function == "cos":
                return f"-sin({function_to_derive[4: ]}*({derivative(function_to_derive[4 : -1])})"
            elif outside_function == "sin":
                return f"cos({function_to_derive[4: ]}*({derivative(function_to_derive[4 : -1])})"
            elif outside_function == "tan":
                return f"sec^(2)({function_to_derive[4: ]}*({derivative(function_to_derive[4 : -1])})"
            elif outside_function == "ln":
                return f"(1/({function_to_derive[3: ]})*({derivative(function_to_derive[3 : -1])})"
            elif outside_function == "e^":
                return f"(e^{function_to_derive[3: ]}*({derivative(function_to_derive[3 : -1])})"
            else:
                return 0
        else:
            if "x" in function_to_derive:
                return derive_power_function(function_to_derive)
            else:
                return 0
    
def apply_product_rule(fx, gx): 
    #applies the product rule, by taking two functions as an input
    return f"({derivative(fx)}*{gx}) + ({fx}*{derivative(gx)})"

def apply_quotient_rule(fx, gx):
    #applies the quotient rule, by taking two functions as an input
    return f"(({derivative(fx)}*{gx}) - ({fx}*{derivative(gx)}))/{gx}^2"

def apply_chain_rule(fx):
    #applies the chain rule to function after they are derived, in order to account for nested functions
    index_of_open_bracket = 0
    index_of_closed_bracket = 0
    bracket_found = False
    first_one = True
    for i in range(len(fx)):
        if fx[i] == "(" and first_one:
            bracket_found = True
            first_one = False
            index_of_open_bracket = i
        elif fx[i] == ")":
            index_of_closed_bracket = i
    inner_function = fx[index_of_open_bracket + 1 : index_of_closed_bracket]

    if bracket_found == True:
        return f"{fx}*{derivative(inner_function)}"
    else:
        return f"{fx}"

def IdentifyOutsideFunction(fx) -> str:
    for i in range(len(fx) - 3):
        if fx[i : i + 3] in list_of_pre:
            return fx[i : i + 3]
        elif fx[i : i + 2] in list_of_pre:
            return fx[i : i + 2]
    return ''


def derive_power_function(fx) -> str:
    index_of_base = 0
    for i in range(len(fx)):
        if fx[i] == "x":
            index_of_base = i
            break
    if fx[index_of_base + 1 : index_of_base + 3] == ")^":
        starting_nest = 1
        for i in range(len(fx[index_of_base + 1: ]), len(fx)):
            if fx[i] == "(":
                starting_nest += 1
            elif fx[i] == ")":
                starting_nest -= 1

            if starting_nest == 0:
                coeff = fx[index_of_base + 4 : i]
                try:
                    exp = str(int(coeff) - 1)
                except Exception:
                    exp = f"({coeff} - 1)"
                finally:
                    if "x" in coeff:
                        return f"({coeff})*(x)^({derivative(exp)})"
                    else:
                        return f"({coeff})*(x)^({exp})"
        return "1"
    else:
        return "1"

            
def find_function(fx):
    #determines what inner function of fx to derive first and returns the derivative, while applying the chain rule

    list_with_base_functions = []

    if "cos" in fx:
        list_with_base_functions.append('cos(x)') 
    if "sin" in fx:
        list_with_base_functions.append('sin(x)') 
    if "tan" in fx:
        list_with_base_functions.append('tan(x)')
    if "ln" in fx:
        list_with_base_functions.append('ln(x)')
    if "e^" in fx:
        list_with_base_functions.append('e^(x)')

    if len(list_with_base_functions) == 0:
        return 0
    
    minimum_index = len(list_with_base_functions)
    function_to_keep = ''

    for i in range(len(list_with_base_functions)):
        location_function_to_find = fx.index(list_with_base_functions[i][0])
        if location_function_to_find < minimum_index or minimum_index == 1:
            function_to_keep = list_with_base_functions[i]

    fx = list(fx)
    fx.pop(0)
    fx.pop(-1)
    
    fx = "".join(fx)
    
    first_index_chain = fx.find('(') + 1
    last_index_chain = fx.rfind(')') + 2
    
    fx = f"({fx})"

    if function_to_keep == "cos(x)":
        return f"-sin{fx[first_index_chain : last_index_chain]}*{derivative(fx[first_index_chain : last_index_chain])}"
    
    elif function_to_keep == "sin(x)":
        return f"cos{fx[first_index_chain : last_index_chain]}*{derivative(fx[first_index_chain : last_index_chain])}"
    
    elif function_to_keep == "tan(x)":
        return f"sec^2{fx[first_index_chain : last_index_chain]}*{derivative(fx[first_index_chain : last_index_chain])}"
    
    elif function_to_keep == "ln(x)":
        return f"1/{fx[first_index_chain : last_index_chain]}*{derivative(fx[first_index_chain : last_index_chain])}"
    
    elif function_to_keep == "e^(x)":
        return f"e^{fx[first_index_chain : last_index_chain]} * ({derivative(fx[first_index_chain : last_index_chain])})"    

def do_apply_product(fx):
    #determines if the product rule needs to be applied to the current function. Returns the index of the multiplication symbol if True and False if not.
    list_with_index = []
    for i in range(len(fx)):
        if fx[i] in possible_operations:
            list_with_index.append(i)
    
    bracket_level_for_index = []
    for j in range(len(list_with_index)):
        beginning = False
        bracket_count = 0
        iteration_count = list_with_index[j]
        num_of_times = 1
        while not beginning:
            if fx[iteration_count - num_of_times] == "(":
                bracket_count += 1
            elif fx[iteration_count - num_of_times] == ")":
                bracket_count -= 1
            
            if (iteration_count - num_of_times) == 0:
                bracket_level_for_index.append(bracket_count)
                beginning = True
                
            num_of_times += 1
            
    min_index = 0
    if len(bracket_level_for_index) >= 1:        
        min = bracket_level_for_index[0]
    else:
        return False
    for k in range(len(bracket_level_for_index)):
        if bracket_level_for_index[k] < min:
            min_index = k
            
    if fx[list_with_index[min_index]] == "*":
        return list_with_index[min_index]
    else:
        return False
                  
def do_apply_quotient(fx):
    #determines if the quotient rule needs to be applied to the current function. Returns the index of the division symbol if True and False if not.
    list_with_index = []
    for i in range(len(fx)):
        if fx[i] in possible_operations:
            list_with_index.append(i)
    
    bracket_level_for_index = []
    for j in range(len(list_with_index)):
        beginning = False
        bracket_count = 0
        iteration_count = list_with_index[j]
        num_of_times = 1
        while not beginning:
            if fx[iteration_count - num_of_times] == "(":
                bracket_count += 1
            elif fx[iteration_count - num_of_times] == ")":
                bracket_count -= 1
            
            if (iteration_count - num_of_times) == 0:
                bracket_level_for_index.append(bracket_count)
                beginning = True
                
            num_of_times += 1
            
    max_index = 0
    if len(bracket_level_for_index) >= 1:
        max = bracket_level_for_index[0]
    else:
        return False
    for k in range(len(bracket_level_for_index)):
        if bracket_level_for_index[k] > max:
            max_index = k
            
    if fx[list_with_index[max_index]] == "/":
        return list_with_index[max_index]
    else:
        return False

def do_addition_or_substraction(fx):
    #checks if there is a "+" or "-" symbol in the function in order to apply the sum or difference rule
    for i in range(len(fx)):
        if fx[i] == "+" or fx[i] == "-":
            return True
    return False

def check_if_polynomial(fx):
    #checks if fx is a polynomial function like x^(3) or 2x or -3x^(4)
    if "^" in fx:
        return fx
    index_of_x = 0
    for i in range(len(fx)):
        if fx[i] == "x":
            index_of_x = i
            break
    
    if len(fx[: index_of_x]) <= 2:
        fx = list(fx)
        fx.pop(-1)
        fx = "".join(fx)
        fx += "^(1))"
        return fx
    
    if fx[index_of_x + 1] == ")":
        for i in range(len(list_of_pre)):
            if list_of_pre[i] in fx[: index_of_x]:
                return False
        fx = list(fx)
        fx.pop(-1)
        fx = "".join(fx)
        fx += "^(1))"
        return fx

def check_if_base_other_than_polynomial(fx):
    #checks if fx is part of the base functions in the dict_with_base_functions dictionnary
    for i in range(len(list_of_pre)):
            if list_of_pre[i] in fx:
                return True
    return False

def addition_or_substraction_derivative(fx):
    #applies the sum or difference rule to fx
    list_with_index = []
    for i in range(len(fx)):
        if fx[i] == "+" or fx[i] == "-":
            list_with_index.append(i)
    
    bracket_level_for_index = []
    for j in range(len(list_with_index)):
        beginning = False
        bracket_count = 0
        iteration_count = list_with_index[j]
        num_of_times = 1
        while not beginning:
            if fx[iteration_count - num_of_times] == "(":
                bracket_count += 1
            elif fx[iteration_count - num_of_times] == ")":
                bracket_count -= 1
            
            if (iteration_count - num_of_times) == 0:
                bracket_level_for_index.append(bracket_count)
                beginning = True
                
            num_of_times += 1
            
    min_index = 0
    min = bracket_level_for_index[0]
    for k in range(len(bracket_level_for_index)):
        if bracket_level_for_index[k] < min:
            min_index = k

    index_of_symbol = list_with_index[min_index]      
    return f"{derivative(fx[: index_of_symbol])} {fx[index_of_symbol]} {derivative(fx[index_of_symbol + 1 :])}"
    
def check_for_valid_brackets(fx):
    count_of_open_brackets = 0
    for i in fx:
        if i == "(":
            count_of_open_brackets += 1
        elif i == ")":
            count_of_open_brackets -= 1

        if count_of_open_brackets == -1:
            raise Exception("Too many closed brackets!")
        
    if count_of_open_brackets != 0:
        raise Exception("Too many opening brackets!")
    else:
        return True

def remove_extra_brackets(fx):
    try: 
        check_for_valid_brackets(fx)
    except Exception:
        bracket_count = 0
        for i in fx:
            if i == "(":
                bracket_count += 1
            elif i == ")":
                bracket_count -= 1
        if bracket_count > 0:
            return fx[1: ]
        else:
            return fx[ :-1]
    return fx
        
def get_function():
    function_to_derive = input("Please input your function here: ")

    if (len(function_to_derive) == 0):
        return get_function()
    if (function_to_derive[0] != "(" or function_to_derive[-1] != ")" or not check_for_valid_brackets(function_to_derive)):
        return get_function()
    else:
        return function_to_derive

def find_least_indented_operator(fx) -> list or sentinel (-1):
    indexes_of_operators = []
    for i in range(len(fx)):
        if fx[i] in possible_operations:
            indexes_of_operators.append(i)

    if (len(indexes_of_operators) == 0):
        return -1

    nested_level = 0
    lowest_nested_level = math.inf   
    current_operator = ""     
    index_of_operator = 0                             
    for i in range(len(fx)):
        if fx[i] == "(":
            nested_level += 1
        elif fx[i] == ")":
            nested_level -= 1

        if i in indexes_of_operators and nested_level < lowest_nested_level and not is_inside_function(fx, i): #this line checks if the index of fx is the least indented operator yet and if said operator is NOT part of a function parameter
            lowest_nested_level = nested_level
            current_operator = fx[i]
            index_of_operator = i
    return [current_operator, index_of_operator]

def is_inside_function(fx, index) -> bool: #this method verifies if a certain index is contained in the argument of the following functions: cos(), sin() and ln() | O(n)
    level_of_nest = 0
    for i in range(len(fx[: index])):
        if fx[i] == "(":
            level_of_nest += 1
        elif fx[i] == ")":
            level_of_nest -= 1
    
    current_nest = 0
    for i in range(len(fx[: index])):
        if fx[i] == "(":
            current_nest += 1
        elif fx[i] == ")":
            current_nest -= 1

        if fx[i : i + 3] in list_of_pre or fx[i : i + 2] in list_of_pre:
            current_nest += 1
            if level_of_nest >= current_nest:
                return True
    return False


function_to_derive = get_function()

print(derivative(function_to_derive))