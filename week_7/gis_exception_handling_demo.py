def is_even(num):
    """
    Checks to see if a given value is odd or even:
    return: Boolean True or False
    returns error message if not possible
    """
    try:
        if num % 2 == 0:
            return True
        return False
    except TypeError:
        # does not follow encapsulation rules
        # ideally would throw new exception at this point
        #raise TypeError("Please enter numbers only")
        return "Please enter numbers only"


# call function
print(is_even(34))
print(is_even(35))
print(is_even("c35"))
