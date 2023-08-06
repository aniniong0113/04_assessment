# import libs
import pandas
import math


# functions

# round_up
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to


# not blank checker
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print(f"\n {error}. Please try again.\n")
            continue

        return response


# number checker that checks whether input is a float or
# an integer that is more than zero, takes in custom error messages
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response < 0 or response > 10000:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# apply currency
def currency(x):
    return f"${x:.2f}"


# round up to whole number of choice
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to


# unit converter
def convert_units(value, from_unit, to_unit):
    # Define conversion rates
    conversion_rates = {
        'kg': {'g': 1000, 'mg': 1_000_000, 'l': 1},
        'g': {'kg': 0.001, 'mg': 1000, 'l': 0.001},
        'mg': {'kg': 0.000001, 'g': 0.001, 'l': 0.000001},
        'l': {'kg': 1, 'g': 1000, 'mg': 1_000_000, 'ml': 1000},
        'ml': {'l': 0.001},

    }

    # Check if units are valid
    if from_unit not in conversion_rates or to_unit not in conversion_rates:
        print("Invalid unit!")
        return

    # Perform conversion
    result = value * conversion_rates[from_unit][to_unit]
    return result


def choice_checker(question, choice_list, error):
    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in choice_list:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item
        print(error)


# main routine
print("**** Meal Cost Calculator ****\n")

if choice_checker("Would you like to see the instructions?: ",
                  ["yes", "no"],
                  "Please enter either 'yes' or 'no'") == "yes":
    print("\nInstructions go here\n")

meal_name = not_blank("What is the name of this recipe?: ",
                      "Recipe name must not be blank.")

serving_amount = num_check("How many servings does your recipe make?: ",
                           "Your answer must be larger than 0",
                           float)
