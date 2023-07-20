from os import system as run


class Error:
    def __init__(self, eqn: str, var: str):
        self.var = var
        self.eqn = eqn
        self.red = "\033[93m"
        self.yellow = "\033[91m"
        self.end = "\033[0m"

    def throw(
        self,
        error_type: str,
        error_msg: str,
        start: None | int = None,
        end: None | int = None,
    ):
        run("clear")

        if start and end:
            print(self.eqn)
            print(
                f"{self.yellow}{' ' * (start - 1)}{'^' * (end - start + 1)}{self.end}"
            )

        print(f"{self.red}{error_type}{self.end}: {error_msg}")

        exit(1)
