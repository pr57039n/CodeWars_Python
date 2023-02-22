# This version separates all conditions and allows modification through setting conditions to true if alternatives are met.
# This version makes the rules into an array so "One" argument is given

def is_acceptable_password(password: str) -> bool:
    rule1 = len(password) > 6
    rule2 = any(char.isdigit() for char in password)
    rule3 = any(char.isalpha() for char in password)
    if len(password) > 9:
        rule2 = rule3 = True
    return all([rule1, rule2, rule3])
