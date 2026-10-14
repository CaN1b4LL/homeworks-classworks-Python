# def print_hello(name):
#     print(f"Hello, {name}")
#
#
# print_hello("Vasya")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def print_number():
#     global num
#     print(num)
#     num = 10
#     print(num)
#
# num = 5
#
#
# print_number()
# print(num)

# def increase(a:int)->int:
#     a += 1
#     return a
#
# a = 1
# a = increase(a)
# print(a)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def compare(str1:str, str2:str)->bool:
#     if str1.lower() == str2.lower():
#         return True
#     return False

#~~~~~~~~~~~~~~~~~~

# def compare(str1:str, str2:str)->bool:
#     return str1.lower() == str2.lower()

# print(compare("hello", "Hello"))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def diff(a:int,b:int)->int:
#     return a - b
#
# print(diff(12,23))
# print(diff(1.2,2.3))

# import random
#
# def fill_list(lst: list[int], start: int, end: int):
#     for i in range(len(lst)):
#         lst[i] = random.randint(start, end)
#     return lst
# l = [0] * 10
#
# print(l)
# l = fill_list(l, -10, 10)
# print(l)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 1

# def get_product_in_range(start, end):
#     if start > end:
#         start, end = end, start
#
#     product = 1
#
#     for i in range(start, end + 1):
#         product *= i
#
#     return product
#
# print(get_product_in_range(5, 25))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 2

# def find_max_in_list(number_list:list) -> int:
#
#     maximum = number_list[0]
#
#     for number in number_list:
#         if number > maximum:
#             maximum = number
#
#     return maximum
#
# my_list = [3, 18, 5, 24, 7, 12]
# print(find_max_in_list(my_list))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 3

# def calculate_sum_in_list(numbers:list[int]) -> int:
#
#     total_sum = 0
#
#     for number in numbers:
#         total_sum += number
#
#     return total_sum
#
# my_list = [10, 20, 30, 40]
# print(calculate_sum_in_list(my_list))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 4

# def analyze_list(numbers):
#
#     evens = 0
#     odds = 0
#     positives = 0
#     negatives = 0
#
#     for num in numbers:
#         if num % 2 == 0:
#             evens += 1
#         else:
#             odds += 1
#
#         if num > 0:
#             positives += 1
#
#         if num < 0:
#             negatives += 1
#
#     print(f"Even numbers: {evens}")
#     print(f"Odd numbers: {odds}")
#     print(f"Positive numbers: {positives}")
#     print(f"Negative numbers: {negatives}")
#
# my_list = [2, -3, 4, -5, 0, 6]
# analyze_list(my_list)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 5

# def reverse_list(numbers:list[int]) -> list[int]:
#
#     reversed_result = []
#
#     for i in range(len(numbers) - 1, -1, -1):
#         reversed_result.append(numbers[i])
#
#     return reversed_result
#
# my_list = [10, 20, 30, 40, 50]
# print(reverse_list(my_list))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 6

# def calculate_factorials_list(numbers:list[int]) -> list[int]:
#
#     factorial_results = []
#
#     for num in numbers:
#         current_factorial = 1
#
#         for i in range(1, num + 1):
#             current_factorial *= i
#
#         factorial_results.append(current_factorial)
#
#     return factorial_results
#
# my_list = [3, 4, 5]
# print(calculate_factorials_list(my_list))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~