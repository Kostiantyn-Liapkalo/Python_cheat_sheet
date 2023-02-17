# The LIFO data structure is implemented using the deque collection. A lifo variable containing the deque collection is created. 
# Size limited by MAX_LEN constant. The push function adds the element value to the beginning of the lifo list. 
# The pop function retrieves and returns the first value from the lifo list.


from collections import deque

MAX_LEN = 10
lifo = deque(maxlen=MAX_LEN)


def push(element):

    lifo.insert(0, element)
    return lifo


def pop():

    first = lifo.popleft()
    return first


if __name__ == "__main__":
    for num in range(1, 5):
        push(num)
    pop()
    print(lifo)
