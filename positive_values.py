
# The positive_values function filters the payment list by positive values using the filter function, 
# and returns it from the function.


def positive_values(list_payment):

    return list(filter(lambda x: x > 0, list_payment))


if __name__ == "__main__":
    payment = [100, -3, 400, 35, -100]

    print(positive_values(payment))



# some_str = 'aaAbbB C F DDd EEe'
# for i in filter(lambda x: x.islower(), some_str):
#     print(i)