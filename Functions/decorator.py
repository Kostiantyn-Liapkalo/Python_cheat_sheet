'''
There is such a design template — Decorator. This pattern is to extend the existing 
functionality without making changes to the code of this functionality itself.
'''

# The decorator adds the prefix +38 to short numbers, 
# and for a full international number (with 12 characters) - only the '+' sign.
def format_phone_number(func):

    def wrapper(num):

        new_num = func(num)
        if len(new_num) == 12:
            return f"+{new_num}"
        elif not num.startswith("+38"):
            return f"+38{new_num}"

    return wrapper


@format_phone_number
def sanitize_phone_number(phone):

    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


if __name__ == "__main__":
    print(sanitize_phone_number('  +38(073)123-45-67'))
