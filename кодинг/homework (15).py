try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2
    print(f"result: {result}")

except ValueError:
    print("Error: You entered the wrong number!")

except ZeroDivisionError:
    print("Error: You cannot divide by zero!")

finally:
    print("The operation is complete.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 2

my_list = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter the element index: "))
    print(f"Element at index {index}: {my_list[index]}")

except ValueError:
    print("Error: Index must be an integer!")

except IndexError:
    print("Error: Element with such index does not exist!")

finally:
    print("The operation is complete.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~