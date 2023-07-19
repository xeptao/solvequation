from functions import validate_eqn

def solve(eqn: str, var: str) -> str:
    eqn = eqn.replace(" ", "")
    result = ""

    validate_eqn(eqn, var)

    return result


if __name__ == "__main__":
    equation = input("Enter equation: ")
    variable = input("Enter variable: ")

    solve(equation, variable)
