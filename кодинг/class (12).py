# def gcd(a: int, b: int) -> int:
#     while b != 0:
#         a, b = b, a % b
#     return a
#
# print(gcd(48, 18))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def gcd(a: int, b: int) -> int:
#     if a < b:
#         limit = a
#     else:
#         limit = b
#
#     for i in range(limit, 0, -1):
#         if a % i == 0 and b % i == 0:
#             return i
#
#
# print(gcd(48, 18))  # Виведе 6

#~~~~~~~~~~~~~~~~~~~~ FILE ~~~~~~~~~~~~~~~~~~~~~~

# with open("test.txt","r") as file:
#      print(file.readlines())