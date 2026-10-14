# with open("data.txt","r") as sours_file:
#     content = sours_file.read()
#
# with open("backup.txt","w") as target_file:
#     target_file.write(content)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 2

# with open("data.txt","r") as file:
#     lines = file.readlines()
#     count = len(lines)
#
# print(f"Кількість рядків у файлі: {count}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 5

# import re
#
# with open("data.txt","r", encoding="utf-8") as file:
#     content = file.readlines()
#
# lines_count = len(content)
#
# words_count = 0
# chars_count = 0
#
# for line in content:
#     chars_count += len(line)
#     words_count += len(re.findall(r"\w+", line))
#
# report = f"Кількість рядків: {lines_count}\n" \
#          f"Кількість слів: {words_count}\n" \
#          f"Кількість символів: {chars_count}\n"
#
# with open("summary.txt","w", encoding="utf-8") as file:
#     file.write(report)
#
# print("Звіт створено у файлі summary.txt")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 6

# alphabet = "abcdefghijklmnopqrstuvwxyz"
#
# with open("data.txt","r", encoding="utf-8") as file:
#     text = file.read()
#
# encrypted_text = ""
#
# for char in text:
#     lower_char = char.lower()
#
#     if lower_char in alphabet:
#         index = alphabet.index(lower_char)
#         new_char = alphabet[(index + 1) % len(alphabet)]
#
#         if char.isupper():
#             encrypted_text += new_char.upper()
#         else:
#             encrypted_text += new_char
#     else:
#         encrypted_text += char
#
# with open("encrypted.txt","w", encoding="utf-8") as file:
#     file.write(encrypted_text)
#
# print("Текст зашифровано у файл encrypted.txt")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~