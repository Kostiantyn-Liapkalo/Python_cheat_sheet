'''
Syntax of lambda functions:

begins with the lambda keyword, followed by a comma-separated list of positional function arguments (there may be no arguments);
followed by a colon;
next comes the body of the function, strictly one expression;
the result of the expression will be returned as a lambda result (return is not required).

"bad tone" to store lambda functions in variables, 
they should be created in the same place where they are used and leave no traces 
anywhere else in the code.
'''

# The normal_name function accepts a list of names and returns a list of names, 
# but with the correct names in capital letters.
def normal_name(list_name):

    return list(map(lambda x: x.capitalize(), list_name))


if __name__ == "__main__":
    name = ["dan", "jane", "steve", "mike"]

    print(normal_name(name))
