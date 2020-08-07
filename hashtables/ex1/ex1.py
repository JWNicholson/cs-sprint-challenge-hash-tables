def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}

    #loop through dictionary - is the key present?
    for i in range(length):
        w = hash_table.get(limit-weights[i])

        ##it is -
        if w != None:
            return i, w

        #set hash_table weight index = i
        hash_table[weights[i]] = i

    return None

# limit is the number which to look for 2 indices to add up to
## - find 2 indices of respective input that add up to limit
#initialize a dictionary as a hash table
#loop through dictionary - is the key present?
##if yes - get the limit minus the weights at the nth index
#set hash table wieghts at nth index equal to n