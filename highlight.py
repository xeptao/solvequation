from os import system as run

def highlight(string: str, start: str|int, end: str|int):
    start = int(start)
    end = int(end)

    run("clear")

    print(string)
    print(f"\033[93m{' ' * (start - 1)}{'^' * (end - start + 1)}\033[0m")


if __name__ == "__main__":
    highlight(
        input("Input String: "),
        input("Input Starting Position: "),
        input("Input Ending Position: "),
    )
