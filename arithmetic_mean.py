# The function decimal_average(number_list, signs_count) calculates the arithmetic average of type Decimal with the number of significant digits signs_count. The parameter number_list is a list of numbers.


from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    number_list = list(map(Decimal, number_list))
    return Decimal(sum(number_list) / len(number_list))


if __name__ == "__main__":
    print(decimal_average([31, 55, 177, 2300, 1.57], 9))
