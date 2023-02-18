from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):

        self.keys = []
        for key in self.data:
            if self.data[key] == value:
                self.keys.append(key)
        return self.keys
