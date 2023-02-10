'''
- The function opens the file using with along the path in the mode of adding information
- Writes the additional_info line to the end of the file
- After recording, the function opens the same file for reading
- Reads and returns a string from position start_pos of length count_chars using the seek function.
'''

path = "name_file.txt"
additional_info = "Hello"
start_pos = 10
count_chars = 5


def file_operations(path, additional_info, start_pos, count_chars):
    
    with open(path, "a") as file:
        file.write(additional_info)
    with open(path, "r") as file:
        text = file.read()
        file.seek(start_pos)
        text2 = file.read(count_chars)
        
    return text2
