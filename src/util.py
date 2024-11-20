class UserInputError(Exception):
    pass


def validate_reference(year):

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
