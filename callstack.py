''''
Callstack and debugging.
'''


text = 'hola!'

def make_upper(text: str) -> str:
    text = text + '!!!'
    return text.upper()


print(len(make_upper(text)))