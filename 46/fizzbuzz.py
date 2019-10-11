def fizzbuzz(num):

    # for numbers divisible by 3 and 5
    if num % 15 == 0:
        return 'Fizz Buzz'

    # for numbers divisble by 3
    elif num % 3 == 0:
        return 'Fizz'
    # for numbers divisble by 5
    elif num % 5 == 0:
        return 'Buzz'

    else:
        return num