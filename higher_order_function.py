# The higher-order function get_student_grade takes the option parameter. 
# If it is equal to "grade", then the function returns the get_grade function, 
# and if its value is "description", then it returns the get_description function. 
# If the value of the parameter did not match the specified values, 
# the get_student_grade function should return None.


def get_grade(key):
    grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
    return grade.get(key, None)


def get_description(key):
    description = {
        "A": "Perfectly",
        "B": "Very good",
        "C": "Good",
        "D": "Satisfactorily",
        "E": "Enough",
        "FX": "Unsatisfactorily",
        "F": "Unsatisfactorily",
    }
    return description.get(key, None)


def get_student_grade(option):
    if option == "grade":
        return get_grade
    elif option == "description":
        return get_description
    else:
        return None


if __name__ == "__main__":
    a = get_student_grade("grade")
    b = get_student_grade("description")
    print(a("A"))
    print(b("A"))


