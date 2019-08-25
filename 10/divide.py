def positive_divide(numerator, denominator):

    global n
    try:
        n = numerator / denominator
    except ZeroDivisionError as e:
        return 0
    try:
        numerator = int(numerator)
        denominator = int(denominator)
    except TypeError:
        if not isinstance(numerator, (int, float)) and not isinstance(denominator, (int, float)):
            raise
    else:
        return n
    finally:
        if n < -0:
            raise ValueError
