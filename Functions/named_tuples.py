'''
The convert_list(cats) function works in two modes.

If the convert_list function accepts a list of named tuples in the cats parameter

[Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
Then the function will return the following list of dictionaries:

[
     {"nickname": "Mick", "age": 5, "owner": "Sara"},
     {"nickname": "Barsik", "age": 7, "owner": "Olga"},
     {"nickname": "Simon", "age": 3, "owner": "Yura"},
]
And at the same time, if the convert_list function accepts a list of dictionaries in the cats parameter, 
the result will be the reverse operation and the function will return a list of named tuples.
'''

import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):

    a = type(cats)
    if isinstance(cats[0], dict):
        lst = []
        for c in cats:
            d = (c.values())
            a = Cat(*d)
            lst.append(a)
        return lst

    if isinstance(cats[0], Cat):
        lst = []
        for cat in cats:
            lst.append(cat._asdict())

        return lst


if __name__ == "__main__":
    print(convert_list([Cat("Mick", 5, "Sara"), Cat(
        "Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]))
    print(convert_list([{'nickname': 'Mick', 'age': 5, 'owner': 'Sara'}, {
          'nickname': 'Barsik', 'age': 7, 'owner': 'Olga'}, {'nickname': 'Simon', 'age': 3, 'owner': 'Yura'}]))
