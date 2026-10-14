#1

#money = int(input("enter the sum or money: "))

#bill_1000 = money // 1000
#money %= 1000
#bill_500 = money // 500
#money %= 500
#bill_200 = money // 200
#money %= 200
#bill_100 = money // 100
#money %= 100
#bill_50 = money // 50
#money %= 50
#bill_20 = money // 20
#money %= 20
#bill_10 = money // 10
#money %= 10
#bill_5 = money // 5
#money %= 5
#bill_2 = money // 2
#money %= 2

#print(f"1000 = {bill_1000}")
#print(f"500  = {bill_500}")
#print(f"200  = {bill_200}")
#print(f"100  = {bill_100}")
#print(f"50   = {bill_50}")
#print(f"20   = {bill_20}")
#print(f"10   = {bill_10}")
#print(f"5    = {bill_5}")
#print(f"2    = {bill_2}")


#2

#birth_year = int(input("Enter birth year: "))
#birth_month = int(input("Enter birth month: "))

#current_year = 2026
#current_month = 6

#year = current_year - birth_month
#month = current_month - birth_month

#years = total_months // 12
#months = total_months % 12

#print(f"Years: {years}")
#print(f"Months: {months}")





#2

# number = int(input("Enter a number: "))
#
# if number % 7 == 0:
#     print(number, "Number is multiple 7")
# else:
#     print(number, "Number is not multiple 7")

#3 - 4

# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
#
# if number1 < number2:
#     print("Minimum is:", number1)
# else:
#     print("Minimum is:", number2)
#
#
# #5
# nuber1 = int(input("Enter first number: "))
# nuber2 = int(input("Enter second number: "))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
birth_year = int(input("Enter your birth year->"))
birth_month = int(input("Enter your birth month->"))

total_birth_months = birth_year * 12 + birth_month

current_year = 2026
current_month = 6

total_current_months = current_year * 12 + current_month

total_months = total_current_months - total_birth_months

years = total_months // 12
months = total_months % 12

print(f"You are {years} years and {months} months old")


