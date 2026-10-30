def is_boolean(value) -> bool:
    return isinstance(value, bool)


# by putting _ in front of the function,
# Python will not put it in the namespace of the module from where the import * is being called from
def _boolean_helper_1():
    pass


def _boolean_helper_2():
    pass
