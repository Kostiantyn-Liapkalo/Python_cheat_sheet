'''
Recursive function encode to encode a list or string. 
As an argument, the function accepts a 
list (for example ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z ", "Z" ]) 
or a string (eg "XXXZZXXYYYZZ"). 
The function returns an encoded list of elements (eg ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]).
'''


def encode(data):
    if len(data) == 0:
        return []
    if len(set(data)) == 1:
        return [data[0], len(data)]

    cnt = 1
    i = 1
    while len(data) > 1:
        if data[i] == data[i - 1]:
            cnt += 1
            i += 1
            continue
        return [data[i - 1], cnt] + encode(data[cnt:])


if __name__ == "__main__":
    print(encode(["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z ", "Z"]))
    print(encode("XXXZZXXYYYZZ"))
