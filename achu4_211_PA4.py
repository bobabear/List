'''
---------------------------------------------------------------------------------
Name: Amanda Chu
Assignment: PA 4
Due Date: 10/23/2023
---------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by professor and class syllabus.
---------------------------------------------------------------------------------
Comments and Assumptions: A note to the grader as to any problems or
uncompleted aspects of the assignment, as well as any assumptions.
You can write in N/A if you don’t have any comments/assumptions.
---------------------------------------------------------------------------------
NOTE: width of source code should be <=80 characters to be readable on-screen.
12345678901234567890123456789012345678901234567890123456789012345678901234567890
        10       20         30        40        50        60        70        80
---------------------------------------------------------------------------------
'''

def filter_popular(reacts_2D, names, threshold):
    users = [] # new list to append to
    for i in range(len(reacts_2D)): # iterates through the length of reacts_2D
        total = 0 # keeps track of the total number of reactions
        for num in reacts_2D[i]: # iterates through the inner list of reacts_2D
            total += num  # adds the number to total
        if total >= threshold: 
        # check if the total is greater or equal than the threshold
            users.append(names[i]) # add name to users list
    return users


def gather_engagement(names, reacts, grouping):
    output = [] # new list to append the final results
    place = 0 # position in the list
    for name in range(len(names)):  # iterates through the names list
        group_num = grouping[name]  # sets group_num to its value
        out_mini = [] # inner list
        out_mini.append(names[name]) # adds key and value pair to mini list
        for j in range(place, place + group_num): 
        # iterate through place and group_num
            out_mini.append(reacts[j]) # adds value pair to mini list
            place += 1 # moves to next position 
        output.append(out_mini) # adds mini list to output list 
            
    return output


def clear_zeros(reacts_2D):
    non_zeros = [] # new list to append results
    for react in reacts_2D: # iterates through outer lists 
        sub_lst = [] # new list for inner lists
        for num in react: # iterates through inner lists
            if num != 0: # checks if the number is not 0 
                sub_lst.append(num) # add to sub_lst if number isn't 0
        if sub_lst: # checks if the list is empty or not
            non_zeros.append(sub_lst) 
            # adds everything in sub_lst to non_zeros list
    return non_zeros


def form_reactions_list(react_dict1, react_dict2):
    # get all unique keys
    out_list = []
    # for each unique key: is it in list 1? 2? Both? get the sum
    react1_keys = list(react_dict1.keys()) # turn into a list
    for rkey in react_dict2: # iterates through react_dict2 
        react1_keys.append(rkey)
        # add content from react_dict2 to react1_keys
    merge_keys = list(set(react1_keys)) # turn react1_keys into list
    for k in merge_keys: # iterating through merge_keys 
        total = 0 # keeps tracks of the values
        inner_list = [] # sub list
        if k in react_dict1.keys(): #checks if the key is in react_dict1
            total += react_dict1[k] # add value to total
        if k in react_dict2.keys(): #checks if the key is in react_dict2
            total += react_dict2[k] # add value to total
        inner_list = [k, total] # inner list format
        out_list.append(inner_list) # add inner_list to out_list

    return out_list


def form_reactions_dict(reacts_2D):
    new_dict = {} # new dictionary to append results
    total = 0 # keeps track of the values
    for item in reacts_2D: # iterating through reacts_2D
        new_dict[item[0]] = item[1] # set key to its value
        total += item[1] # adds value to total 
    new_dict['total'] = total 
    # create new key 'total' with the value of all values

    return new_dict
