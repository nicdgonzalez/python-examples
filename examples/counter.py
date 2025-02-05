counter = 0


def add_to_counter(n: int = 1, /) -> None:
    global counter
    counter += n
    print(f"Added {n} to the counter! Now: {counter}")


print("Type a number to add to the counter!")

try:
    while 1:
        response = input()

        try:
            n = int(response)
        except ValueError:
            print("Whoops! That's not a number...")
            continue
        else:
            add_to_counter(n)
except KeyboardInterrupt:
    pass
