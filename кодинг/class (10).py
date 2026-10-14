#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~СОРТУВАННЯ БУЛЬБАШКОЮ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# from random import randint as rand
# from time import time


# def bubble_sort(lst:list[int]):
#     for i in range(len(lst)):
#         for j in range(len(lst)-1, i, -1):
#             if lst[j] < lst[j-1]:
#                 lst[j], lst[j-1] = lst[j-1], lst[j]
#
# l = [1,5,3,7,2]
# print(l)
# bubble_sort(l)
# print(l)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def select_sort(lst:list[int]):
#     for i in range(len(lst)):
#         min_pos = i
#         for j in range(i+1, len(lst)):
#             if lst[j] < lst[min_pos]:
#                 min_pos = j
#
#         lst[i], lst[min_pos] = lst[min_pos], lst[i]
#
# l = [1,5,3,7,2]
# print(l)
# select_sort(l)
# print(l)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# def insertion_sort(lst:list[int]):
#     for i in range(1,len(lst)):
#         key = lst[i]
#         j = i-1
#         while j >= 0 and lst[j] > key:
#             lst[j+1] = lst[j]
#             j -= 1
#         lst[j+1] = key
#
#
# test_list = [2,9,5,1,6,5]
# print(test_list)
# insertion_sort(test_list)
# print(test_list)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Recursion ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def factorial(num: int) -> int:
#     prod = 1
#     for i in range(1, num + 1):
#         prod *= i
#     return prod
#
# def factorial_r(num: int) -> int:
#     if num < 2:
#         return 1
#     return num * factorial_r(num - 1)
#
# print(f"I 3!: {factorial(3)}")
# print(f"R 3!: {factorial_r(3)}")
# print(f"I 5!: {factorial(5)}")
# print(f"R 5!: {factorial_r(5)}")


# def digits_counter(num: int) -> int:
#     if num < 10:
#         return 1
#     return 1 + digits_counter(num // 10)
#
# print(digits_counter(234))

# def sum_digits(num: int) -> int:
#     if num < 10:
#         return num
#     return num % 10 + sum_digits(num // 10)
#
# print(sum_digits(234))

# def reverse_sum(num: int):
#     if num < 10:
#         print(num)
#     else:
#         print(num % 10, end=" ")
#         reverse_sum(num // 10)
#
# reverse_sum(123)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Fast Sort ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def quick_sort(lst:list[int])->list[int]:
#     if len(lst) <= 1:
#         return lst
#     tmp = lst[0]
#     left_part = []
#     right_part = []
#     for item in lst[1:]:
#         if item <= tmp:
#             left_part.append(item)
#         else:
#             right_part.append(item)
#     return quick_sort(left_part) + [tmp] + quick_sort(right_part)
#
#
# def fill_list(lst:list[int]):
#     for i in range(len(lst)):
#         lst[i] = rand(-10000, 10000)
#
# l = [0]*20000
#
# fill_list(l)
# start = time()
# bubble_sort(l)
# end = time()
# print(f"Bubble sort: {end - start}")
#
# fill_list(l)
# start = time()
# select_sort(l)
# end = time()
# print(f"Select sort: {end - start}")
#
# fill_list(l)
# start = time()
# insertion_sort(l)
# end = time()
# print(f"Insertion sort: {end - start}")
#
# fill_list(l)
# start = time()
# quick_sort(l)
# end = time()
# print(f"Quick sort: {end - start}")
#
# fill_list(l)
# start = time()
# l = sorted(l)
# end = time()
# print(f"Standard sort: {end - start}")


# print(l)
# l = quick_sort(l)
# print(l)