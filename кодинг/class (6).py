# task 1

# import random
#
# numbers = []
# for i in range(15):
#     numbers.append(random.randint(-50, 50))
#
# print(f"Generated list: {numbers}")
#
# #СТВОРЕННЯ ЗМІННИХ ДЛЯ ПЕРШИХ ЧОТИРЬОХ ПУНКТІВ
# sum_negatives = 0
# sum_evens = 0
# sum_odds = 0
# mult_by_index_3 = 1
#
# # ЦИКЛ ДЛЯ ОБРОБКИ ПЕРШИХ ЧОТИРЬОХ ПУНКТІВ
# for i in range(len(numbers)):
#     n = numbers[i]
# #[ПУНКТ 4] Перевірка індексів кратних 3
#     if i > 0 and i % 3 == 0:
#         mult_by_index_3 *= n
#
# # [ПУНКТ 2 та 3] Перевірка на парність
#     if n % 2 == 0:
#         sum_evens += n
#     else:
#         sum_odds += n
# # [ПУНКТ 1] Перевірка на від'ємне число
#     if n < 0:
#         sum_negatives += n
#
# print(f"Sum of even numbers: {sum_evens}")
# print(f"The sum of odd numbers: {sum_odds}")
# print(f"Sum of negatives: {sum_negatives}")
# print(f"Product of elements with indices multiple of 3: {mult_by_index_3}")
#
# # [ПУНКТ 5]: ДОБУТОК ЕЛЕМЕНТІВ МІЖ МІНІМАЛЬНИМ І МАКСИМАЛЬНИМ
# min_idx = 0
# max_idx = 0
#
# for i in range(len(numbers)):
#     if numbers[i] < numbers[min_idx]:
#         min_idx = i
#     if numbers[i] > numbers[max_idx]:
#         max_idx = i
#
# if min_idx < max_idx:
#     start_idx = min_idx
#     end_idx = max_idx
# else:
#     start_idx = max_idx
#     end_idx = min_idx
#
# prod_between = 1
# for j in range(start_idx + 1, end_idx):
#     prod_between *= numbers[j]
#
# # [ПУНКТ 6]: СУМА ЕЛЕМЕНТІВ МІЖ ПЕРШИМ І ОСТАННІМ ДОДАТНИМИ
# first_pos_idx = -1
# last_pos_idx = -1
#
# for i in range(len(numbers)):
#     if numbers[i] > 0:
#         if first_pos_idx == -1:
#             first_pos_idx = i
#         last_pos_idx = i
#
# sum_between_pos = 0
# if first_pos_idx != -1 and last_pos_idx != -1 and first_pos_idx != last_pos_idx:
#     for j in range(first_pos_idx + 1, last_pos_idx):
#         sum_between_pos += numbers[j]
#
# print(f"Product between min and max: {prod_between}")
# print(f"Sum between first and last positive: {sum_between_pos}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 2

# import random
#
# numbers = []
# for i in range(15):
#     numbers.append(random.randint(-50,50))
#
# print(f"Initial array: {numbers}")
# print("-" * 80)
#
# # task 2.1 Створити список цілих, що містить тільки парні числа
#
# even_list = []
#
# for n in numbers:
#     if n % 2 == 0:
#         even_list.append(n)
#
# print(f"1. List with only even numbers: {even_list}")
#
# # task 2.2 Створити список цілих, що містить тільки непарні числа
#
# odd_list = []
#
# for n in numbers:
#     if n % 2 != 0:
#         odd_list.append(n)
#
# print(f"2. List with only odd numbers: {odd_list}")
#
# # task 2.3 Створити список цілих, що містить тільки від'ємні числа
#
# negative_list = []
#
# for n in numbers:
#     if n < 0:
#         negative_list.append(n)
#
# print(f"3. List with only negative numbers: {negative_list}")
#
# # task 2.4 Створити список цілих, що містить тільки додатні числа
#
# positive_list = []
#
# for n in numbers:
#     if n > 0:
#         positive_list.append(n)
#
# print(f"4. List with only positive numbers: {positive_list}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 3

# # 1. ВВЕДЕННЯ РЯДКІВ З КЛАВІАТУРИ
# strings = []
#
# while True:
#     text = input("Type the line (or just press Enter to finish):")
#     if text == "":
#         break
#     strings.append(text)
#
# print(f"Your list of lines: {strings}")
# # 2. ПОШУК НАЙКОРОТШОГО РЯДКА
# if len(strings) > 0:
#     shortest = strings[0]
#
#     for s in strings:
#         if len(s) < len(shortest):
#             shortest = s
#
#     print(f"The shortest line in the list: {shortest}")
# else:
#     print("The list is empty, you have not entered anything!")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 4

# # 1. ВВЕДЕННЯ СПИСКУ РЯДКІВ
#
# strings = []
#
# while True:
#     text = input("Enter the string (or just Enter to finish): ")
#     if text == "":
#         break
#     strings.append(text)
#
# print(f"Initial string list: {strings}")
# print("-" * 50)
#
# # 2. ВВЕДЕННЯ ЗАДАНОЇ ЛІТЕРИ
#
# search_letter = input("Enter the letter by which we will search for lines:")
#
# # 3. СТВОРЕННЯ НОВОГО СПИСКУ
#
# filtered_strings = []
#
# for s in strings:
#     if len(s) > 0 and s[0] == search_letter:
#         filtered_strings.append(s)
#
# print(f"New list (strings starting with '{search_letter}'): {filtered_strings}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~