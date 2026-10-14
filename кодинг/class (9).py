# def find_first_max_index(numbers):
#     max_index = 0
#
#     for i in range(1, len(numbers)):
#         if numbers[i] > numbers[max_index]:
#             max_index = i
#
#     return max_index
#
# test_list = [3, 5, 9, 1, 4, 9, 2]
# print(find_first_max_index(test_list))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def find_last_min_index(numbers:list[int]) -> int:
#     min_index = 0
#
#     for i in range(1, len(numbers)):
#         if numbers[i] <= numbers[min_index]:
#             min_index = i
#
#     return min_index
#
# test_list = [5, 1, 8, 3, 1, 7]
# print(find_last_min_index(test_list))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def product_of_odds(numbers:list[int]) -> int:
#     sum_product = 1
#
#     for num in numbers:
#         if num % 2 != 0:
#             sum_product *= num
#
#     return sum_product
#
# test_list = [2,6,9,3,6,3]
# print(product_of_odds(test_list))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def sum_even_positions(numbers:list[int]) -> int:
#     total_sum = 0
#
#     for i in range(len(numbers)):
#         if i % 2 == 0:
#             total_sum += numbers[i]
#
#     return total_sum
#
# test_list = [0,1,2,3,4,5,6,7,8,9]
# print(sum_even_positions(test_list))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~