'''
Stack testing
'''


from stack import Stack


s1 = Stack(5)
print(s1)

# Pushes
s1.push('A')
print(s1)
s1.push('B')
print(s1)
s1.push('C')
print(s1)
s1.push('D')
print(s1)
s1.push('E')
print(s1)
print('Peeked:', s1.peek())
# s1.push('F')
# print(s1)

# Pops
s1.pop()
print(s1)
s1.pop()
print(s1)
s1.pop()
print(s1)
print('Peeked:', s1.peek())