# text = input("Enter some text: ")
#
# # pos = text.find(" ")
#
# # result = text[pos+1:]+" "+text[:pos]
#
# words = text.split()
# result = words[1]+" "+words[0]
# print(result)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import re
# text = "one, two:;.three!? four,five"
#
# # words = re.split("[!?;:,. ]+", text)
# words = re.findall("[a-zA-Z]+", text)
# print(words)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# lst = list()
# print(len(lst))

# lst = [3,5,8,4,1,7,6,9,2]
# print(lst)

# for i in range(len(lst)):
#     print(lst[i], end=" ")
# print()
#
# for item in lst:
#     print(item, end=" ")
# print()

# print(lst[2:7])

# copy = lst.copy()
# copy = lst[:]
# lst[0] = 100
# print(lst)
# print(copy)


# lst = [1,2,3,4,5]
# lst.append(100)
# lst.insert(5,100)
# lst.extend([6,7,8])
# print(lst.pop(6))
# lst.remove(3)
# lst.clear()
# print(lst)



# lst = [3,5,8,4,1,7,6,9,2]
# print(lst)
# # lst.reverse()
# lst.sort(reverse=True)
# print(lst)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 1

# lst = []
#
# for i in range(5):
#     num = int(input(f"Enter the [{i}] number: "))
#     lst.append(num)
# print(lst)
#
# sum_value = 0
#
# for item in lst:
#     sum_value += item
#
# print(f"Sum: {sum_value}")
# print(f"Average: {sum_value/len(lst)}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 2

# numbers = []
#
# print("Enter numbers one at a time. To end the entry, enter 0:")
#
# while True:
#     user_input = int(input("Enter a number: "))
#
#     if user_input == 0:
#         break
#
#     numbers.append(user_input)
#
# search_number = int(input("Enter a number to search for: "))
#
# count = 0
#
# for num in numbers:
#     if num == search_number:
#         count += 1
#
# print(f"Number {search_number} occurs in the list so many times: {count}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~RANDOM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import random
# lst = []
#
# for i in range(50):
#     lst.append(random.randint(-10,10))
# print(lst)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~