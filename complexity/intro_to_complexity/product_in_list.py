def product_in_list(arr, product):

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] * arr[j] == product:
                return True
            
    return False


test_n = 100
test_arr = [1] * test_n
test_product = 7

print(product_in_list(test_arr, test_product))
