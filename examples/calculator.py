import sys
import re
from typing import NamedTuple, Callable

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
        "Created by "
        + "\033[1;38;5;220m"  # bold, 256 pink fg
        + "Nic"
        + "\033[0m"  # reset all
        + ", the strongest programmer of the modern era"
    )
    print(
        "\033[3m"  # italic
        + "To exit the program, press "
        + "\033[1;23;38;5;0;48;5;255m"  # bold, reset italic, 256 black fg, 256 white bg  # noqa: E501
        + "CTRL+C"
        + "\033[3;39;49m"  # italic, reset fg, reset bg
        + "."
        + "\033[0m"  # reset all
    )

    try:
        start_calculator_loop()
    except KeyboardInterrupt:
        print()
        print("Thank you for playing. Bye!")
        sys.exit(0)


def start_calculator_loop() -> None:
    previous_calculation = ""

    while 1:
        display_separator()

        if previous_calculation != "":
            print(
                "\033[1m"  # bold
                + "Previous calculation"
                + "\033[0m"  # reset all
                + ":"
            )
            print(
                "  "
                + "\033[32m"  # green
                + previous_calculation
                + "\033[0m"  # reset all
            )
            print()

        display_operations()
        print()

        print(f"Total: {total}")
        while 1:
            response = get_input("Please select an operation")

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
            response = get_input(
                "Please provide a space-separated list of values."
            )

            if response == "":
                print_error("Please provide at least one value.")
                continue

            break

        values_raw = response.strip().split(sep=" ")

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
        print(
            "  "
            + "\033[38;5;219m"  # 256 pink fg
            + str(i)
            + "\033[0m"  # reset all
            + f" {operation}"
        )


def is_valid_operation(response: str, /) -> bool:
    return (
        response != ""
        and response.isdigit()
        and (1 <= int(response) <= len(OPERATIONS))
    )


def display_separator() -> None:
    print()
    print("\033[2m", end="")  # dim
    print("".center(80, "="))
    print("\033[0m", end="")  # reset all
    print()


def is_float(value: str, /) -> bool:
    pattern = re.compile(r"^[0-9]*\.[0-9]+$")
    return pattern.match(value) is not None


def print_error(text: str) -> None:
    print(
        "\033[1;31m"  # bold, red fg
        + "error"
        + "\033[0m"  # reset all
        + ": "
        + text
    )


def print_hint(text: str) -> None:
    print("\033[1;32mhint\033[0m:", text)


def get_input(prompt: str) -> str:
    print(
        "\033[1;36m"  # bold, cyan fg
        + "* "
        + "\033[39m"  # reset fg
        + prompt
        + "\033[0m"  # reset all
    )
    response = input("> ")
    print()
    return response.strip()


if __name__ == "__main__":
    main()
