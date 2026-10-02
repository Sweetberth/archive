def validate_id(value):
    """An ID is the letters 'MS' followed by exactly three digits.

    Valid:   "MS001", "MS742"
    Invalid: "MS1", "MS0012", "ms001", "XX001", "", "MS00A"

    Returns (bool, str). Testing something. this to be removed
    """

    if len(value) != 5 or value[0] != "M" or value[1] != "S":
        validation = "Invalid"

    else:
        validation = "Valid"

        for i in range(2, 5):
            if not value[i].isdigit():
                validation = "Invalid"

    if validation == "Invalid":
        return False, "Invalid"
    else:
        return True, "Valid"
    


Id = input("Enter ID: ")

validate_id(Id)