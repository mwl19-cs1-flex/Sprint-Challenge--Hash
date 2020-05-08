def get_indices_of_item_weights(weights, length, limit):
    item_1 = None
    item_2 = None
    for i in weights:
        print('i', i)
        for j in range(1, length):
            print('j', weights[j])
            if i + weights[j] == limit:
                item_1 = i
                item_2 = j
                print('hit') 

    return (item_1, item_2)

weightlist = [1, 3, 5, 7, 9, 11]
get_indices_of_item_weights(weightlist, 6, 4)