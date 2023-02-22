# Password Requirements would need 1 number, and at least 7 characters.
# Changed to just make additional requirements use an and statement

def is_acceptable_password(password: str) -> bool:
    if len(password) > 7 and any(map(str.isdigit, password)):
        return True
    else:
        return False
