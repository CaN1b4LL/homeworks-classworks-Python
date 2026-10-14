# task 1

# Користувач вводить із клавіатури два числа. Потрібно порахувати окремо суму парних, непарних і чисел, кратних 9 у вказаному діапазоні, а також середньоарифметичне кожної групи.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# even_sum = 0
# even_count = 0
#
# odd_sum = 0
# odd_count = 0
#
# m9_sum = 0
# m9_count = 0
#
# for num in range(num1, num2 + 1):
#
#     if num % 2 == 0:
#         even_sum = even_sum + num
#         even_count = even_count + 1
#     else:
#         odd_sum = odd_sum + num
#         odd_count = odd_count + 1
#
#     if num % 9 == 0:
#         m9_sum = m9_sum + num
#         m9_count = m9_count + 1
#
# print(f"\n--- Analysis for range {num1} to {num2} ---")
#
# if even_count > 0:
#     print(f"Even numbers - Sum: {even_sum}, Average: {even_sum / even_count}")
# else:
#     print("Even numbers - None found")
#
# if odd_count > 0:
#     print(f"Odd numbers - Sum: {odd_sum}, Average: {odd_sum / odd_count}")
# else:
#     print("Odd numbers - None found")
#
# if m9_count > 0:
#     print(f"Multiple of 9 - Sum: {m9_sum}, Average: {m9_sum / m9_count}")
# else:
#     print("Multiple of 9 - None found")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 2

# Користувач вводить з клавіатури довжину лінії та символ для заповнення лінії. Потрібно відобразити на екрані вертикальну лінію із введеного символу, зазначеної довжини.

# length = int(input("Enter the length of the line: "))
# symbol = input("Enter the symbol to fill the line: ")
#
# print("\nResult (Vertical line):")
#
# for i in range(length):
#     print(symbol)
# else:
#     print("\nLine drawing completed")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 3

# Користувач вводить із клавіатури числа. Якщо число більше нуля потрібно вивести напис "Number is positive", якщо менше нуля "Number is negative", якщо дорівнює нулю "Number is equal to zero". Коли користувач вводить число 7 програма припиняє свою роботу і виводить на екран напис "Good bye!".

# number = 0
#
# while number != 7:
#     number = int(input("Enter a number (enter 7 to exit): "))
#
#     if number == 7:
#         print("Goodbye")
#     elif number > 0:
#         print("Number is positive")
#     elif number < 0:
#         print("Number is negative")
#     else:
#         print("Number is equal to zero")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 4

# Користувач вводить із клавіатури числа. Програма повинна підраховувати суму, максимум і мінімум, введених чисел. Коли користувач вводить число 7 програма припиняє свою роботу і виводить на екран напис "Good bye!".

# number = 0
#
# total_sum = 0
#
# maximum = 0
# minimum = 0
#
# is_first = True
#
# while number != 7:
#     number = int(input("Enter a number (enter 7 to exit): "))
#
#     if number == 7:
#         print("Good bye!")
#     else:
#         total_sum = total_sum + number
#
#         if is_first == True:
#             maximum = number
#             minimum = number
#             is_first = False
#         else:
#             if number > maximum:
#                 maximum = number
#
#             if number < minimum:
#                 minimum = number
#
# print(f"\n--- Final Results ---")
# print(f"Sum of numbers: {total_sum}")
# print(f"Maximum number: {maximum}")
# print(f"Minimum number: {minimum}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 5

# Напишіть програму, яка перевіряє, чи є введене користувачем число простим.

# N = int(input("Enter an integer N: "))
#
# if N <= 1:
#     print("The number must be greater than 1")
#
# else:
#     is_prime = True
#
#     for divisor in range(2, N):
#         if N % divisor == 0:
#             is_prime = False
#
#     if is_prime == True:
#         print(f"The number {N} is prime")
#     else:
#         print(f"The number {N} is NOT prime")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 6

# Напишіть програму, яка перевіряє, чи є введене користувачем число членом послідовності Фібоначчі.

# N = int(input("Enter an integer N: "))
#
# f1 = 0
# f2 = 1
#
# if N == 0:
#     print(f"The number {N} belongs to the Fibonacci sequence")
#
# else:
#     while f2 < N:
#         f_next = f1 + f2
#
#         f1 = f2
#         f2 = f_next
#
#     if f2 == N:
#         print(f"The number {N} belongs to the Fibonacci sequence")
#     else:
#         print(f"The number {N} does NOT belong to the Fibonacci sequence")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~