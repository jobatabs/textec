class UserInputError(Exception):
    pass


def validate_reference(author, title, journal, year):
    if not all([author, title, journal, year]):
        raise UserInputError("Adding was unsuccessful. All required fields need to be filled.")

    try:
        int(year)
    except ValueError as exc:
        raise UserInputError("Adding was unsuccessful. Invalid year.") from exc

    if int(year) < 0:
        raise UserInputError("Adding was unsuccessful. Invalid year.")

    # if len(content) < 5:
        # raise UserInputError("Todo content length must be greater than 4")

    # if len(content) > 100:
        # raise UserInputError("Todo content length must be smaller than 100")
