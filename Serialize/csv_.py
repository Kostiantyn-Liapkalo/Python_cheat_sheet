import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, "w", newline='') as f:
        field_names = ["name", "email", "phone", "favorite"]
        csv_writer = csv.DictWriter(f, fieldnames=field_names)
        csv_writer.writeheader()
        for contact in contacts:
            csv_writer.writerow(contact)


def read_contacts_from_file(filename):
    lst = []
    with open(filename, "r", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['favorite'] == "False":
                row['favorite'] = False
            elif row['favorite'] == "True":
                row['favorite'] = True
            lst.append(row)
    return lst


if __name__ == "__main__":

    contacts = [
        {
            "name": "Allen Raymond",
            "email": "nulla.ante@vestibul.co.uk",
            "phone": "(992) 914-3792",
            "favorite": False
        },
        {
            "name": "Chaim Lewis",
            "email": "dui.in@egetlacus.ca",
            "phone": "(294) 840-6685",
            "favorite": False
        }
    ]

    write_contacts_to_file("file.csv", contacts)
    print(read_contacts_from_file("file.csv"))
