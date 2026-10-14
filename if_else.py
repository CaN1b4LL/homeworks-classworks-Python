# +, -, *, /, //, %, **
# example 1
# money = int(input("Enter the sum of money to withdraw ->"))
#
# bill_1000 = money // 1000
# money = money % 1000
# bill_500 = money // 500
# money = money % 500
# bill_200 = money // 200
# money %= 200
# bill_100 = money // 100
# money %= 100
# bill_50 = money // 50
# money %= 50
# bill_20 = money // 20
# money %= 20
# bill_10 = money // 10
# money %= 10
# bill_5 = money // 5
# money %= 5
# bill_2 = money // 2
# bill_1 = money % 2
#
# print(f"1000 = {bill_1000}")
# print(f"500  = {bill_500}")
# print(f"200  = {bill_200}")
# print(f"100  = {bill_100}")
# print(f"50   = {bill_50}")
# print(f"20   = {bill_20}")
# print(f"10   = {bill_10}")
# print(f"5    = {bill_5}")
# print(f"2    = {bill_2}")
# print(f"1    = {bill_1}")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# example 2
# birth_year = int(input("Enter your birth year->"))
# birth_month = int(input("Enter your birth month->"))
#
# total_birth_months = birth_year * 12 + birth_month
#
# current_year = 2026
# current_month = 6
#
# total_current_months = current_year * 12 + current_month
#
# total_months = total_current_months - total_birth_months
#
# years = total_months // 12
# months = total_months % 12
#
# print(f"You are {years} years and {months} months old")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# >     >
# <     <
# =     ==
# ≠     !=
# ≥     >=
# ≤     <=
# and, or, not

# a = 3
# b = 5
#
# # print(a > b) # False
# # print(a < b) # True
# # print(a >= b)# False
# # print(a <= b)# True
# # print(a == b)# False
# # print(a != b)# True
#
# x = int(input("Enter a number->"))
#
# # print(x >= a and x < b)
# print(x >= a or x < b)

# number = int(input("Enter a number->"))
#
# # if number < 0:
# #     print("Negative")
# # else:
# #     if number > 0:
# #         print("Positive")
# #     else:
# #         print("Zero")
#
#
# if number < 0:
#     print("Negative")
# elif number > 0:
#     print("Positive")
# else:
#     print("Zero")

#task 1
# num = int(input("Enter a number->"))
#
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")