def intersection(arrays):
    result = []
    d = {}
    """
    YOUR CODE HERE
    """
    for item in arrays[0]:
        d[item] = 0

    for array in arrays:
        for item in array:
            if item in d:
                d[item] += 1
            else: 
                pass

    for item in d: 
        if d[item] == len(arrays):
            result.append(item)
    
    return result

    


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1,5)) + [1,2,3])
    arrays.append(list(range(2,6)) + [1,2,3])
    arrays.append(list(range(3,7)) + [1,2,3])

    print(intersection(arrays))
