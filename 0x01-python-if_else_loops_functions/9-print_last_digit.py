def print_last_digit(number):
    number = number < 0 and -number % 10 or number % 10
    print(number, end='')
    return number
