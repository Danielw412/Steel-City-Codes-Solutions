"""Calculator solution organized with one function per job."""


def add(first, second):
    """Return first plus second."""
    return first + second


def subtract(first, second):
    """Return first minus second."""
    return first - second


def multiply(first, second):
    """Return first times second."""
    return first * second


def divide(first, second):
    """Return first divided by second, or None when second is zero."""
    if second == 0:
        return None

    return first / second


def calculate(first, operator, second):
    """Run the math for one operator and return the answer."""
    if operator == "+":
        return add(first, second)

    if operator == "-":
        return subtract(first, second)

    if operator == "*":
        return multiply(first, second)

    return divide(first, second)


def format_number(number):
    """Show 4.0 as 4, but keep decimals such as 2.5."""
    number = round(number, 10)

    if number == int(number):
        return str(int(number))

    return str(number)


def get_number(prompt):
    """Ask until the user types a number. Decimals are allowed."""
    while True:
        text = input(prompt).strip()

        try:
            return float(text)
        except ValueError:
            print("Please type a number, such as 7 or 2.5.")


def get_operator():
    """Ask until the user types +, -, *, or /."""
    while True:
        operator = input("Operator (+, -, *, /): ").strip()

        if operator in ["+", "-", "*", "/"]:
            return operator

        print("Please choose +, -, *, or /.")


def main():
    print("Calculator")

    while True:
        print()
        first = get_number("First number: ")
        operator = get_operator()
        second = get_number("Second number: ")

        answer = calculate(first, operator, second)

        if answer is None:
            print("You cannot divide by zero.")
        else:
            print(format_number(first), operator, format_number(second), "=", format_number(answer))

        again = input("Do another calculation? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
