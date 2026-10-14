# number = float(input("Enter the diameter of the circle: "))
#
# op = input("Choose an option:\n1. Circle area\n2. perimeter of a circle\nEnter your choice: ")
#
# r = number / 2
# pi = 3.14
#
# if op == "1":
#     area = pi * (r ** 2)
#     print(f"area is: {area}")
# elif op == "2":
#     perimeter = 2 * pi * r
#     print(f"perimeter is: {perimeter}")
# else:
#     print("Error")

# 3

# cost = int(input("cost of one game console: "))
# number = int(input("Enter the quantity: "))
# discount = int(input("Enter the discount: "))
#
# op = input("Enter the operation:\n1. the total amount of the order\n2. the cost of one set-top box\nEnter the choice: ")
#
# total_full_price = cost * number
# total_discounted_price = total_full_price - (total_full_price * discount / 100)
#
# single_discounted_price = cost - (cost * discount / 100)
#
# if op == "1":
#     print(f"The total amount of the order is {total_discounted_price}")
# elif op == "2":
#     print(f"The cost of one set-top box is {single_discounted_price}")

# 4

# gb_size = float(input("Enter the file size in Gigabytes (GB): "))
# speed = float(input("Enter your internet speed in bits per second (bps): "))
#
# file_bits = gb_size * 1024 * 1024 * 1024 * 8
#
# total_seconds = file_bits / speed
#
# op = input("Choose an option: \n1. How many hours until download\n2. How many minutes to download\n3. How many seconds to download\nChoose an option: ")
#
# if op == "1":
#     print(f"The file will download in {total_seconds} sec.")
# elif op == "2":
#     total_minutes = total_seconds / 60
#     print(f"The file will download in {total_minutes} min.")
# elif op == "3":
#     total_hours = total_seconds / 3600
#     print(f"The file will download in {total_hours} hours.")
# else:
#     print("Error")