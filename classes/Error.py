class Error:
    def __init__(self, eqn: str, var: str):
        self.var = var
        self.eqn = eqn

    def throw(self, error_type: str, error_msg: str):
        print(f"\033[91m{error_type}\033[0m: {error_msg}")

        exit(1)
