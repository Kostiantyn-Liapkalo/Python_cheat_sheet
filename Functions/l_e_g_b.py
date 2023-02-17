'''
In Python, the rules for finding names are very simple:

first the search is in the local namespace (LOCAL);
if not found in the local, then in the local at the next level (ENCLOSED) and so on, until the local ends;
then the global (GLOBAL) namespace (module level) will be checked;
and finally the built-in namespace (BUILT INS) are keywords and functions that are part of the Python language.
If no entity with this name is found anywhere, then we will get an exception.

This rule can be remembered by its acronym: (LOCAL, ENCLOSED, GLOBAL, BUILT INS).
'''

# The get_discount_price_customer function is implemented to calculate the price 
# of an online store product.
DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    # print(price)
    # print(customer)
    if "discount" in customer:
        discount = customer["discount"]
    else:
        discount = DEFAULT_DISCOUNT
    return price * (1 - discount)


if __name__ == "__main__":
    print(get_discount_price_customer(10, {'name': 'Boris', 'discount': 0.15}))
