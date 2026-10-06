def validate_condition(value):
    """A condition must be one of VALID_CONDITIONS, case-insensitively.

    Valid:   "fragile", "GOOD", "Fair"
    Invalid: "excellent", "", "ok"

    Returns (bool, str).
    """

    if value == "fragile" or "Good" or "Fair":
        
        return True, "Valid"

    else:
        return False, "Invalid"


condition = input("Enter condition: ")
validate_condition(condition)