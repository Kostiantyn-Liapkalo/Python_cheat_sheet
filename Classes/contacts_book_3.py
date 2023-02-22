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
        result = list(
            filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None

    def remove_contacts(self, id):
        remove_contact = list(
            filter(lambda contact: contact["id"] == id, self.contacts))
        self.contacts.remove(remove_contact[0])


phonebook = Contacts()
phonebook.add_contacts('Wylie Pope', '(692) 802-2949',
                       'est@utquamvel.net', True)
phonebook.add_contacts('Cyrus Jackson', '(501) 472-5218',
                       'nibh@semsempererat.com', False)
print(phonebook.list_contacts())
# print(phonebook.get_contact_by_id(2))
phonebook.remove_contacts(1)
print(phonebook.list_contacts())
