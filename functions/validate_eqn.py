from classes import Error


def all_are_true(inputs: tuple, *conditions):
    results = []

    for condition in conditions:
        results.append(all(condition(input) for input in inputs))

    return False not in results


def any_is_true(inputs: tuple, condition):
    return any(condition(input) for input in inputs)


def validate_eqn(eqn: str, var: str):
    allowed = ("+", "-" "/", "*", "^", "=", var)
    error = Error(eqn, var)
    equal_count = 0
    tags = {
        "input": "InputError",
        "logic": "LogicError",
        "syntax": "SyntaxError",
    }
    common_messages = [lambda a, b: f"{a} and {b} can't be neighbours"]

    if "=" not in eqn:
        error.throw(tags["logic"], "An equation can't be made without an =")

    if var not in eqn:
        error.throw(
            tags["input"], f"Your equation needs to have {var} in it"
        )

    if len(var) != 1:
        error.throw(
            tags["input"],
            f"Your variable needs to be one character",
        )

    for i, letter in enumerate(eqn):
        is_last_letter = i == len(eqn) - 1
        is_first_letter = i == 0

        if not letter.isdigit() and letter not in allowed:
            error.throw(tags["input"], f"{letter} isn't allowed")

        if letter == "=":
            if is_last_letter or is_first_letter:
                error.throw(
                    tags["logic"],
                    "An equation can't be formed if there isn't two sides",
                )

            equal_count += 1

        if equal_count > 1:
            error.throw(tags["logic"], "There can't be multiple '='s")

        if not is_first_letter:
            prev = eqn[i - 1]

            if (
                letter == var
                and prev.isdigit()
                or letter.isdigit()
                and prev == var
            ):
                error.throw(
                    tags["syntax"],
                    common_messages[0](letter, prev),
                )

            if all_are_true(
                (letter, prev),
                lambda x: x in allowed,
                lambda x: x != var,
                lambda x: x != "=",
            ):
                error.throw(
                    tags["syntax"],
                    common_messages[0](letter, prev),
                )

                if letter == prev:
                    error.throw(
                        tags["syntax"],
                        common_messages[0](letter, prev),
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
