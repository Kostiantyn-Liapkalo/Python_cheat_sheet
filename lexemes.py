'''
Python's split() method is used to split a string into pieces, 
and it takes a single argument called separator. 
The delimiter can be any character or symbol.
'''


def token_parser(s):
    
    for sep in ("+", "-", "*", "/", "(", ")"): # lexemes
        l = s.split(sep)  # splitting by lexemes
        s = f" {sep} ".join(l) # join str
        s = s.replace("  ", " ")  # replacing double spaces with single spaces
    return s.split()  # split a string into a list of strings


if __name__ == "__main__":
    print(token_parser("2+ 34-5 * 3"))





