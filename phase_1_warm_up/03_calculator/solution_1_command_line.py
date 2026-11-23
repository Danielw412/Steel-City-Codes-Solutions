"""Calculator solution using one simple loop in the terminal."""


operators = ["+", "-", "*", "/"]

print("Calculator")
print("Type quit at any prompt to stop.")

while True:
    print()
    first_text = input("First number: ").strip()

    if first_text.lower() in ["quit", "q", "exit"]:
        print("Goodbye!")
        break

    try:
        first_number = float(first_text)
    except ValueError:
        print("That is not a number. Please try again.")
        continue

    operator = input("Operator (+, -, *, /): ").strip()

    if operator.lower() in ["quit", "q", "exit"]:
        print("Goodbye!")
        break

    if operator not in operators:
        print("Please choose +, -, *, or /.")
        continue

    second_text = input("Second number: ").strip()

    if second_text.lower() in ["quit", "q", "exit"]:
        print("Goodbye!")
        break

    try:
        second_number = float(second_text)
    except ValueError:
        print("That is not a number. Please try again.")
        continue

    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    else:
        if second_number == 0:
            print("You cannot divide by zero.")
            continue

        result = first_number / second_number

    print("Result:", result)
