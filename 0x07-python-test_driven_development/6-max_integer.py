def max_integer(list=[]):
    """Defines a function to return the max integer in a list of ints.

    function returns None if list is empty.
    """
    if not list:
        return None

    max_int = list[0]
    for number in list:
        if number > max_int:
            max_int = number

    return max_int
