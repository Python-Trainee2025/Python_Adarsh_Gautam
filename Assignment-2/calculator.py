# 4. create a calculator that takes two numbers and an operator (+, -, *, /) and performs the operation.
# Handle division by zero and invalid input errors.
while True:
    number1 = float(input("Enter a number: "))
    number2 = float(input("Enter another number: "))
    operator = input("Enter an operator (+, -, *, /) or 'exit' to quit: ")
    match operator:
            case '+':
                print(f"{number1 + number2:.2f}")
            case '-':
                print(f"{number1 - number2:.2f}")
            case '*':
                print(f"{number1 * number2:.2f}")
            case "/":
                if number2 != 0:
                    print(f"{number1 / number2:.2f}")
                else:
                    print("Error:cannot divide by zero")
            case 'exit':
                break
            case _:
                print("Wrong choice")
    prompt = input("Do you want to continue? (y/n): ").lower()
    if prompt == "n":
        break
