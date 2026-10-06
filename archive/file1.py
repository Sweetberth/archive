from archive.validation import (
    validate_id,
    validate_title,
    validate_city,
    validate_year,
    validate_condition,
)


def validate_record(record):
    """Validate a whole record dictionary.

    record is a dict with the keys: id, title, city, year, condition.

    Returns a LIST of reasons the record is invalid — one string per broken
    rule, in this field order: id, title, city, year, condition.
    An empty list means the record is valid.

    Do not re-write the rules here. Call the five functions above.
    """
    if not isinstance(record, dict):
        return ["Record must be a dictionary"]

    reasons = []
    for field_name, validator in [
        ("id", validate_id),
        ("title", validate_title),
        ("city", validate_city),
        ("year", validate_year),
        ("condition", validate_condition),
    ]:
        valid, reason = validator(record.get(field_name, ""))
        if not valid:
            reasons.append(reason)

    return reasons
