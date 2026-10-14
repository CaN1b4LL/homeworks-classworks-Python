# task 1

# Користувач вводить з клавіатури номер дня тижня (1-7). Необхідно вивести на екран назви дня тижня. Наприклад, якщо 1, то на екрані напис понеділок, 2 — вівторок тощо.

# num = int(input("Enter the day of the week number (1 - 7): "))
#
# if num == 1:
#     print("Monday")
# elif num == 2:
#     print("Tuesday")
# elif num == 3:
#     print("Wednesday")
# elif num == 4:
#     print("Thursday")
# elif num == 5:
#     print("Friday")
# elif num == 6:
#     print("Saturday")
# elif num == 7:
#     print("Sunday")
# else :
#     print("Error")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 2

# Користувач вводить із клавіатури номер місяця (1-12). Необхідно вивести на екран назву місяця. Наприклад, якщо 1, то на екрані напис січень, 2 — лютий тощо.

# month_number = int(input("Enter the month number (1-12): "))
#
# if month_number == 1:
#     print("January")
# elif month_number == 2:
#     print("February")
# elif month_number == 3:
#     print("March")
# elif month_number == 4:
#     print("April")
# elif month_number == 5:
#     print("May")
# elif month_number == 6:
#     print("June")
# elif month_number == 7:
#     print("July")
# elif month_number == 8:
#     print("August")
# elif month_number == 9:
#     print("September")
# elif month_number == 10:
#     print("October")
# elif month_number == 11:
#     print("November")
# elif month_number == 12:
#     print("December")
# else:
#     print("Error")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 3

# Користувач вводить суму покупки і свій вік. Програма обчислює знижку

# purchase_amount = float(input("Enter the purchase amount: "))
# age = int(input("Enter your age: "))
#
# if age < 18:
#     discount_percent = 10
# elif 18 <= age <= 60:
#     discount_percent = 5
# else:
#     discount_percent = 15
#
# final_amount = purchase_amount - (purchase_amount * discount_percent / 100)
#
# print(f"\nYour discount is: {discount_percent}%")
# print(f"Final amount to pay: {final_amount}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 4

# Користувач вводить оцінки з трьох предметів (від 1 до 5). Програма перевіряє, чи є серед них хоча б одна "двійка". Якщо так, виводиться повідомлення "Незадовільно". Якщо всі оцінки 4 і вище, виводиться "Відмінно".

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
#
# if num1 == 2 or num2 == 2 or num3 == 2:
#     print("Unsatisfactory")
# elif num1 >= 4 and num2 >= 4 and num3 >= 4:
#     print("Excellent")
# else:
#     print("Good")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 5

# Користувач вводить оцінки з чотирьох предметів (від 1 до 5). Програма перевіряє, чи може він бути допущений до іспиту.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# num4 = int(input("Enter fourth number: "))
#
# if num1 < 3 or num2 < 3 or num3 < 3 or num4 < 3:
#     print("the student is not allowed to take the exam")
# elif num1 >= 4 and num2 >= 4 and num3 >= 4 and num4 >= 4:
#     print("the student is admitted to the exam with honors")
# else :
#     print("the student is admitted to the exam")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 6

# Користувач вводить дані про свій автомобіль: вік і пробіг.

# age = int(input("Enter the age of the vehicle: "))
# run = int(input("Enter the vehicle's mileage: "))
#
# if age < 3 and run <= 30000:
#     print("The car is in excellent condition.")
# elif age < 10 and run <= 100000:
#     print("The car is in good condition.")
# else:
#     print("The car needs to be checked.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~