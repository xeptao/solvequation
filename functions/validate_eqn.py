"""
This is the module for the validate_eqn functions and its helpers which
check if the logic, syntax, and input are correct.
"""

from classes import Error


def all_are_true(inputs: tuple, *conditions):
    """
    Checks if all given conditions are true for all inputs.

            Parameters:
                inputs (tuple): The inputs to apply the conditions for
                conditions: The conditions to apply to the inputs

            Returns:
                False if there are any Falses, else True
    """

    results = []

    for condition in conditions:
        results.append(all(condition(input) for input in inputs))

    return False not in results


def any_is_true(inputs: tuple, condition):
    """
    Checks if the given condition is true for any of the inputs.

            Parameters:
                inputs (tuple): The inputs to apply the conditions for
                condition: The condition to apply to the inputs

            Returns:
                True if there are any Trues, else False
    """

    return any(condition(input) for input in inputs)


def validate_eqn(eqn: str, var: str):
    """
    Checks if the logic, syntax, and the inputs for the
    variable and equation are correct.

            Parameters:
                inputs (tuple): The inputs to apply the conditions for
                condition: The condition to apply to the inputs

            Returns:
                True if there are any Trues, else False
    """

    allowed = ("+", "-", "/", "*", "^", "=", var)
    error = Error(eqn, var)
    equal_count = 0
    tags = {
        "input": "InputError",
        "logic": "LogicError",
        "syntax": "SyntaxError",
    }
    common_messages = [lambda a, b: f"{a} and {b} can't be next to eachother"]

    if len(var) != 1:
        error.throw(
            tags["input"],
            "Your variable needs to be one character",
        )

    if any_is_true(("=", var), lambda x: x not in eqn):
        error.throw(
            tags["input"],
            f"Your equation either doesn't have '=' or it doesn't have {var}",
        )

    for i, letter in enumerate(eqn):
        is_last = i == len(eqn) - 1
        is_first = i == 0

        if not letter.isdigit() and letter not in allowed:
            error.throw(tags["input"], f"{letter} isn't allowed", i)

        if letter == "=":
            equal_count += 1

            if is_last or is_first:
                error.throw(
                    tags["logic"],
                    "An equation can't be formed if there isn't two sides",
                    i,
                )

            if equal_count > 1:
                error.throw(tags["logic"], "There can't be multiple '='s")

        if not is_first:
            prev = eqn[i - 1]

            if (
                letter == var
                and prev.isdigit()
                or letter.isdigit()
                and prev == var
            ):
                error.throw(
                    tags["syntax"], common_messages[0](letter, prev), i, i + 1
                )

            if all_are_true(
                (letter, prev),
                lambda x: x in allowed,
                lambda x: x != var,
                lambda x: x != "=",
            ):
                if letter == prev:
                    error.throw(
                        tags["syntax"],
                        common_messages[0](letter, prev),
                        i,
                        i + 1,
                    )

                if prev != "-":
                    continue

                error.throw(
                    tags["syntax"], common_messages[0](letter, prev), i, i + 1
                )

    # placed at end because unpack would give an error if there were more
    # than one equal signs
    left, right = eqn.split("=")

    if left == right:
        error.throw(
            tags["logic"], "Nothing to compute since both sides are equal"
        )

    if any_is_true((left, right), lambda x: x == var):
        error.throw(tags["logic"], "This equation has already been solved")
