import pickle


def write_contacts_to_file(filename, contacts):
    with open(filename, "wb") as file:
        pickle.dump(contacts, file)


def read_contacts_from_file(filename):
    with open(filename, "rb") as file:
        result = pickle.load(file)
        return result


if __name__ == "__main__":
    filename = r"/home/koss/Desktop/data.bin"
    contacts = [{
        'name': 'Allen Raymond', 
        'email': 'nulla.ante@vestibul.co.uk', 
        'phone': '(992) 914-3792', 
        'favorite': False}, 
                {
        'name': 'Chaim Lewis', 
        'email': 'dui.in@egetlacus.ca', 
        'phone': '(294) 840-6685', 
        'favorite': False}]
    write_contacts_to_file(filename, contacts)
    print(read_contacts_from_file(filename))
