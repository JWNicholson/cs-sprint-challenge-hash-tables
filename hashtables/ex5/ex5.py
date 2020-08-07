# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    #initalize empty list for results
    result = []
    #initialize a dictionary
    directory = {}

    for file in files:
        #split to get the file name
        split_path = file.split("/")
        filename = split_path[-1]

        #add to dict if not already in there
        if filename not in directory:
            directory[filename] = []

            #add the current path using filename as key
            directory[filename].append(file)

        #iterate the queries param
        for query in queries:
            #if file is found add the path to result
            if query in directory:
                result.extend(directory[query])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))


#the filename is th last part of the path so split on / and get the last one
#add to dict if needed
#add current path to dict using filename as key
#iterate through the queries, looking for the correct file
#if file is found add the path to result. extend() adds the elements to the end of current list
