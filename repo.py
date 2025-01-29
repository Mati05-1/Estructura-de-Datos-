'''
'Array' elements in memory.
'''


arr = [1, 2, 3, 4, 5]

for i in range(5):
    print('Element {} is in address: {}'.format(arr[i], id(arr[i])))