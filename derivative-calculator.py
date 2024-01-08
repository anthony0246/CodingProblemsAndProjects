#This program calculates the derivative of common functions and can apply the chain rule. 

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

possible_operations = ["*", "/", "+", "-", "^"]

def derivative(function_to_derive):
    #check which derivative rule to apply (product or quotient), if necessary
        #do the derivative 
    
    function_to_derive = remove_extra_brackets(function_to_derive)
    function_to_derive = function_to_derive.replace(" ", "")
    
    split_multi = do_apply_product(function_to_derive)
    split_div = do_apply_quotient(function_to_derive)

    if type(split_multi) != bool:
        #call function that splits function_to_derive at the multiplication
        return apply_product_rule(remove_extra_brackets(function_to_derive[: split_multi]), remove_extra_brackets(function_to_derive[split_multi + 1 :]))
    elif type(split_div) != bool:
        #call function that splits function_to_derive at the division
        return apply_quotient_rule(remove_extra_brackets(function_to_derive[: split_div]), remove_extra_brackets(function_to_derive[split_div + 1 :]))
    elif do_addition_or_substraction(function_to_derive) == True:
        #find the first part of function_to_derive (by finding the first addition or minus symbol)
        #derive that part and apply the chain rule, if necessary
        return addition_or_substraction_derivative(function_to_derive)

    #check if remaining function is one of the base cases   

    if len(function_to_derive) >= 3:
        function_to_derive = list(function_to_derive)
        first_pop = function_to_derive.pop(0)
        last_pop = function_to_derive.pop(-1)
        function_to_derive = "".join(function_to_derive)

    if function_to_derive.isnumeric():
        return "0"
    
    if len(function_to_derive) >= 3:
        function_to_derive = str(first_pop) + function_to_derive + str(last_pop)

    if check_if_base_other_than_polynomial(function_to_derive) == True:
        return find_function(function_to_derive)
    elif type(check_if_polynomial(function_to_derive)) != bool:
            return help_with_power_functions(check_if_polynomial(function_to_derive))
    else:
        return "something ain't right...."
    
def apply_product_rule(fx, gx): 
    #applies the product rule, by taking two functions as an input
    return f"{derivative(fx)}*{gx} + {fx}*{derivative(gx)}"

def apply_quotient_rule(fx, gx):
    #applies the quotient rule, by taking two functions as an input
    return f"({derivative(fx)}*{gx} - {fx}*{derivative(gx)}/{gx}^2"

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

def help_with_power_functions(fx):
    #Applies the power rule to a function
    index_of_power = 0
    for i in range(len(fx)):
        if fx[i] == "^":
            index_of_power = i
            break

    if index_of_power == 0:
        return f"1"

    fx = list(fx)
    fx.pop(0)
    fx.pop(-1)
    index_of_power -= 1
    fx = "".join(fx)
    fx = fx.replace("(", "")
    fx = fx.replace(")", "")
    
    place_of_coef = fx[: index_of_power - 1]
    place_of_power = fx[index_of_power + 1 :]
    
    coef = int(place_of_power)
    power = int(place_of_power) - 1
    
    derivative = f"({coef}x^({power}))"
    
    return derivative
            
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
    
def remove_extra_brackets(fx):
#removes any unecessary brackets. To be called after every recursive call of derivative()
    bracket_count = 0
    for i in range(len(fx)):
        if fx[i] == "(":
            bracket_count += 1
        elif fx[i] == ")":
            bracket_count -= 1
            
    fx = list(fx)
    if bracket_count == 1:
        fx.pop(0)
    elif bracket_count == -1:
        fx.pop(-1)
    fx = "".join(fx)
    
    indexes_of_protected_brackets = []
    i = 0
    while i < len(fx) and len(fx) >= 3:
        if fx[i : i + 3] == "cos" or fx[i : i + 3] == "sin":
            bracket_count = 0
            done_with_function = False
            i += 3
            indexes_of_protected_brackets.append(i)
            while not done_with_function:
                if fx[i] == "(":
                    bracket_count += 1
                elif fx[i] == ")":
                    bracket_count -= 1
                
                if bracket_count == 0:
                    indexes_of_protected_brackets.append(i)
                    done_with_function = True
                i += 1
        i += 1

    i = 0
    while i < len(fx) and len(fx) >= 3:
        if fx[i] == "^" or fx[i] == "n":
            bracket_count = 0
            done_with_function = False
            i += 1
            indexes_of_protected_brackets.append(i)
            while not done_with_function:
                if fx[i] == "(":
                    bracket_count += 1
                elif fx[i] == ")":
                    bracket_count -= 1
                
                if bracket_count == 0:
                    indexes_of_protected_brackets.append(i)
                    done_with_function = True
                i += 1
        i += 1
        
    fx = list(fx)
    j = 0
    pop_count = 0
    while j < len(fx) - pop_count:
        if (fx[j] in list_for_check_poly) and (fx[j] == fx[j + 1]) and (j not in indexes_of_protected_brackets) and (j + 1 not in indexes_of_protected_brackets):
            for i in range(len(indexes_of_protected_brackets)):
                if indexes_of_protected_brackets[i] > j:
                    indexes_of_protected_brackets[i] -= 1 
            fx.pop(j)
            pop_count += 1
        else:
            j += 1
            
        if j + 1 == len(fx):
            break
        
    fx = "".join(fx)
    return fx         

function_to_derive = input("Please input your function here: ")

print(derivative(function_to_derive))