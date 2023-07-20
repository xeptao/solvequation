"""
The module for solve()
"""

from functions import validate_eqn


def solve(eqn: str, var: str) -> str:
    """
    Parameters:
        eqn (str): The equation
        var (str): The variable name used in the equation

    Returns:
        result (str): The result of the equation
    """

    TOKEN_SYMBOLS = ("+", "-", "/", "*", "^", "=")
    TOKEN_NAMES = ("PLUS", "MINUS", "DIV", "MUL", "EXP", "EQUAL")

    eqn = eqn.replace(" ", "")
    result = ""
    operations = []
    curr_num = ""

    validate_eqn(eqn, var)

    for i, letter in enumerate(eqn):
        if letter.isdigit() or letter == var:
            curr_num += letter

            if i != len(eqn) - 1:
                next_letter = eqn[i + 1]

                if not next_letter.isdigit():
                    operations.append(curr_num)
                    curr_num = ""
            else:
                operations.append(curr_num)

            continue

        if letter in TOKEN_SYMBOLS:
            tok_name_idx = TOKEN_SYMBOLS.index(letter)

            operations.append(TOKEN_NAMES[tok_name_idx])

    return result


if __name__ == "__main__":
    equation = input("Enter equation: ")
    variable = input("Enter variable: ")

    solve(equation, variable)
