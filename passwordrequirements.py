def is_acceptable_password(password: str) -> bool:
    if len(password) < 7:
        return False
    else:
        return True
