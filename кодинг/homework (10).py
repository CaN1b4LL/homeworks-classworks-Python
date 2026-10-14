# task 1

# Користувач з клавіатури вводить список цілих чисел. Необхідно визначити кількість елементів у списку, які більші за попередній елемент. Результат вивести на екран.

# # ВВЕДЕННЯ ЧИСЕЛ ПО ЧЕРЗІ
# numbers = []
#
# while True:
#     user_input = input("Enter an integer (or just press Enter to finish): ")
#     if user_input == "":
#         break
#     numbers.append(int(user_input))
#
# print(f"Your list of numbers: {numbers}")
# print("-" * 50)
#
# # ПІДРАХУНОК ЕЛЕМЕНТІВ, ЩО БІЛЬШІ ЗА ПОПЕРЕДНІЙ
#
# count = 0
#
# for i in range (1, len(numbers)):
#     current_element = numbers[i]
#     previous_element = numbers[i - 1]
#
#     if current_element > previous_element:
#         count += 1
#
# print(f"Number of items greater than previous: {count}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 2

# Користувач вводить список цілих чисел. Необхідно вивести тільки ті елементи, які зустрічаються у списку рівно один раз, зберігаючи порядок їхньої появи.

# # ВВЕДЕННЯ СПИСКУ ЧИСЕЛ
# numbers = []
#
# while True:
#     user_input = input("Enter an integer (or just press Enter to finish): ")
#     if user_input == "":
#         break
#     numbers.append(int(user_input))
#
# print(f"Initial list: {numbers}")
# # ПОШУК УНІКАЛЬНИХ ЕЛЕМЕНТІВ
# unique_numbers = []
#
# for n in numbers:
#     if numbers.count(n) == 1:
#         unique_numbers.append(n)
#
# print(f"Elements that occur exactly once: {unique_numbers}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 3

# Користувач з клавіатури вводить список чисел. Необхідно знайти у списку найдовшу послідовність елементів, що зростають, і вивести її довжину та самі елементи.

# # ВВЕДЕННЯ СПИСКУ ЧИСЕЛ
# numbers = []
#
# while True:
#     user_input = input("Enter a number (or just press Enter to finish): ")
#     if user_input == "":
#         break
#     numbers.append(int(user_input))
#
# print(f"Initial list: {numbers}")
#
# # ПОШУК НАЙДОВШОЇ ПОСЛІДОВНОСТІ
#
# if len(numbers) > 0:
#     current_seq = [numbers[0]]
#     max_seq = [numbers[0]]
#
#     for i in range(1, len(numbers)):
#         if numbers[i] > numbers[i - 1]:
#             current_seq.append(numbers[i])
#         else:
#             if len(current_seq) > len(max_seq):
#                 max_seq = list(current_seq)
#             current_seq = [numbers[i]]
#
#     if len(current_seq) > len(max_seq):
#         max_seq = list(current_seq)
#
#     print(f"Sequence length: {len(max_seq)}")
#     print(f"Sequence: {max_seq}")
# else:
#     print("The list is empty.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 4

# Користувач із клавіатури вводить список цілих чисел. Необхідно реалізувати циклічний зсув списку вправо на N позицій. Результат вивести на екран.

# numbers = []
#
# while True:
#     user_input = input("Enter a number (or just press Enter to finish): ")
#     if user_input == "":
#         break
#     numbers.append(int(user_input))
#
# print(f"Initial list: {numbers}")
# N = int(input("How many positions to shift?: "))
#
# shifted_list = numbers[-N:] + numbers[:-N]
#
# print(f"Shifted list: {shifted_list}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 5

# Два списки цілих заповнюються випадковими числами.

# import random
#
# list1 = []
# list2 = []
#
# for i in range(5):
#     list1.append(random.randint(1,10))
#     list2.append(random.randint(1,10))
#
# print(f"list1: {list1}")
# print(f"list2: {list2}")
# print("-" * 70)
#
# # 1
# list3_all = list1 + list2
# print(f"Elements of both lists: {list3_all}")
#
# # 2
# list3_no_duplicates = []
#
# for i in range(len(list3_all)):
#     if list3_all[i] not in list3_no_duplicates:
#         list3_no_duplicates.append(list3_all[i])
#
# print(f"elements of both lists without repetitions: {list3_no_duplicates}")
#
# # 3
# common_elements = []
#
# for i in range(len(list1)):
#     if list1[i] in list2 and list1[i] not in common_elements:
#         common_elements.append(list1[i])
#
# print(f"elements common to two lists: {common_elements}")
#
# # 4
# unique_elements = []
#
# for x in list1:
#     if x not in list2 and x not in unique_elements:
#         unique_elements.append(x)
#
# for x in list2:
#     if x not in list1 and x not in unique_elements:
#         unique_elements.append(x)
#
# print(f"contains only unique elements of each list: {unique_elements}")
#
# # 5
# min1 = list1[0]
# max1 = list1[0]
# min2 = list2[0]
# max2 = list2[0]
#
# for x in list1:
#     if x < min1:
#         min1 = x
#     if x > max1:
#         max1 = x
#
# for x in list2:
#     if x < min2:
#         min2 = x
#     if x > max2:
#         max2 = x
#
# min_max_list = [min1, max1, min2, max2]
# print(f"Min and max elements of each list: {min_max_list}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 6

# Користувач вводить список цілих чисел. Необхідно відсортувати список так, щоб числа чергувалися: спочатку найменше, потім найбільше, потім друге за величиною, друге за мінімальністю тощо.

# numbers = []
#
# while True:
#     user_input = input("Enter a number (or just press Enter to finish): ")
#     if user_input == "":
#         break
#     numbers.append(int(user_input))
#
# n = len(numbers)
#
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#
# print(f"Sorted list: {numbers}")
#
# result = []
# left = 0
# right = len(numbers) - 1
#
# while left <= right:
#     if left == right:
#         result.append(numbers[left])
#         break
#
#     result.append(numbers[left])
#     result.append(numbers[right])
#
#     left += 1
#     right -= 1
#
# print(f"Expected result: {result}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~