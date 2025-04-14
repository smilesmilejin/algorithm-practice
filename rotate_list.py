# Add your clarifying questions here
# Will the value of shift_by always be positive? 
    # Yes, always a positive shift by 
# Is the list always non-empty? 
    # An empty list will just return an empty
# Will the shift alway be to the right?
    # Yes, we wil never shift to the left
# What if the shift_by is larger than our length?
    # Shift by will be alwasy be less than the length
    # let group decide
# Are we allowed to use built ins(pop, insert)?

# if there is only one element in the list, return the list?
# return None, shift out of bounds

# input : [1, 2, 3] , 2
# output: [2, 3, 1]\
#asssert rotate_list([1, 2, 3], 2) = [2, 3, 1]

# input: ['a', 'b', 'c', 'd'] , 1
# output": ['d','a','b', 'c']


# input = [9], 5233
# output: None, or shift out of bounds  

# Method 1
def rotate_list(list, shift_by):
    if not list:
        return []
    if len(list) < shift_by:
        return f"shift_by {shift_by} is out of bounds"
    if len(list) == 1:
        return list
    
    updated_list = [None] * len(list) # update_list = [None, None, None]

    for i in range(len(list)):
        if i + shift_by > len(list) - 1:
            updated_list[i+shift_by-len(list)] = list[i]
            continue
        updated_list[i+shift_by] = list[i]

    return updated_list

result = rotate_list(['a', 'b', 'c', 'd'] , 1)
print(result)

# Method 2 hard code, not add a new list!
def rotate_list(list, shift_by):
    if not list:
        return []
    if len(list) < shift_by:
        return f"shift_by {shift_by} is out of bounds"
    if len(list) == 1:
        return list

    return list[(len(list) - shift_by): len(list)] + list[0: (len(list) - shift_by)]


    # This also works
    # return list[(len(list) - shift_by): ] + list[: (len(list) - shift_by)]
result = rotate_list([1, 2, 3] , 2)
print(result)
