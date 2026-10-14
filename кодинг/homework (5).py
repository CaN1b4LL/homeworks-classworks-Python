# task 1

# Користувач вводить із клавіатури два числа (початок і кінець діапазону). Потрібно проаналізувати всі числа в цьому діапазоні за таким правилом: якщо число кратне 7, його треба виводити на екран.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# if num1 > num2:
#     num1, num2 = num2, num1
#
# counter = num1
#
# print(f"\nChecking numbers from {num1} to {num2} for multiplicity of 7:")
#
# while counter <= num2:
#     if counter % 7 == 0:
#         print(counter, end=" ")
#
#     counter += 1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 2

# Користувач вводить із клавіатури два числа (початок і кінець діапазону). Потрібно проаналізувати всі числа в цьому діапазоні.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# if num1 > num2:
#     num1, num2 = num2, num1
#
# print("1. All numbers in ascending order:")
# counter = num1
# while counter <= num2:
#     print(counter, end=" ")
#     counter += 1
# print("\n--------------------------------------------------------")
#
# print("2. All numbers in descending order:")
# counter = num2
# while counter >= num1:
#     print(counter, end=" ")
#     counter -= 1
# print("\n--------------------------------------------------------")
#
# print("3. All numbers multiple of 7:")
# counter = num1
# while counter <= num2:
#     if counter % 7 == 0:
#         print(counter, end=" ")
#     counter += 1
# print("\n--------------------------------------------------------")
#
# print("4. Counting numbers multiple of 5:")
# counter = num1
# count_of_fives = 0
# while counter <= num2:
#     if counter % 5 == 0:
#         count_of_fives += 1
#     counter += 1
#
# print(f"Total numbers multiple of 5 in this range: {count_of_fives}")
# print("--------------------------------------------------------")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 3

# Користувач вводить із клавіатури два числа (початок і кінець діапазону). Потрібно проаналізувати всі числа в цьому діапазоні. Виведення на екран має відбуватися за правилами, зазначеними нижче.
#
# Якщо число кратне 3 (ділиться на 3 без залишку) потрібно вивести слово "Fizz". Якщо число кратне 5 потрібно вивести слово "Buzz". Якщо число кратне 3 і 5 потрібно вивести "Fizz Buzz". Якщо число не кратне не 3 і 5 потрібно вивести саме число.

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
#
# if num1 > num2:
#     num1, num2 = num2, num1
#
# counter = num1
#
# print(f"\n--- FizzBuzz result for range {num1} to {num2} ---")
#
# while counter <= num2:
#     if counter % 3 == 0 and counter % 5 == 0:
#         print("Fizz Buzz", end=" ")
#     elif counter % 3 == 0:
#         print("Fizz", end=" ")
#     elif counter % 5 == 0:
#         print("Buzz", end=" ")
#     else:
#         print(counter, end=" ")
#     counter += 1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 4

# Користувач вводить два числа і крок (інтервал), з яким потрібно проходити по діапазону. Програма має показати числа від початку діапазону до кінця, збільшуючи кожне число на вказаний крок. Також програма повинна надавати вибір порядку виведення: у прямому або зворотному порядку.

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# step = int(input("Enter the step (interval): "))
#
# if num1 > num2:
#     num1, num2 = num2, num1
#
# choice = input("\nEnter your choice: \n1. Straight order (ascending)\n2. Reverse order (descending)\nYour choice (1 or 2): ")
#
# if choice == "1":
#     counter = num1
#     while counter <= num2:
#         print(counter, end=" ")
#         counter += step
# elif choice == "2":
#     counter = num2
#     while counter >= num1:
#         print(counter, end=" ")
#         counter -= step
# else:
#     print("Error: Invalid choice!")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 5

# Користувач вводить два числа, що представляють діапазон. Програма повинна пройти по діапазону і вивести добуток усіх чисел, які діляться на 4, але не діляться на 6. Якщо таких чисел немає, вивести відповідне повідомлення. Діапазон має автоматично нормалізуватися, якщо початок більший за кінець.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# if num1 > num2:
#     num1, num2 = num2, num1
#
# counter = num1
# product = 1
# found_count = 0
#
# while counter <= num2:
#     if counter % 4 == 0 and counter % 6 != 0:
#         product = product * counter
#         found_count = found_count + 1
#     counter += 1
# if found_count > 0:
#     print(f"The product of numbers is: {product}")
# else:
#     print("\nThere are no numbers in this range that match the criteria.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 6

# Користувач вводить два числа: число A і ступінь N, у який потрібно піднести число. Програма повинна обчислити A у степені N за допомогою циклу (без використання вбудованих функцій піднесення до степеня).

# A = int(input("Enter the number A: "))
# N = int(input("Enter the power N: "))
#
# result = 1
#
# steps = 0
#
# while steps < N:
#     result = result * A
#     steps = steps + 1
# else:
#     print("\nCalculation completed")
#
# print(f"The number {A} to the power of {N} is: {result}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~