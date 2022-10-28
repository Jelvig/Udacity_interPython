class InvalidPasswordError(ValueError):
    pass


INVALID_PASSWORDS = (
    'password',
    'abc123',
    '123abc',
)


def validate_password(username, password):
    if password == username:
        raise InvalidPasswordError("Password cannot be the same as your username")
    if password in INVALID_PASSWORDS:
        raise InvalidPasswordError("Password is invalid, try a new one")


def create_account(username, password):
    return (username, password)


def main(username, password):
    try:
        validate_password(username, password)
    except InvalidPasswordError as err:
        print(err)
    else:
        account = create_account(username, password)
    finally:
        print("Validated password against username and collection")
