'''
The function finds in the file (parameter path) 
all employees of the specified profession (parameter profession).
'''

path = "file_name.txt"
profession = "courier"


def get_employees_by_profession(path, profession):

    with open(path, "r") as file:
        l = []
        employees = file.readlines()
        employees = [line.strip() for line in employees if line]

        for employee in employees:
            res = employee.find(profession)
            if res != -1:
                l.append(employee)

        str = "".join(l)
        str = str.replace(profession, "")

        return str.strip()
    
# or version 2


# def get_employees_by_profession(path, profession):
#     with open(path, 'r') as reader:
#         result = []
#         r_list = reader.readlines()
#         for i in r_list:
#             if i.find(profession) != -1:
#                 i.removesuffix('\n')
#                 i.strip()
#                 result.append(i)
#         str = ' '.join(result).replace(profession, '')
#         str = str[:-2]
#         return str

