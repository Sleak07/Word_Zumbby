# TODO: Check for error raise exceptions in python


def validate_age(age: int) -> None:
    if age < 0:
        raise ValueError("Age cannot be less than zero")
