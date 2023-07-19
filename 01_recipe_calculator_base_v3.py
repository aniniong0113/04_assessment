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

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# apply currency
def currency(x):
    return f"${x:.2f}"


# gets expenses, returns list which has the data frame and sub total
def get_expenses(var_fixed):
    # Set up dictionaries and lists
    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":
        print()
        # get name, quantity and item
        item_name = not_blank("Item name: ", "The item name must not be blank")
        if item_name.lower() == "xxx":
            break

        if var_fixed == "fixed":
            quantity = 1
        else:
            quantity = num_check("Quantity:",
                                 "Tha amount must be a whole number,",
                                 int)

        price = num_check("How much for a single item? $",
                          "The price must be a number <more than zero>",
                          float)
        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]


# round up to whole number of choice
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to


# string checker
def is_string(input):
    return isinstance(input, str)


# unit converter
def convert_units(value, from_unit, to_unit):
    # Define conversion rates
    conversion_rates = {
        'kg': {'g': 1000, 'mg': 1_000_000, 'l': 1},
        'g': {'kg': 0.001, 'mg': 1000, 'l': 0.001},
        'mg': {'kg': 0.000001, 'g': 0.001, 'l': 0.000001},
        'l': {'kg': 1, 'g': 1000, 'mg': 1_000_000, 'ml':1000},
        'ml': {'l': 0.001},

    }

    # Check if units are valid
    if from_unit not in conversion_rates or to_unit not in conversion_rates:
        print("Invalid unit!")
        return

    # Perform conversion
    result = value * conversion_rates[from_unit][to_unit]
    return result


# main routine

print("**** Meal Cost Calculator ****\n")

meal_name = not_blank("What is the name of this recipe?: ", "Recipe name must not be blank.")

serving_amount = num_check("How many servings does your recipe make?: ", "Your answer must be larger than 0", float)