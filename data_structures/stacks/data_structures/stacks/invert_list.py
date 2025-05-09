from memory_profiler import profile
from stack import Stack
import time


# start_time = time.time()

@profile
def invert_list(og_list: list, verbose=False):

    s = Stack(len(og_list))
    new_list = []

    if verbose:
        print(f'\nLista original: {og_list}')
        print('\n', s)

    # Poblar stack
    for element in og_list:
        s.push(element)

    if verbose:
        print('\n', s)

    # Poblar nueva lista
    while s.peek() != 'underflow':
        popped = s.pop()
        new_list.append(popped)

    if verbose:
        print(f'\nNew list: {new_list}')


test_list = ['A', 'B', 'C', 'D'] * 1000
invert_list(test_list, False)
