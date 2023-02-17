
# The generator_numbers function parses a string and finds all the integers in it and works as a generator 
# that will return the specified numbers when called in a loop.
def generator_numbers(string=""):

    if len(string) == 0:
        return
    else:
        for w in string.split():
            w = w.strip("$.,")
            if w.isdigit():
                yield int(w)


def sum_profit(string):

    s = 0
    for n in generator_numbers(string):
        s += n
    return s


if __name__ == "__main__":
    string = """The resulting profit was: from the southern possessions $ 100, 
    from the northern colonies $500, and the king gave $1000."""

    print(sum_profit(string))
