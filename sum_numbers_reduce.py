from functools import reduce

'''
reduce(func, iterable[, initial])
'''

'''
from functools import reduce

result = reduce((lambda x, y: x * y), [1, 2, 3, 4], 3)

print(result)  # 72
'''

'''
from functools import reduce

result = reduce((lambda x, y: x * y), [1, 2, 3, 4])

print(result)  # 24
'''


# The sum numbers(numbers) function, the result of which is the sum of the numbers of all elements of the numbers list.


def sum_numbers(numbers):

    return reduce(lambda x, y: x + y, numbers)


if __name__ == "__main__":
    numbers = [3, 4, 6, 9, 34, 12]
    print(sum_numbers(numbers))
