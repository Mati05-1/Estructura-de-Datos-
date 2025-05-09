# from stack import Stack
# from data_structures.stacks.stack import Stack
from stack import Stack
# from memory_profiler import profile


# @profile
def is_palindrome(text: str) -> bool:

    stack_size = len(text) // 2
    s = Stack(stack_size)

    first_half = text[:stack_size]
    second_half = text[-stack_size:]

    # Llenar el stack
    for char in first_half:
        s.push(char)

    # Vaciar el stack y comparar
    for char in second_half:
        popped = s.pop()
        if char != popped:
            return False
    
    return True


# print(is_palindrome('1'*10000))
# print(is_palindrome('hello'))
# print(is_palindrome('199787991'))
# print(is_palindrome('a'))
s = Stack(1)
print(s)
