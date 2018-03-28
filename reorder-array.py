def reorderArray(data, order):
    # data =  ["E", "A", "D", "B", "C"]
    # order = [ 4,   0,   3,   1,   2 ]

    made_swap = False
    i = 0

    while i < len(data):
        curr_index = i
        new_index = order[i]
        if curr_index != new_index:
            data[i], data[new_index] = data[new_index], data[i]
            order[i], order[new_index] = order[new_index], order[i]
            made_swap = True
            i += 1
        else:
            i += 1
        if i == len(data):
            if made_swap == True:
                i = 0
                made_swap = False
    return data