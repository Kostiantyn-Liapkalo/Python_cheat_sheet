
# The get_emails function receives the list_contacts list as a parameter 
# and returns a list containing the email addresses of all contacts from the list_contacts list.


def get_emails(list_contacts):

    lst = list(map(lambda x: x.get("email"), list_contacts))
    return lst


if __name__ == "__main__":
    print(get_emails([{
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    }]))
