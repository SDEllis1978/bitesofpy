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
        raise
    else:
        return n
    finally:
        if n < -0:
            raise ValueError
