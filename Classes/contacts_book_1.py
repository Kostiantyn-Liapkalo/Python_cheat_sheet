class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        contact = {
            "id": Contacts.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite,
        }
        self.contacts.append(contact)
        Contacts.current_id += 1


phonebook = Contacts()
phonebook.add_contacts('Wylie Pope', '(692) 802-2949',
                       'est@utquamvel.net', True)
phonebook.add_contacts('Cyrus Jackson', '(501) 472-5218',
                       'nibh@semsempererat.com', False)
print(phonebook.list_contacts())
