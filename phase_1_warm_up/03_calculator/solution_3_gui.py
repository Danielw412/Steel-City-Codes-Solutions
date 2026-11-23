"""Calculator solution with a tkinter window and clickable buttons."""

import tkinter as tk


# The calculator remembers these between button clicks.
state = {
    "first_number": None,
    "operator": None,
    "start_new_number": False,
}

# Each row of buttons, from top to bottom.
button_rows = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]


def calculate(first, operator, second):
    """Return the answer, or None when dividing by zero."""
    if operator == "+":
        return first + second

    if operator == "-":
        return first - second

    if operator == "*":
        return first * second

    if second == 0:
        return None

    return first / second


def format_number(number):
    """Show 4.0 as 4, but keep decimals such as 2.5."""
    number = round(number, 10)

    if number == int(number):
        return str(int(number))

    return str(number)


def press_digit(display, digit):
    """Add a digit or decimal point to the number on the display."""
    current = display.get()

    if state["start_new_number"] or current in ["0", "Error"]:
        current = ""
        state["start_new_number"] = False

    if digit == "." and "." in current:
        return

    if digit == "." and current == "":
        current = "0"

    display.set(current + digit)


def press_operator(display, operator):
    """Remember the first number and the operator."""
    if display.get() == "Error":
        return

    # If an operator is already waiting, finish that calculation first.
    if state["operator"] is not None and not state["start_new_number"]:
        press_equals(display)

    state["first_number"] = float(display.get())
    state["operator"] = operator
    state["start_new_number"] = True


def press_equals(display):
    """Calculate the answer and show it."""
    if state["operator"] is None or display.get() == "Error":
        return

    second_number = float(display.get())
    answer = calculate(state["first_number"], state["operator"], second_number)

    if answer is None:
        display.set("Error")
    else:
        display.set(format_number(answer))

    state["first_number"] = None
    state["operator"] = None
    state["start_new_number"] = True


def press_clear(display):
    """Reset the calculator."""
    display.set("0")
    state["first_number"] = None
    state["operator"] = None
    state["start_new_number"] = False


def press_button(display, label):
    """Decide what to do for the button that was clicked."""
    if label in ["+", "-", "*", "/"]:
        press_operator(display, label)
    elif label == "=":
        press_equals(display)
    else:
        press_digit(display, label)


def build_window():
    """Create the window, the display, and every button."""
    window = tk.Tk()
    window.title("Calculator")
    window.resizable(False, False)

    display = tk.StringVar(value="0")

    screen = tk.Label(
        window,
        textvariable=display,
        anchor="e",
        font=("Arial", 24),
        bg="white",
        relief="sunken",
        padx=10,
        pady=10,
    )
    screen.grid(row=0, column=0, columnspan=4, sticky="we", padx=8, pady=8)

    for row_index, row in enumerate(button_rows):
        for column_index, label in enumerate(row):
            button = tk.Button(
                window,
                text=label,
                width=5,
                height=2,
                font=("Arial", 16),
                command=lambda label=label: press_button(display, label),
            )
            button.grid(row=row_index + 1, column=column_index, padx=4, pady=4)

    clear_button = tk.Button(
        window,
        text="Clear",
        height=2,
        font=("Arial", 16),
        command=lambda: press_clear(display),
    )
    clear_button.grid(row=5, column=0, columnspan=4, sticky="we", padx=4, pady=4)

    return window


def main():
    window = build_window()
    window.mainloop()


if __name__ == "__main__":
    main()
