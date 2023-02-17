# A FIFO data structure is implemented using the deque collection. A fifo variable containing the deque collection is created. 
# Size limited by MAX_LEN constant. The push function adds the element value to the end of the fifo list. 
# The pop function retrieves and returns the first value from the fifo list.


from collections import deque

MAX_LEN = 5

fifo = deque(maxlen=MAX_LEN)


def push(element):

    fifo.append(element)
    return fifo


def pop():

    first = fifo.popleft()
    return first


if __name__ == "__main__":
    for num in range(1, 10):
        push(num)
    pop()
    print(fifo)
