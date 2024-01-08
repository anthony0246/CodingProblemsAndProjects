def switch(l): #reverses the order of elements in a list (for example, item at index 0 switches with index n-1, 1 with n-2....)
    if len(l) > 2:
        beginning = l[0]
        end = l[-1]
        return [end] + switch(l[1:-1]) + [beginning] # returns the switched elements with edged of list
    else:
        if len(l) == 2: 
            beginning = l[0]
            end = l[1]
            return [end, beginning]
        else:
            return l
    
    

liste = ["a", "b", "c", "d", "e", "f", "g"]
print(switch(liste))