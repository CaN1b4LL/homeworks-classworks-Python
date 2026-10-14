# number = int(input("Enter a number: "))
#
# counter = 0
#
# while number > 0:
#     counter += 1
#     number //= 10
#
# print(f"There are {counter} counter in the number")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# number = int(input("Enter a number: "))
#
# counter = 0
#
# while number > 0:
#     counter += number % 10
#     number //= 10
#
# print(f"Result = '{counter}'")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# number = 1
#
# while number != 0:
#     number = int(input("Enter a number (0 to exit): "))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# number = 1
# counter = 0
# while number != 0:
#     number = int(input("Enter a number (0 to exit): "))
#     counter += 1
#
# print(f"{counter}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~ for ~~~~~~~~~~~~~~~~~~~~~~~~~~

# for i in range(10):
#     print("Hello World!!!")

# for i in range(10):
#     print(i, end=" ")

# for i in range(5, 20):
#     print(i, end=" ")

# for i in range(1, 10, 2):
#     print(i, end=" ")

# for i in range(30, 10, -1):
#     print(i, end=" ")

# a = 23
#
# for i in range(a%10, 20):
#     print(i, end=" ")

# for i in range(1, 10):
#     print(i/10, end=" ")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 1

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# for i in range(num1, num2):
#         print(i, end=" ")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 2

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# for i in range(num1, num2):
#     if i % 2 != 0:
#         print(i, end=" ")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 3

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# for i in range(num1, num2, -1):
#     if i % 2 == 0:
#         print(i, end=" ")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 4

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# if num1 > num2:
#     num1, num2 = num2, num1
#
# number = input("\n1. display in ascending order.\n2. displayed in descending order.\nEnter an option:")
#
# if number == "1":
#     for i in range(num1, num2):
#         print(i, end=" ")
# elif number == "2":
#     for i in range(num2, num1, -1):
#         print(i, end=" ")
# else:
#     print("Error")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 5

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# if num1 > num2:
#     num1, num2 = num2, num1
#
# for num in range(num1, num2 + 1):
#     if num % 2 != 0:
#         print(num, end=" ")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 1/2

# мой вариант

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# if num1 > num2:
#     num1, num2 = num2, num1
#
# total_sum = 0
# count = 0
#
# for num in range(num1, num2 + 1):
#     total_sum = total_sum + num
#     count = count + 1
#
# average = total_sum / count
#
# print(f"\nResults for range from {num1} to {num2}:")
# print(f"Sum of numbers: {total_sum}")
# print(f"Average: {average}")


# вариант учителя (с учетом проверки на ошибку при делении (т.е. if counter > 0))


# start = int(input("Enter the start of the range->"))
# end = int(input("Enter the end of the range->"))
#
# if start > end:
#     start, end = end, start
#
# sum_value = 0
# counter = 0
#
# for i in range(start, end):
#     sum_value += i
#     counter += 1
#
# print(f"Sum = {sum_value}")
# if counter > 0:
#     print(f"Average = {sum_value/counter}")
# else:
#     print("Cannot calculate average, counter is zero")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~