#25 = 2, 5

# целое перевести в дробленое     (тут ошибка)

#num = float(input("Enter number: "))

#tens = num // 10
#units = num % 10
#result = tens + units
#print(f"result is => {result}")

#2, 5 = 25
# дребленое число перевести в целое
#tens = int(input("Enter the number of tens: "))
#units = int(input("Enter the number of units: "))

#result = tens * 10 + units

#print(f"result => {result}")



# самостоятельная робота

#1

# перевести градусы цельсия в фаренгейт
#celsius = float(input("Enter the temperature in Celsius => "))

#fahrenheit = celsius * 1.8 + 32

#print(f"Fahrenheit => {fahrenheit}")

#2

#перевести евро в долар по курсу

#euro = float(input("Enter the number of euro to exchange => "))
#rate = float(input("Enter the currency rate => "))

#dollar = euro * rate

#print(f"{euro} euro => {dollar} dollar")

#3

# Користувач з клавіатури вводить двозначне число. Наприклад, 26. Потрібно показати на різних рядках значення першого і другого розряду.

#num = int(input("Enter a number: "))

#tens = num // 10
#units = num % 10

#print(tens)
#print(units)

#4

# Користувач вводить із клавіатури дві цифри. Необхідно створити число, що містить ці цифри. Наприклад, якщо з клавіатури введено 9, 7, тоді потрібно сформувати число 97.

#tens = int(input("Enter the number of tens: "))
#units = int(input("Enter the number of units: "))

#result = tens * 10 + units

#print(f"result => {result}")

#5

# Користувач із клавіатури вводить тризначне число. Наприклад, 891. Потрібно показати на різних рядках значення першого, другого і третього розряду. Також потрібно показати на окремому рядку суму цих трьох чисел.

#number = int(input("Enter the three-digits number => "))

#units = number % 10
#tens = number // 10 % 10
#hundreds = number // 100

#print(f"{hundreds} {tens} {units}")
#print(f"{hundreds + tens + units}")
