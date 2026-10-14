# task 1

#Необхідно знайти суму чисел, добуток чисел.

#a = int(input("Enter the first number->"))
#b = int(input("Enter the second number->"))

#sum_result = a + b
#prod_result = a * b

#print("Sum =", sum_result)
#print("Product =", prod_result)

#task 2

# Напишіть програму, що обчислює площу ромба. Користувач з клавіатури вводить довжину двох його діагоналей.

#a1 = float(input("Enter the length of the first diagonal: "))
#a2 = float(input("Enter the length of the second diagonal: "))

#area = (a1 * a2) / 2

#print("The area of a rhombus is equal to:", area)

#task 3

# Перше число - зарплата за місяць, друге число — сума місячного платежу за кредитом у банку, третє число — заборгованість за комунальні послуги. Необхідно вивести на екран суму, яка залишиться у користувача після всіх виплат.

#salary = float(input("Enter your monthly salary: "))
#credit = float(input("Enter your monthly credit payment: "))
#utilities = float(input("Enter your utility debt: "))

#balance = salary - credit - utilities

#print("The amount left after all payments is: ", balance)

#task 4

# Користувач вводить відстань у кілометрах, витрату палива на 100 кілометрів і ціну за літр бензину.

#distance = float(input("Enter the trip distance in kilometers: "))
#consumption = float(input("Enter the fuel consumption per 100 km: "))
#price = float(input("Enter the fuel price per liter: "))

#total_cost = (distance / 100) * consumption * price

#print("The total cost of the trip is:", total_cost)

#task 5

#Напишіть програму, яка розраховує суму чайових (15% від загальної суми) і загальну суму, включаючи чайові. Потім програма повинна розділити загальну суму з чайовими на кількість осіб і вивести, скільки кожна людина має заплатити.

#total_bill = float(input("Enter the total bill amount: "))
#people_count = int(input("Enter the number of people: "))

#tip_amount = total_bill * 0.15
#grand_total = total_bill + tip_amount

#amount_per_person = grand_total / people_count

#print("Tip amount (15%):", tip_amount)
#print("Total bill including tips:", grand_total)
#print("Each person must pay:", amount_per_person)

#task 6

#Користувач вводить вартість оренди автомобіля за день, кількість днів оренди та суму застави, яку потрібно внести. Напишіть програму, яка розраховує загальну вартість оренди (з урахуванням застави) і виводить суму, яку необхідно заплатити користувачеві після повернення автомобіля (припускаючи, що застава повертається повністю). Програма повинна також розділити підсумкову суму оренди (без застави) на кількість днів і вивести вартість оренди за один день.

#daily_rate = float(input("Enter the rental cost per day: "))
#rental_days = int(input("Enter the number of rental days: "))
#deposit = float(input("Enter the security deposit amount: "))

#total_with_deposit = (daily_rate * rental_days) + deposit

#actual_cost = total_with_deposit - deposit

#calculated_daily_rate = actual_cost / rental_days

#print("Total upfront payment (with deposit): ", total_with_deposit)
#print("Final cost after deposit return: ", actual_cost)
#print("Calculated cost per one day: ", calculated_daily_rate)