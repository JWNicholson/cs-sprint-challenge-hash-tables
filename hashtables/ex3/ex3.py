def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # get array count (how many?)
    arr_count = len(arrays)
    #print(arr_count)
    #initialize dict
    total = {}

    #get total of the first list (position[0] in list of arrays)
    for i in arrays[0]:
        #add all idx to the total dict
        total[i] = 1
    
    #the remaing lists
    for next_arr in arrays[1:]:
        #get total occurances
        for next_i in next_arr:
            #check if its already in total dict
            if next_i in total:
                #increment total at next_1 idx +1
                total[next_i] +=1

        #loop through total dict key:value pairs and set equal to result
        result = [key for (key,val) in total.items() if val == arr_count]
    
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))


#initialize a dict for occurances of each number
#get len of arrays(list) param
#loop through each number in each array to see if is it occurs more than once
#if yes - add 1 each time to the count, otherwise count is one
##