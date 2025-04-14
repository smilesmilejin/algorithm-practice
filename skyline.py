# Add your clarifying questions here
# Find smallest in the list, anythin above that is you could seens, order there is ascending order with no repeats

# Only one elemetn in the list? return None
# if the list if empty? return None
# if the elemenets are all the same? return None
# if the elements are not numbers? assume they are all numbers


# Given a list [-1, 1, 3, 7, 7, 3] determine which values could be "seen."
# The output should be: [1,3,7]


def skyline(building_list):
    if not building_list:
        return None
    if len(building_list) == 1:
        return None
    
    # bottom_floor = min(building_list, key=lambda element: element)
    bottom_floor = min(building_list)
    top_floor = max(building_list)

    seen_list = []
    previous_floor = float('-inf')

    for floor in building_list:
        # If it reaches the top floor, nothing else could be seen, exit the loop
        if floor == top_floor:
            seen_list.append(floor)
            break
        if (floor > bottom_floor) and (floor > previous_floor):
            seen_list.append(floor)
            previous_floor = floor
    
    return seen_list


result = skyline([-1, 1, 3, 7, 7, 3])
print(result)