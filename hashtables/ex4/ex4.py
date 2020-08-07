def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    #initialize dict
    numbers = {}
    #initialize an array for results
    result = []

    
    for num in a:
    #add every number to the dictionary 
        numbers[num] = 1

    #if the current number has a corresponding negative add the positive number to negative numbers list, excluding 0
        if num != 0 and -num in numbers:
         result.append(abs(num))


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))


#take an array as an input
#put all into a dictionary
#exclude 0 because it has no negative version
#check if positive AND negative number are both in dict. Putting a - in front of iteration variable makes it negative (for x in array: -x)
#if yes - append to resulting array, but use absolute * abs() * to make it positive which is absolute value