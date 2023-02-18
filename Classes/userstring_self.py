from collections import UserString


class NumberString(UserString):

    def number_count(self):

        n = 0
        for i in self.data:
            if i.isdigit():
                n += 1
        return n
