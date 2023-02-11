'''
Let's analyze a simple technique of coding and decoding based on series. 
For example, we have a list with repeated observations of some quantity, 
it can take the values X, Y or Z. The values ​​appear in a random order and 
we store them in the list ["X", "X", "X", "Z ", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"] 
or the string "XXXZZXXYYYZZ".

As a result, we can reduce the amount of information stored? 
Compression can be achieved by replacing a group of repeating values with a single value 
and a repetition counter: ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]

A recursive decode function to decode a list encoded in this way. 
The function accepts an encoded list as an argument. 
The function returns a decrypted list of elements.
'''



def decode(data):
    if len(data) == 0:
        return []

    if data[1] == 1:
        return [data[0]] + decode(data[2:])

    if data[1] > 1:
        return [data[0]] * int(data[1]) + decode(data[2:])



# Decoding without recursion:

# def decode(data):
#     s = ""
#     for i in range(0, len(data), 2):
#         s += data[i] * int(data[i + 1])
#
#     return list(s)


if __name__ == "__main__":
    print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))
