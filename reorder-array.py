def reorderArray(data, order):
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


def reorderArrayTwo(data, order):
    index = 0

    for i in range(len(data)):
        new_index = order[index]
        if index != new_index:
            data[index], data[new_index] = data[new_index], data[index]
            order[index], order[new_index] = order[new_index], order[index]
        else:
            index += 1
        i += 1
    return data



data =  ["E", "A", "D", "B", "C", "F", "I"]
order = [ 4, 5, 3, 1, 2, 6, 0]

print reorderArrayTwo(data, order)