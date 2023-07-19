from functions import validate_eqn


def solve(eqn: str, var: str) -> str:
    eqn = eqn.replace(" ", "")
    result = ""
    token_symbols = ["+", "-", "/", "*", "^", "="]
    token_names = ["PLUS", "MINUS", "DIV", "MUL", "EXP", "EQUAL"]
    operations = []
    curr_num = ""

    validate_eqn(eqn, var)

    for i, letter in enumerate(eqn):
        if letter.isdigit() or letter == var:
            curr_num += letter

            if i != len(eqn) - 1:
                next = eqn[i + 1]

                if not next.isdigit():
                    operations.append(curr_num)
                    curr_num = ""
            else:
                operations.append(curr_num)

            continue

        if letter in token_symbols:
            tok_name_idx = token_symbols.index(letter)

            operations.append(token_names[tok_name_idx])

    return result


if __name__ == "__main__":
    equation = input("Enter equation: ")
    variable = input("Enter variable: ")

    solve(equation, variable)
