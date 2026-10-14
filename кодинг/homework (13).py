def binary_search(lst, val):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == val:
            return mid

        elif lst[mid] < val:
            left = mid + 1

        else:
            right = mid - 1
    return -1

test_list = [10,20,30,40,50]
print(binary_search(test_list, 30))
print(binary_search(test_list, 99))