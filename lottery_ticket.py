# The function randomly selects a set of numbers for a lottery ticket. There are no duplicates among these numbers.


from random import randrange


def get_numbers_ticket(min, max, quantity):
    
    if not quantity or min < 1 or max > 1000 or max - min < quantity:
        return []
    dct = {}
    while len(dct) < quantity:
        num = randrange(min, max+1)
        if num not in dct:
            dct[num] = num
    return sorted(dct)


if __name__ == "__main__":
    print(get_numbers_ticket(1, 88, 8))
