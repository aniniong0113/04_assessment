import math


def round_up(amount, round_to):
    print(int(math.ceil(amount / round_to)) * round_to)
    return int(math.ceil(amount / round_to)) * round_to


def num_check(question, error, num_type, min, max):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response < min or response > max:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


while True:
    round_up(num_check("Please enter a number: ",
                       "Number must be between 0,10000",
                       float, 0, 10000),
             num_check("Please enter number to round to: ",
                       "Number must be greater than 0",
                       float, 0.0001, 10000))
