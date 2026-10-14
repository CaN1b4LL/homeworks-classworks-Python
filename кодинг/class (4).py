# number = int(input("Enter a number: "))
#
# sum_div = 0
#
# for i in range(1, number//2+1):
#     if number % i == 0:
#         sum_div += i
#
# if sum_div == number:
#     print(f"The {number} is a perfect number.")
# else:
#     print(f"The {number} is not a perfect number.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# for number in range(1, 1000 + 1):
#     sum_div = 0
#
#     for i in range(1, number // 2 + 1):
#         if number % i == 0:
#             sum_div += i
#
#     if sum_div == number:
#         print(f"The number {number} is a perfect number.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~ str ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# text = "Hello world!"
#
# print(text[0])
# print(text[1])
# print(text[2])
# print(text[3])
# print(text[4])
#
# print(text[2:7])
# print(text[2:])
# print(text[:7])
# print(text[:])

# for i in range(0, len(text)):
#     print(text[i], end=" ")

# print(text[-1])

# for i in range(-1, -(len(text)+1), -1):
#     print(text[i], end=" ")

# for char in text:
#     print(char, end=" ")

# print(text[7:2:-1])

# print(text[::-1])

# print("Hello world".title())
# print("Hello world".upper())
# print("Hello world".lower())
# print("Hello world".swapcase())
# print("Hello world".capitalize())
# print("Hello world".casefold())

# print("Hello1".isalnum())

# print("Hello".ljust(10,'0'))
# print("Hello".rjust(10,'_'))
# print("Hello".center(10,'-'))
#
# print("5".rjust(5,'0'))
# print("5".zfill(5))

# print("Hello".startswith("He"))
# print("Hello".endswith("o"))

# print("  Hello  ".strip())
# print("  Hello  ".lstrip())
# print("  Hello  ".rstrip())

# print("Hello".index("lo"))
# print("Hello".find("lo"))

# print("Hello".count("l"))

# print("Hello world".replace("ll","l"))



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 1

# text = input("Enter some text: ")
#
# letters = 0
# digits = 0
# puncts = 0
#
# for i in text:
#     if i.isalpha():
#         letters += 1
#     if i.isdigit():
#         digits += 1
#     if i in ",.?!;:'-_":
#         puncts += 1
#
# print(f"letters: {letters}\n digits: {digits}\n puncts: {puncts}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 2

# text = input("Enter some text: ")
# search_char = input("Enter a search character: ")
#
# result = text.count(search_char)
#
# print(f"The character '{search_char}' occurs in the string so many times: {result}")


# text = input("Enter some text: ")
# search_char = input("Enter a search character: ")
#
# count = 0
#
# for char in text:
#     if char == search_char:
#         count += 1
#
# print(f"The character '{search_char}' occurs {count} times in the string")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 3

# text = input("Enter some text: ")
#
# reversed_string = ""
#
# for char in text:
#     reversed_string = char + reversed_string
#
# print(f"Turn result: {reversed_string}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 4 (через split) не для сегодняшнего урока тема обьяснения

# text = input("Enter some text: ")
# word = input("Enter the word to count: ")
#
# counter = 0
#
# for w in text.split():
#     if word == w:
#         counter += 1
#
# print(f"Counter = {counter}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# words = "one two three four five".split()
# print(words)
# line = " ".join(words)
# print(line)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

