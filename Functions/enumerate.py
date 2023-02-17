'''
The function to_indexed(start_file, end_file) reads the contents of the file, adds to
serial number of the read lines and saves them in this form in a new file.
'''

def to_indexed(source_file, output_file):

    lst = []

    with open(source_file, "r") as in_file:
        text = in_file.readlines()
        print(text)

        for num, line in enumerate(text):
            s = f"{num}: {line}"
            lst.append(s)
            print(s)
    print(lst)

    with open(output_file, "w") as out_file:
        for s in lst:
            out_file.write(f"{s}")
            print(out_file)
