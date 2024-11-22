import re

class UserInputError(Exception):
    pass


def validate_reference(year, pp):

    try:
        int(year)
    except ValueError as exc:
        raise UserInputError("Adding was unsuccessful. Invalid year.") from exc

    if int(year) < 0:
        raise UserInputError("Adding was unsuccessful. Invalid year.")

    if pp is not None:
        if not re.match(r"^\d+-?\d*", pp):
            raise UserInputError("Adding was unsuccessful. \
                                 Invalid pages pertinent (should be of \
                                 either format start-end or page).")

    # if len(content) < 5:
        # raise UserInputError("Todo content length must be greater than 4")

    # if len(content) > 100:
        # raise UserInputError("Todo content length must be smaller than 100")
