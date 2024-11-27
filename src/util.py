import re


class UserInputError(Exception):
    pass


def validate_reference(author, title, journal, year, pp):
    if not all([author, title, journal, year]):
        raise UserInputError(
            "Adding was unsuccessful. All required fields need to be filled.")

    try:
        int(year)
    except ValueError as exc:
        raise UserInputError("Adding was unsuccessful. Invalid year.") from exc

    if int(year) < 0:
        raise UserInputError("Adding was unsuccessful. Invalid year.")

    if pp is not None:
        if len(pp) >= 20:
            raise UserInputError("Pages pertinent value is too long (needs to be less than 20 characters).")
        if not re.match(r"^\d+-?\d*$", pp):
            raise UserInputError(
                "Adding was unsuccessful. " +
                "Invalid pages pertinent (should be of either format start-end or page).")

    # if len(content) < 5:
        # raise UserInputError("Todo content length must be greater than 4")

    # if len(content) > 100:
        # raise UserInputError("Todo content length must be smaller than 100")
