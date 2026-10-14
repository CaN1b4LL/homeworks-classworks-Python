# task 1
from unittest import result

# Користувач з клавіатури вводить список цілих чисел. Необхідно порахувати, скільки у списку парних і непарних чисел. Результати вивести на екран.

# numbers = []
#
# even_numbers = 0
# not_even_numbers = 0
#
# while True:
#     num = int(input("Enter integers (enter 0 to complete entry): "))
#     if num == 0:
#         break
#     numbers.append(num)
#
# for n in numbers:
#     if n % 2 == 0:
#         even_numbers += 1
#     else:
#         not_even_numbers += 1
#
# print(f"Even numbers: {even_numbers}")
# print(f"Not even numbers: {not_even_numbers}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 2

# Користувач із клавіатури вводить список цілих чисел. Необхідно визначити максимальне і мінімальне значення у списку. Результати вивести на екран.

# numbers = []
#
# while True:
#     num = int(input("Enter numbers (enter 0 to complete entry): "))
#     if num == 0:
#         break
#     numbers.append(num)
#
# min_number = numbers[0]
# max_number = numbers[0]
#
# for n in numbers:
#     if n > max_number:
#         max_number = n
#     elif n < min_number:
#         min_number = n
#
# print(f"Min number: {min_number}")
# print(f"Max number: {max_number}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 3

# У списку цілих, заповненому випадковими числами, визначити мінімальний, додатний елемент і максимальний, від'ємний елемент, порахувати кількість від'ємних елементів, порахувати кількість додатних елементів, порахувати кількість нулів. Результати вивести на екран.

# import random
#
# numbers = []
# for i in range(10):
#     numbers.append(random.randint(-100, 100))
#
# print(f"Generated list: {numbers}")
#
# negative_count = 0
# positive_count = 0
# zero_count = 0
#
# min_positive = 101
# max_negative = -101
#
# for n in numbers:
#     if n > 0:
#         positive_count += 1
#         if n < min_positive:
#             min_positive = n
#
#     elif n < 0:
#         negative_count += 1
#         if n > max_negative:
#             max_negative = n
#
#     else:
#         zero_count += 1
#
# print(f"Negative count: {negative_count}")
# print(f"Positive count: {positive_count}")
# print(f"Zero count: {zero_count}")
# print(f"Min positive count: {min_positive}")
# print(f"Max negative count: {max_negative}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 4

# Користувач із клавіатури вводить список цілих чисел і деяке число. Необхідно видалити зі списку всі елементи, які менші за задане число. Результат вивести на екран.

# numbers = []
#
# while True:
#     num = int(input("Enter numbers (enter 0 to complete entry): "))
#     if num == 0:
#         break
#     numbers.append(num)
#
# limit = int(input("Enter the limit number: "))
#
# filtered_numbers = []
#
# for num in numbers:
#     if num >= limit:
#         filtered_numbers.append(num)
#
# print(f"filtered numbers: {filtered_numbers}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 5

# Користувач вводить з клавіатури арифметичний вираз. Наприклад, 23+12.
# Необхідно вивести на екран результат виразу. У нашому прикладі це 35. Арифметичний вираз може складатися тільки з трьох частин: число, операція, число. Можливі операції: +, -, *, /.

# expression = input("Enter an arithmetic expression (for example, 23+12): ")
#
# expression = expression.replace(" ", "")
#
# if "+" in expression:
#     parts = expression.split("+")
#     num1 = int(parts[0])
#     num2 = int(parts[1])
#     result = num1 + num2
#     print(f"Result: {result}")
# elif "-" in expression:
#     parts = expression.split("-")
#     num1 = int(parts[0])
#     num2 = int(parts[1])
#     result = num1 - num2
#     print(f"Result: {result}")
# elif "*" in expression:
#     parts = expression.split("*")
#     num1 = int(parts[0])
#     num2 = int(parts[1])
#     result = num1 * num2
#     print(f"Result: {result}")
# elif "/" in expression:
#     parts = expression.split("/")
#     num1 = int(parts[0])
#     num2 = int(parts[1])
#     result = num1 / num2
#     print(f"Result: {result}")
# else:
#     print("Error")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 6

# Користувач із клавіатури вводить список цілих чисел. Необхідно відсортувати цей список так, щоб від'ємні числа залишилися на своїх місцях, а решта елементів були відсортовані за зростанням. Результат вивести на екран.

# numbers = []
#
# while True:
#     num = int(input("Enter numbers (enter 0 to complete entry): "))
#     if num == 0:
#         break
#     numbers.append(num)
#
# positives = []
# for n in numbers:
#     if n > 0:
#         positives.append(n)
#
# positives.sort()
#
# result = []
# pos_index = 0
#
# for n in numbers:
#     if n < 0:
#         result.append(n)
#     else:
#         result.append(positives[pos_index])
#         pos_index += 1
#
# print(f"Sorted list: {result}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~