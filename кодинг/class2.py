# num = int(input("Enter a number(1 - 10): "))
#
# if num == 1:
#     print("I")
# elif num == 2:
#     print("II")
# elif num == 3:
#     print("III")
# elif num == 4:
#     print("IV")
# elif num == 5:
#     print("v")
# elif num == 6:
#     print("VI")
# elif num == 7:
#     print("VII")
# elif num == 8:
#     print("VIII")
# elif num == 9:
#     print("IX")
# elif num == 10:
#     print("X")
# else:
#     print("Error")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# num = int(input("Enter a number(1 - 10): "))
#
# match num:
#     case 1:
#         print("I")
#     case 2:
#         print("II")
#     case 3:
#         print("III")
#     case 4:
#         print("IV")
#     case 5:
#         print("v")
#     case 6:
#         print("VI")
#     case 7:
#         print("VII")
#     case 8:
#         print("VIII")
#     case 9:
#         print("IX")
#     case 10:
#         print("X")
#     case val if val > 10:
#             print("A lot")
#     case _:
#         print("Error")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# a = int(input("enter the first number: "))
# b = int(input("enter the second number: "))
#
# max_value = a if a > b else b
#
# # if a > b:
# #     max_value = a
# # else :
# #     max_value = b
#
# print(f"Max = {max_value}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# counter = 0
# while counter < 10:
#     print("Hello World")
#     # counter = counter + 1
#     counter += 1

# counter = 0
# while counter < 10:
#     counter += 1
#     print(counter, end=", ")
# else:
#     print("End of the loop")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# num = int(input("Enter a number: "))
#
# counter = 0
# while counter < num:
#     print(counter, end=" ")
#     counter += 1
# else:
#     print("End of the loop")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 1

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
#
# counter = num1
# while counter < num2:
#     print(counter, end=" ")
#     counter += 1
# else:
#     print("End of the loop")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 2

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
#
# counter = num1 + (1 - num1 % 2)
#
# while counter <= num2:
#     print(counter, end=" ")
#     counter += 2
# else:
#     print("End of the loop")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 3

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
#
# counter = num1 + (num1 % 2)
#
# while counter <= num2:
#     print(counter, end=" ")
#     counter += 2
# else:
#     print("End of the loop")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 4

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
#
# choice = input("Enter the operation: \n1. In ascending order\n2. in descending order\nEnter your choice: ")
#
# if choice == "1":
#     counter = num1
#     while counter <= num2:
#         print(counter, end=" ")
#         counter += 1
# elif choice == "2":
#     counter = num2
#     while counter >= num1:
#         print(counter, end=" ")
#         counter -= 1
# else:
#     print("\nError")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 5

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
#
# if num1 > num2:
#     num1, num2 = num2, num1
#
# counter = num1 + (1 - num1 % 2)
#
# while counter <= num2:
#     print(counter, end=" ")
#     counter += 2
# else:
#     print("End of the loop")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~