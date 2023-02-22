class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for contact in self.contacts:
            if id == contact["id"]:
                return contact


phonebook = Contacts()
phonebook.add_contacts('Wylie Pope', '(692) 802-2949',
                       'est@utquamvel.net', True)
phonebook.add_contacts('Cyrus Jackson', '(501) 472-5218',
                       'nibh@semsempererat.com', False)
print(phonebook.get_contact_by_id(2))
