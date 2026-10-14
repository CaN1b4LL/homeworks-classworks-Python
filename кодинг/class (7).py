# from random import randint as rand
#
# lst = [0] * 10
# print(lst)
# # i = 0
# # while i < len(lst):
# #     lst[i] = rand(0, 9)
# #     if lst[i] not in lst[:i]:
# #         i += 1
#
# i = 1
# while i < len(lst):
#     pos = rand(0, 9)
#     if lst[pos] == 0:
#         lst[pos] = i
#         i += 1
# print(lst)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# lst = [[0]*3]*4
# # print(lst)
#
# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         lst[i][j] = rand(0, 100)
#
#
# for row in lst:
#     for item in row:
#         print(item, end="\t")
#     print()
#
#
# max_val = lst[0][0]
#
# for row in lst:
#     for item in row:
#         if max_val < item:
#             max_val = item
#
# print(f"Max = {max_val}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def print_hello():
#     print("Hello World!!!")
#
# # print_hello()
#
# def greeting(name):
#     print(f"Hello, {name}!")
#
# greeting("Vasya")
# greeting("Petya")


# def print_hello(n=1):
#     for i in range(n):
#         print("Hello world!!!")
#
# print_hello(5)
# print()
# print_hello(3)
# print()
# print_hello()


# def my_sum(a, b):
#     return a + b
#
# result = my_sum(12, 23)
#
# print(result)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~task~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 1

# def show_quote():
#     print(
#         "\"Don't let the noise of others' opinions\n    drown out your own inner voice.\"\n        \033[33mSteve Jobs\033[0m")
# show_quote()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 2

# def show_odd_numbers(start, end):
#     for i in range(start, end):
#         if i % 2 != 0:
#             print(i, end=" ")
#     print()
#
# show_odd_numbers(1, 10)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 3

# def draw_line(length, direction, symbol):
#     if direction == "horizontal":
#         print(symbol * length)
#     elif direction == "vertical":
#         for i in range(length):
#             print(symbol)
#
# print("Horizontal line:")
# draw_line(10, "horizontal", "*")
#
# print("\nVertical line:")
# draw_line(5, "vertical", "|")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 4

# def find_max_of_four(num1, num2, num3, num4):
#     maximum = num1
#
#     if num2 > maximum:
#         maximum = num2
#     if num3 > maximum:
#         maximum = num3
#     if num4 > maximum:
#         maximum = num4
#
#     return maximum
#
# final_answer = find_max_of_four(8, 29, 42, 11)
# print(final_answer)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 5

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#
#     return True
#
# print(is_prime(7))
# print(is_prime(10))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~