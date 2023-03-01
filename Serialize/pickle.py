import pickle


def write_contacts_to_file(filename, contacts):
    with open(filename, "wb") as file:
        pickle.dump(contacts, file)


def read_contacts_from_file(filename):
    with open(filename, "rb") as file:
        result = pickle.load(file)
        return result


if __name__ == "__main__":
    filename = r""
    contacts = [
        {
            "name": "Allen Raymond",
            "email": "nulla.ante@vestibul.co.uk",
            "phone": "(992) 914-3792",
            "favorite": False,
        },
        {
            "name": "Alisa Porter",
            "email": "alisa2015@gmail.com",
            "phone": "(067) 111-11-11",
            "favorite": True,
        }]
    write_contacts_to_file(filename, contacts)
    print(read_contacts_from_file(filename))
