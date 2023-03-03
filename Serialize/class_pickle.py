import pickle


class Person:

    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:

    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            self.contacts = []
        else:
            self.contacts = contacts
        self.filename = filename

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            result = pickle.load(file)
            return result
