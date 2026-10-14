# 1.1
# from turtledemo.penrose import start

# l = [1,2,3,4,5,6,7,8,9,10]
# lx10 = []
# for item in l:
#     lx10.append(item*10)
#
# print(lx10)

# 1.2

# l = [1,2,3,4,5,6,7,8,9,10]
# lx10 = [item * 10 for item in l]
# print(lx10)

# 1.3.1

# l = [1,2,3,4,5,6,7,8,9,10]

# lx10 = list(map(mult_10, l))
# print(lx10)

# 1.3.2

# l = [1,2,3,4,5,6,7,8,9,10]
#
# lx10 = list(map(lambda item: item*10, l))
# print(lx10)

# 2.1
# l = [1,2,3,4,5,6,7,8,9,10]
# l_even = []
# for item in l:
#     if item % 2 == 0:
#         l_even.append(item)
#
# print(l_even)

# 2.2
# l = [1,2,3,4,5,6,7,8,9,10]
# l_even = [item for item in l if item % 2 == 0]
#
# print(l_even)

# 2.3.1
# def is_even(number: int) -> bool:
#     return number % 2 == 0
#
# l = [1,2,3,4,5,6,7,8,9,10]
# l_even = list(filter(is_even, l))
# print(l_even)

# 2.3.2
# l = [1,2,3,4,5,6,7,8,9,10]
# l_even = list(filter(lambda item: item % 2 == 0, l))
# print(l_even)

# 3

# from random import randint as rand
# from functools import reduce
# lst = [rand(-10, 10)for _ in range(10)]
# print(lst)
#
# # s = 0
# #
# # for item in lst:
# #     s += item
#
# s = reduce(lambda a, b: a+b, lst)
# print(f"Sum = {s}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# start = 12
# end = 230
#
# for i in range(start, end):
#     print(i, end=" ")
#
# res = start + end
# print()
# print(res)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# buf = int(input("Enter the first number: "))
# if buf.isdigit():
#     a = int(buf)
# else:
#     a = 0
# buf = int(input("Enter the second number: "))
# if buf.isdigit():
#     b = int(buf)
# else:
#     b = 0
#
# if b != 0:
#     res = a / b
# else:
#     res = 0
#
# print(res)



# try:
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#
#     res = a / b
#
#     if res < 0:
#         raise ArithmeticError("res cannot be negative")
#
#     print(res)
# except ValueError as e:
#     print(f"ValueError: {e}")
# except ZeroDivisionError as e:
#     print(f"ZeroDivisionError: {e}")
# except Exception as e:
#     print(f"Exception: {e}")
# else:
#     print(res)
# finally:
#     print("Finally")

# def quot(a, b):
#     return a / b
#
#
# try:
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#
#     res = quot(a, b)
#
#     print(res)
# except Exception as e:
#     print(f"Main program. {e}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~