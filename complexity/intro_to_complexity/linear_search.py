def linear_search(arr, key):
    
    for i in range(len(arr)):
        if arr[i] == key:
            return True
    
    return False


test_n = 100
test_arr = [7] * test_n
test_key = 8

print(linear_search(test_arr, test_key))
