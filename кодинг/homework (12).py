# task 1

# Напишіть функцію, яка повертає суму чисел у вказаному діапазоні. Межі діапазону передаються як параметри. Якщо межі діапазону переплутані (наприклад, 5 — верхня межа, 25 — нижня межа), їх потрібно поміняти місцями.

# def get_sum_in_range(start, end):
#     if start > end:
#         start, end = end, start
#
#     total_sum = 0
#
#     for i in range(start, end + 1):
#         total_sum += i
#
#     return total_sum
#
# print(get_sum_in_range(5, 1))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 2

# Напишіть функцію, що обчислює добуток елементів списку цілих. Список передається як параметр. Отриманий результат повертається з функції.

# def calculate_product_in_list(numbers:list[int]) -> int:
#     product = 1
#
#     for num in numbers:
#         product *= num
#
#         pass
#     return product
#
# my_list = [1, 2, 3, 4, 5]
# print(calculate_product_in_list(my_list))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 3

# Напишіть функцію для знаходження мінімуму в списку цілих. Список передається як параметр. Отриманий результат повертається з функції.

# def find_min_in_list(number_list:list[int]) -> int:
#     minimum = number_list[0]
#
#     for number in number_list:
#         if number < minimum:
#             minimum = number
#
#         pass
#     return minimum
#
# my_list = [18, 5, 24, 3, 7, 12]
# print(find_min_in_list(my_list))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 4

# Напишіть функцію, що визначає кількість простих чисел у списку цілих. Список передається як параметр. Отриманий результат повертається з функції.

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
# def count_primes_in_list(numbers):
#     count = 0
#     for num in numbers:
#         if is_prime(num):
#             count += 1
#     return count
#
# my_list = [1, 2, 3, 4, 5, 7]
# print(count_primes_in_list(my_list))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 5

# Напишіть функцію, що видаляє зі списку цілих деяке задане число. З функції потрібно повернути кількість видалених елементів.

# def remove_element_from_list(numbers, value_to_remove):
#     cleaned_list = []
#     removed_count = 0
#
#     for num in numbers:
#         if num == value_to_remove:
#             removed_count += 1
#         else:
#             cleaned_list.append(num)
#
#     numbers[:] = cleaned_list
#
#     return removed_count
#
# my_list = [1, 2, 3, 2, 4, 2, 5]
# target = 2
#
# print("Number of deleted:", remove_element_from_list(my_list, target))
# print("Cleaned list:", my_list)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 6

# Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків

# def marge_lists(list1, list2):
#     combined_list = []
#
#     for item in list1:
#         combined_list.append(item)
#
#     for item in list2:
#         combined_list.append(item)
#
#     return combined_list
#
# first = [1, 2, 3]
# second = [4, 5, 6]
#
# print("Combined list: ", marge_lists(first, second))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 7

# Напишіть функцію, що вираховує ступінь кожного елемента списку цілих. Значення для ступеня передається як параметр, список теж передається як параметр. Функція повертає новий список, що містить отримані результати.

# def calculate_powers_list(numbers, power):
#     power_results = []
#
#     for num in numbers:
#         result = num ** power
#         power_results.append(result)
#
#     return power_results
#
# my_list = [2, 3, 4, 5]
# exponent = 2
#
# print("Ascension result: ", calculate_powers_list(my_list, exponent))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~