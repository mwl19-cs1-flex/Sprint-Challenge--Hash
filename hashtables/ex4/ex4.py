def has_negatives(a):

    """
    YOUR CODE HERE
    """
    result = []
    n = {}
    for item in a:
        n[item] = item 
    
    for item in a:
        if item == n[abs(item)] and item*-1 in n:
            if item == 0:
                pass
            else:
                result.append(item)

    return result

# Another solution
# THIS WAS EXPLAINED TO ME AFTER I PASSED
    # hashtable = {}
    # for num in a:
        # if num < 0:
            # hashtable[num] = True
    # for num in a:
        # if (num * -1) in hashtable:
            #results.append(num)
if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
