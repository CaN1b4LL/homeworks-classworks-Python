# task 1

# Напишіть функцію, яка відображає на екран форматований текст

# def show_gates_quote():
#     print("\"Don't compare yourself with anyone in this world…\n    \033[31mif\033[0m \033[97myou\033[0m \033[31mdo so\033[0m, \033[97myou are insulting yourself.\033[0m\"\n       \033[97mBill Gates\033[0m")
#
# show_gates_quote()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 2

# Напишіть функцію, яка приймає два числа як параметр і відображає всі парні числа між ними.

# def show_even_numbers(start, end):
#     for i in range (start, end + 1):
#         if i % 2 == 0:
#             print(i, end=" ")
#
# show_even_numbers(1, 10)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 3

# Напишіть функцію, яка відображає порожній або заповнений квадрат з деякого символу. Функція приймає як параметри: довжину сторони квадрата, символ і змінну логічного типу

# def draw_square(size, symbol, filled):
#     if filled:
#         for i in range(size):
#             print(symbol * size)
#         pass
#     else:
#         print(symbol * size)
#         for i in range(size - 2):
#             print(symbol + " " * (size - 2) + symbol)
#         print(symbol * size)
#
# draw_square(7, "*", False)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 4

# Напишіть функцію, яка повертає мінімальне з п'яти чисел. Числа передаються як параметри

# def find_min_of_five(num1, num2, num3, num4, num5):
#     minimum = num1
#     if num2 < minimum:
#         minimum = num2
#     if num3 < minimum:
#         minimum = num3
#     if num4 < minimum:
#         minimum = num4
#     if num5 < minimum:
#         minimum = num5
#
#     return minimum
#
# print(find_min_of_five(5, 6, 7, 8, 9))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 5

# Напишіть функцію, яка рахує кількість цифр у числі. Число передається як параметр. З функції потрібно повернути отриману кількість цифр. Наприклад, якщо передали 3456, кількість цифр буде 4.

# def count_digits(num):
#     count = 0
#     while num > 0:
#         count += 1
#         num = num // 10
#
#     return count
#
# print(count_digits(3456))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 6

# Напишіть функцію, яка перевіряє чи є число паліндромом. Число передається як параметр. Якщо число паліндром, потрібно повернути з функції true, інакше false.

# def is_palindrome(num):
#     original_num = num
#     reversed_num = 0
#     while num > 0:
#         digit = num % 10
#         reversed_num = reversed_num * 10 + digit
#         num = num // 10
#
#     return original_num == reversed_num
# 
# print(is_palindrome(123321))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~