# task 1

# line1 = input("enter first line: ")
# line2 = input("enter second line: ")
# line3 = input("enter third line: ")
#
# with open("data.txt", "w", encoding="utf-8") as file:
#     file.write(line1 + "\n")
#     file.write(line2 + "\n")
#     file.write(line3 + "\n")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 2

# try:
#     with open("data.txt", "r", encoding="utf-8") as file:
#         print("The file exists!")
#         lines = file.readlines()
#
#         for index, line in enumerate(lines, start=1):
#             if index % 2 == 0:
#                 print(line.strip())
#
# except FileNotFoundError:
#     print("The file data.txt does not exist!")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 3

# with open("data.txt", "r", encoding="utf-8") as source_file, \
#     open("filtered.txt", "w", encoding="utf-8") as target_file:
#
#     for line in source_file:
#         if "Python" in line:
#             target_file.write(line)
#
# print("Filtering complete! Lines with the word Python saved in filtered.txt")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 4

# filename = input("Enter file name: ")
#
# with open(filename, "r", encoding="utf-8") as file:
#     text = file.read()
#
# cleaned_text = ""
# for char in text:
#     if not char.isdigit():
#         cleaned_text += char
#
# with open("cleaned_text.txt", "w", encoding="utf-8") as file:
#     file.write(cleaned_text)
#
# print("The file has been successfully cleaned of numbers and saved to cleaned.txt!")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 6

# with open("data.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#
# reversed_lines = lines[::-1]
#
# with open("reversed.txt", "w", encoding="utf-8") as file:
#     file.writelines(reversed_lines)
#
# print("The lines have been successfully reversed into the reversed.txt file!")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~