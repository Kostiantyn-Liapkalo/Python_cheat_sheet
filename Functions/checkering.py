'''
A checker is the transformation of a function from many arguments into a set of functions, 
each of which is a function of a single argument. We can pass some arguments to a function 
and get back a function that expects other arguments.

def sum_func(x, y):
    return x + y


def sub_func(x, y):
    return x - y


OPERATIONS = {
    '-': sub_func,
    '+': sum_func
}


def get_handler(operator):
    return OPERATIONS[operator]


handler = get_handler('-')
handler(2, 3)           # -1

get_handler('+')(2, 3)  # 5

'''

# The discount_price(discount) function will return a function that calculates the price 
# of the product with a discount equal to discount.
def discount_price(discount):

    def get_price(price):
        return price * (1 - discount)

    return get_price


if __name__ == "__main__":
    dsc = discount_price(0.15)
    print(dsc(100))
