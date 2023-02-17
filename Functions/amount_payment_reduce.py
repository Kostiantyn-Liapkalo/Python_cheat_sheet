
# The amount_payment function returns the payment amount at the end of the month.

from functools import reduce


def amount_payment(payment):

    return reduce(lambda x, y: x+y, filter(lambda x: x > 0, payment))


if __name__ == "__main__":
    payment = [100, -3, 400, 35, -100]
    print(amount_payment(payment))
