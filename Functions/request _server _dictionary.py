'''
When working with web services, communication, using the HTTP protocol, 
most often takes place in JSON format. 
And sending data to the server in a POST request is the need to use a dictionary, 
because the structure of the JSON format is identical to the Python dictionary.
'''
keys = ''
values = ''

def make_request(keys, values):
    # If the lengths of keys and values do not match, return an empty dictionary
    return dict(zip(keys, values)) if len(keys) == len(values) else dict()
