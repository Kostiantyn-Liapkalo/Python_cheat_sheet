'''
A sublist is a list that is part of a larger list. A sublist can contain one element, multiple elements, or be empty.

For example, [1], [2], [3] and [4] are subscripts of the list [1, 2, 3, 4]. 
The list [2, 3] is also part of [1, 2, 3, 4], but the list [2, 4] is not a sublist of [1, 2, 3, 4], 
because in the original list the numbers 2 and 4 are not neighbors.

An empty list is a sublist of any list.
''' 


def all_sub_lists(data):
    lst_sublists = [[]]
    for i in range(len(data)): 
        # print(i)
        for j in range(len(data)): 
            # print(j)
            if j + i < len(data):
                lst_sublists.append(data[j:j + i + 1])
                # print(lst_sublists)
    return lst_sublists


if __name__ == "__main__":
    print(all_sub_lists([4, 6, 1, 3]))




