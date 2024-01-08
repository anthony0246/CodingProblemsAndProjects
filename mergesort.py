def sort_and_combine(small_list1, small_list2):
    list_to_return = []
    initial_length = len(small_list1 + small_list2)
    for i in range(initial_length):
        if len(small_list1) != 0 and len(small_list2) != 0:
            if small_list1[0] < small_list2[0]:
                list_to_return.append(small_list1[0])
                small_list1.pop(0)
            else: 
                list_to_return.append(small_list2[0])
                small_list2.pop(0)
    else:
        if len(small_list1) != 0:
            return list_to_return + small_list1
        else:
            return list_to_return + small_list2

def merge_sort(liste):
    first_half = liste[0 : (len(liste))//2 ]
    middle = liste[len(liste) // 2 : len(liste) // 2 + 1]
    second_half = liste[(len(liste))//2 + 1 : ]
    if len(first_half) <= 1:
        sorted_list = sort_and_combine(first_half, second_half)
        sorted_list = sort_and_combine(sorted_list, middle)
        return sorted_list
    return sort_and_combine(sort_and_combine(merge_sort(first_half), merge_sort(second_half)), middle)
    
    
print(merge_sort([67, 10]))