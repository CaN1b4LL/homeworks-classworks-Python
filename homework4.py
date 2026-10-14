# task 1

# Користувач вводить з клавіатури три числа. Залежно від вибору користувача програма виводить на екран суму трьох чисел або добуток трьох чисел.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
#
# operation = input("What to do? Enter + for sum or * for product: ")
#
# if operation == "+":
#     result = num1 + num2 + num3
#     print("Sum is:", result)
# elif operation == "*":
#     result = num1 * num2 * num3
#     print("Product is:", result)
# else:
#     print("Error: Unknown operation!")

# task 2

# Користувач вводить з клавіатури три числа. Залежно від вибору користувача програма виводить на екран максимум із трьох, мінімум із трьох або середньоарифметичне трьох чисел.

# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# number3 = int(input("Enter third number: "))
#
# operation = input("What to find? Enter 'max', 'min' or 'avg': ")
#
# if operation == "max":
#     result = max(number1, number2, number3)
#     print("Maximum is:", result)
#
# elif operation == "min":
#     result = min(number1, number2, number3)
#     print("Minimum is:", result)
#
# elif operation == "avg":
#     result = (number1 + number2 + number3) / 3
#     print("Average is:", result)
#
# else:
#     print("Error: Unknown operation!")

# task 3

# Користувач вводить число, що представляє оцінку за шкалою від 1 до 5. Програма повинна вивести текстову інтерпретацію оцінки: 1. Дуже погано 2. Погано 3. Задовільно 4. Добре 5. Відмінно

# number = int(input("Enter a number from 1 to 5: "))
#
# if number == 1:
#     print("Very bad")
# elif number == 2:
#     print("Badly")
# elif number == 3:
#     print("Satisfactorily")
# elif number == 4:
#     print("good")
# elif number == 5:
#     print("Perfectly")
# else :
#     print("Error")

# task 4

# Користувач вводить з клавіатури кількість метрів. Програма має запропонувати кілька варіантів перекладу і, залежно від вибору користувача, перевести метри в одну або кілька одиниць виміру.

# number = float(input("Enter the number of meters: "))
#
# operation = input("choose one of the options: \n1. Convert to one of the units of your choice: miles, inches, or yards.\n2. Convert to all three units at once (miles, inches, and yards) and display the results for each.\n3. Convert to kilometers and centimeters. \nChoose an option: ")
#
# if operation == "1":
#     operation = input("choose one of the options: \n1. miles \n2. inches\n3. yards\nChoose an option: ")
#     if operation == "1":
#         result = number * 0.000621371
#         print(f"miles: {result}")
#     elif operation == "2":
#         result = number * 39.37
#         print(f"inches: {result}")
#     elif operation == "3":
#         result = number * 1.09361
#         print(f"yards: {result}")
#     else :
#         print("Error")
# elif operation == "2":
#     result1 = number * 0.000621371
#     result2 = number * 39.37
#     result3 = number * 1.09361
#     print(f"result: \nmiles: {result1}\ninches: {result2}\nyards: {result3}")
# elif operation == "3":
#     result1 = number / 1000
#     result2 = number * 100
#     print(f"result: \nkilometers: {result1}\ncentimeters: {result2}")
# else:
#     print("Error")

# task 5

# Користувач вводить два числа і вибирає операцію (додавання, віднімання, множення, ділення, знаходження залишку, піднесення до степеня). Програма повинна виконати вибрану операцію і вивести результат.

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
#
# op = input("Enter operation (+, -, *, /, %, **): ")
#
# if op == "+":
#     result = num1 + num2
#     print("Result:", result)
# elif op == "-":
#     result = num1 - num2
#     print("Result:", result)
# elif op == "*":
#     result = num1 * num2
#     print("Result:", result)
# elif op == "/":
#     result = num1 / num2
#     print("Result:", result)
# elif op == "%":
#     result = num1 % num2
#     print("Result:", result)
# elif op == "**":
#     result = num1 ** num2
#     print("Result:", result)
# else:
#     print("Error: Unknown operation!")

# task 6

# Користувач вводить тризначне число. Програма повинна визначити, чи всі цифри числа однакові. Якщо всі цифри однакові, вивести «Всі цифри однакові», інакше — «Цифри різні».

# num = int(input("Enter a three-digit number: "))
#
# d1 = num // 100
# d2 = (num // 10) % 10
# d3 = num % 10
#
# if d1 == d2 and d2 == d3:
#     print("All numbers are the same")
# else:
#     print("The numbers are different")