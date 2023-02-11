'''
Recursion is what we call the technology of calling a function to itself. 
Such a function is called recursive. Since there is a reference to itself in the description 
of the function, it must arrive at a final solution, otherwise we will get an infinite call. 
Therefore, a recursive function must reach the final result at least once without calling itself. 
This method is called the base case, other variants in which the function calls itself are 
called recursive cases.

Where can recursion be useful? In practice, recursion is used when faced with, 
for example, tree-like data structures: traversal of directories on disk, 
bottom-up method of grammar analysis for a programming language compiler.

We calculate the factorial of the number n using recursion
param n is the number for which the factorial must be calculated
return factorial of number n
def factorial(n):
     if n < 2:
         return 1 # Base case
     otherwise:
         return n * factorial(n - 1) # Recursive case


num = int(input("Enter a positive integer: "))
result = factorial(num)
print(f"The factorial of the number {num} is {result}")
'''

#example
'''
If the input list is empty, then:
   We return an empty list
If the first element of the list is a list, then:
   We get the first list by recursively calling the function with the first element of the list
   We get the second list by recursively calling the function with the rest of the list without the first element
   We return the concatenation of two lists
If the first element of the list is not a list, then:
   We get the first list from the first element of the list
   We get the second list by recursively calling the function with the rest of the list without the first element
   We return the concatenation of two lists
'''


def flatten(data):
    if len(data) == 0:
        return []
    if isinstance(data[0], list):
        return flatten(data[0]) + flatten(data[1:])
    return data[:1] + flatten(data[1:])


if __name__ == "__main__":
    print(flatten([1, 2, [3, 4, [5, 6]], 7]))
