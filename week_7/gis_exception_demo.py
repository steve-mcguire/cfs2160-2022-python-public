def is_even(num):
    """
    Checks to see if a given value is odd or even:
    return: Boolean True or False
    """
    if num % 2 == 0:
        return True
    return False


# call function
print(is_even(34))
print(is_even(35))
print(is_even("c35"))
