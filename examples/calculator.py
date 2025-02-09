import re
import sys
from typing import Callable, NamedTuple

from colorize import Colorize

HEADER = r"""
 ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
 """

total = 0


class Operation(NamedTuple):
    operator: str
    handler: Callable[[tuple[int | float, ...]], None]


def add_handler(*values: int | float) -> None:
    global total

    for value in values:
        total += value


def subtract_handler(*values: int | float) -> None:
    global total

    for value in values:
        total -= value


def multiply_handler(*values: int | float) -> None:
    global total

    for value in values:
        total *= value


def divide_handler(*values: int | float) -> None:
    global total

    for value in values:
        total /= value


def reset_handler(*_: int | float) -> None:
    global total
    total = 0


OPERATIONS: dict[str, Operation] = {
    "add": Operation(operator="+", handler=add_handler),
    "subtract": Operation(operator="-", handler=subtract_handler),
    "multiply": Operation(operator="*", handler=multiply_handler),
    "divide": Operation(operator="/", handler=divide_handler),
    "reset": Operation(operator="", handler=reset_handler),
}


def main() -> None:
    """The main entry point to the program"""

    print(HEADER)
    print(
        "Created by",
        Colorize("Nic").bold().color256(220) + ",",
        "the strongest sorcerer of the modern era.",
    )
    print(
        Colorize("To exit the program, press").italic(),
        Colorize("CTRL+C").bold().color256(0).on_color256(255),
    )

    try:
        start_calculator_loop()
    except KeyboardInterrupt:
        print()
        print("Thank you for playing. Goodbye!")
        sys.exit(0)


def start_calculator_loop() -> None:
    previous_calculation = ""

    while 1:
        display_separator()

        if previous_calculation != "":
            print(Colorize("Previous calculation").bold() + ":")
            print(Colorize(f"  {previous_calculation}").green())
            print()

        display_operations()
        print()

        print(f"Total: {total}")
        while 1:
            response = get_input("Please select an operation").strip()

            if not is_valid_operation(response):
                print_error("Whoops... that's not a valid option!")
                continue

            break

        index = int(response)
        valid_operations = tuple(OPERATIONS.keys())

        # -1 because the options are listed starting from 1, but tuples
        # are indexed starting from 0.
        key = valid_operations[index - 1]
        operation = OPERATIONS[key]

        # reset is a special case compared to the other handlers.
        if key.lower() == "reset":
            operation.handler()
            previous_calculation = ""
            continue

        while 1:
            while 1:
                response = get_input(
                    "Please provide a space-separated list of values."
                )
                response = response.strip()

                if response == "":
                    print_error("Please provide at least one value.")
                    continue

                break

            values_raw = response.split(sep=" ")

            values = []
            errors = []

            for value in values_raw:
                if not (value.isnumeric() or is_float(value)):
                    errors.append(value)
                    continue

                if value.isdigit():
                    values.append(int(value))
                elif is_float(value):
                    values.append(float(value))
                else:
                    raise AssertionError("unreachable")

            if len(errors) > 0:
                print_error(f"discarding invalid values: {", ".join(errors)}")

            if key.lower() == "divide" and 0 in values:
                print_error("divide by zero... you know you can't do that!")
                continue

            break

        total_before = total
        operation.handler(*values)

        operator = f" {operation.operator} "
        # Looks something like: "0 + 1 + 2 + 3 + 4 = 10"
        previous_calculation = (
            str(total_before)
            + operator
            + operator.join([str(v) for v in values])
            + " = "
            + str(total)
        )


def display_operations() -> None:
    valid_operations = OPERATIONS.keys()

    for i, operation in enumerate(valid_operations, start=1):
        print("  " + Colorize(str(i)).color256(219), operation)


def is_valid_operation(response: str, /) -> bool:
    return (
        response != ""
        and response.isdigit()
        and (1 <= int(response) <= len(OPERATIONS))
    )


def display_separator() -> None:
    print()
    print(Colorize("".center(80, "=")).dim())
    print()


def is_float(value: str, /) -> bool:
    pattern = re.compile(r"^[0-9]*\.[0-9]+$")
    return pattern.match(value) is not None


def print_error(text: str) -> None:
    print(Colorize("error").bold().red() + ":", text)


def get_input(prompt: str) -> str:
    print(
        Colorize("*").bold().cyan(),
        Colorize(prompt).bold(),
    )
    response = input("> ")
    print()
    return response


if __name__ == "__main__":
    main()
