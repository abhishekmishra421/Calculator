def print_calculator():
  """Prints a simple calculator to the console."""

  print("Calculator")
  print("-------")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")

  choice = int(input("Enter your choice: "))

  while choice != 5:
    if choice == 1:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      result = num1 + num2
      print(f"{num1} + {num2} = {result}")
    elif choice == 2:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      result = num1 - num2
      print(f"{num1} - {num2} = {result}")
    elif choice == 3:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      result = num1 * num2
      print(f"{num1} * {num2} = {result}")
    elif choice == 4:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      result = num1 / num2
      print(f"{num1} / {num2} = {result}")
    else:
      print("Invalid choice.")

    choice = int(input("Enter your choice: "))

  print("Exiting calculator.")


if __name__ == "__main__":
  print_calculator()