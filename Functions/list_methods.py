def data_preparation(list_data):

    result_list = []

    for l in list_data:
        if len(l) > 3:
            l.remove(min(l))
            l.remove(max(l))
        result_list.extend(l)

    result_list.sort(reverse=True)
    return result_list


if __name__ == "__main__":
    print(data_preparation([[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]))




'''Adding an element to the end of the list: my_list.append(element)

chars = ['a', 'b']
chars.append('c')
print(chars)  # ['a', 'b', 'c']

removing an element from the list will cause an error if such an element is not in the list: my_list.remove(element)

chars = ['a', 'b']
chars.remove('b')
print(chars)  # ['a']

Return the ith element and remove it from the list i_element = my_list.pop(i). By default, i = -1

chars = ['a', 'b']
last = chars.pop(1)
print(chars)  # ['a']
print(last)  # 'b'

Extend the list a_list with elements from b_list: a_list.extend(b_list)

chars = ['a', 'b']
numbers = [1, 2]

chars.extend(numbers)
print(chars)  # ['a', 'b', 1, 2]

Insert x at position with index i: my_list.insert(i, x)

chars = ["a", "b"]
chars.insert(1, "c")
print(chars)  # ['a', 'c', 'b']

Clear list: my_list.clear()

chars = ['a', 'b']
last = chars.clear() print(chars)  # []

Find the index of the first element in the list equal to x: index = my_list.index(x)

chars = ['a', 'b', 'c', 'd']
c_ind = chars.index('c') print(c_ind)  # 2

Check the number of elements in the list equal to x: x_number = my_list.count(x)

chars = ['a', 'b', 'c', 'a']
a_count = chars.count('a')
print(a_count)  # 2

Sort the list in ascending order: my_list.sort(key=None, reverse=False)

chars = ['z', 'a', 'b']
chars.sort()
print(chars)  # ['a', 'b', 'z']

Reverse the order of elements in the list: my_list.reverse()

chars = ['a', 'b']
chars.reverse()
print(chars)  # ['b', 'a']

Return a copy of the list: copy_of_my_list = my_list.copy()

chars = ['a', 'b']
chars_copy = chars.copy()
chars == chars_copy  # True
'''
