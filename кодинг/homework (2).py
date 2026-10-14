# task 1

# Користувач вводить з клавіатури кількість метрів. Потрібно вивести результат переведення метрів у сантиметри, дециметри, міліметри, милі.

# meter = int(input("Enter the number in meters: "))
#
# centimeter = meter * 100
# decimeters = meter * 10
# millimeter = meter * 1000
# miles = meter * 0.000621371
#
# print(f"centimeter = {centimeter}\ndecimeters = {decimeters}\nmillimeter = {millimeter}\nmiles = {miles}")

# task 2

# Напишіть програму, що обчислює площу трикутника. Користувач з клавіатури вводить розмір основи трикутника і розмір висоти.

# base = float(input("Enter the size of the base of the triangle: "))
# height = float(input("Enter the height of the triangle: "))
#
# area = (base * height) / 2
#
# print(f"The area of the triangle is {area}")

# task 3

# Користувач вводить з клавіатури три цифри. Необхідно створити число, що містить ці цифри. Наприклад, якщо з клавіатури введено 1, 5, 7, тоді потрібно сформувати число 157.

# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
#
# result = number1 * 100 + number2 * 10 + number3
#
# print(f"result: {result}")

# task 4

# Користувач вводить із клавіатури число, що складається з чотирьох цифр. Потрібно знайти добуток цифр. Наприклад, якщо з клавіатури введено 1324, тоді результат добутку 1*3*2*4 = 24.

# number = int(input("Enter a number: "))
#
# num1 = number // 1000 % 10
# num2 = number // 100 % 10
# num3 = number // 10 % 10
# num4 = number % 10
#
# result = num1 * num2 * num3 * num4
#
# print(f"result is {result}")

# task 5

# Користувач з клавіатури вводить чотиризначне число. Необхідно перевернути число і відобразити результат. Наприклад, якщо введено 4512, результат 2154.

# number = int(input("Enter a number: "))
#
# num1 = number // 1000 % 10
# num2 = number // 100 % 10
# num3 = number // 10 % 10
# num4 = number % 10
#
# reversed_num = num4 * 1000 + num3 * 100 + num2 * 10 + num1
#
# print(f"Reversed number: {reversed_num}")

# task 6

# Користувач вводить два тризначні числа. Напишіть програму, яка:
# Об'єднує їх таким чином, щоб перша цифра взята з першого числа, друга цифра – з другого числа, третя цифра – знову з першого числа, і так далі.

# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
#
# a1 = number1 // 100 % 10
# a2 = number1 // 10 % 10
# a3 = number1 % 10
#
# b1 = number2 // 100 % 10
# b2 = number2 // 10 % 10
# b3 = number2 % 10
#
# total_sum = (a1 * 100000) + (b1 * 10000) + (a2 * 1000) + (b2 * 100) + (a3 * 10) + b3
#
# print(f"result is: {total_sum}")